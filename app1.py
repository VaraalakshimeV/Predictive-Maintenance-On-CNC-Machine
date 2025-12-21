import mysql.connector
from flask import Flask, render_template,jsonify
import pickle
import pandas as pd
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import plotly.tools as tls
from plotly.graph_objs import*
from plotly.subplots import make_subplots


app = Flask(__name__)

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'varumysql',
    'database': 'pdm'
}


@app.route('/')
def retrieve_data():
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)

        # Create a cursor
        cursor = conn.cursor(dictionary=True)

        # SQL query to retrieve data
        query = "SELECT * FROM pdmdata"
        cursor.execute(query)

        # Fetch all rows
        data = cursor.fetchall()
        data1=pd.DataFrame(data,columns=['Spindle_Motor_Baselooseness_Vibration','Spindle_Motor_Bearing_Vibration','Spindle_Motor_Misalignment_Vibration','Spindle_Motor_Unbalance_Vibration'])
        #Remove timestamp 
        #Based on the ISO STANDARD VIBRATION  CREATE FAULT LABELS
        classes = []
        for i in data1['Spindle_Motor_Bearing_Vibration']:
            if i <=0.71:
                classes.append(0)
            elif 0.71 < i <= 1.80:
                classes.append(1)
            elif 1.80 < i <= 4.50:
                classes.append(2)
            else:
                classes.append(3)
        classes=pd.DataFrame(classes,columns=['Fault_type'])
        data1=pd.concat([data1,classes],axis=1)

        X=data1.drop(["Fault_type"],axis=1)
        Y=data1["Fault_type"]
        from sklearn.model_selection import train_test_split
        X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size=0.3, random_state=42)
        model=pd.read_pickle('mlp_clf_pdm.pkl')
        
        y_pred = model.predict(X_val)
        y_pred =pd.DataFrame(y_pred)

        y_pred_1= model.predict(X_train)
        y_pred_1=pd.DataFrame(y_pred_1)

        fault_types=pd.concat([y_pred_1,y_pred])

        fault_types=fault_types.add_prefix('class__')

        data1['Fault_types']=fault_types['class__0'].values

        data1=data1.drop(['Fault_type'],axis=1)
        data2=data1.head(25)
         #data2=data2.to_html(classes='table table-striped')
        #full data
        prob_data=data1
        data3 = data2.sort_values(by='Fault_types',ascending=False)

        #new code added here-label the faults
        fault_type_labels = {
        0: "No FAILURE",
        1: "LOW",
        2: "MEDIUM",
        3: "HIGH"
        }
        data3['Fault_type_label'] = data3['Fault_types'].map(fault_type_labels)

        data2=data2.to_html(classes='table table-striped',index=False)
        data3=data3.to_html(classes='table table-striped',index=False)

        #new code for probability
        prob_data['count'] = prob_data['Fault_types'].map(prob_data['Fault_types'].value_counts())
        prob_data['probability'] = prob_data['count'] / prob_data['count'].sum()
        fault_type_probs = pd.DataFrame(prob_data.groupby('Fault_types')['probability'].sum())
        fault_type_probs.rename(columns={'probability': 'probability_of_failure'}, inplace=True)
        print(fault_type_probs)

        highest_probability_fault = fault_type_probs['probability_of_failure'].idxmax()
        lowest_probability_fault = fault_type_probs['probability_of_failure'].idxmin()
        occurrence_ratings = {}
        for Fault_types  in fault_type_probs.index:
            if Fault_types  == highest_probability_fault:
                occurrence_ratings[Fault_types ] = 10  # Assign a high occurrence rating
            elif Fault_types  == lowest_probability_fault:
                occurrence_ratings[Fault_types ] = 1 
            else:
                occurrence_ratings[Fault_types ] = 5  # Assign a low occurrence rating (or adjust as needed)
        fault_type_probs['OccurrenceRating'] = fault_type_probs.index.map(occurrence_ratings)
        print(fault_type_probs[['probability_of_failure', 'OccurrenceRating']])

        highest_probability_fault = fault_type_probs['probability_of_failure'].idxmax()
        lowest_probability_fault = fault_type_probs['probability_of_failure'].idxmin()

        # Assign occurrence ratings based on the highest probability
        Detection = {}
        for Fault_types  in fault_type_probs.index:
            if Fault_types  == highest_probability_fault:
                Detection[Fault_types ] = 10  # Assign a high occurrence rating
            elif Fault_types  == lowest_probability_fault:
                Detection[Fault_types ] = 1 
            else:
                Detection[Fault_types ] = 5  # Assign a low occurrence rating (or adjust as needed)
        fault_type_probs['Detection'] = fault_type_probs.index.map(Detection)
        print(fault_type_probs[['probability_of_failure', 'OccurrenceRating','Detection']])

        # Assign occurrence ratings based on the highest probability
        Severity= {}
        for Fault_types  in fault_type_probs.index:
          if Fault_types  == 3:
            Severity[Fault_types ] = 7  # Assign a high occurrence rating
          elif Fault_types  == 2:
            Severity[Fault_types ] = 5 
          elif Fault_types  == 1:
            Severity[Fault_types ] = 3    
          else:
            Severity[Fault_types ] = 0  # Assign a low occurrence rating (or adjust as needed)
        fault_type_probs['Severity'] = fault_type_probs.index.map(Severity)
        print(fault_type_probs[['probability_of_failure', 'OccurrenceRating','Detection','Severity']])
        # Calculate the RPN for each fault type
        fault_type_probs['RPN'] = fault_type_probs['OccurrenceRating'] * fault_type_probs['Detection'] * fault_type_probs['Severity']
        fault_type_probs.reset_index(inplace=True)

        #new code
        # Create a list of the RPN values
        rpn_values = fault_type_probs['RPN'].tolist()

        # Find the index of the highest RPN value
        max_rpn_index = np.argmax(rpn_values)

        # Get the fault type with the highest RPN value
        max_rpn_fault_type = fault_type_probs.iloc[max_rpn_index]['Fault_types']

        if max_rpn_fault_type == 1:
            print("Low")
        elif max_rpn_fault_type == 2:
            print("Medium")
        else:
            print("High")

        # y_pred_proba = model.predict_proba(X)
        # fault_type_probabilities = np.mean(y_pred_proba, axis=0)
        # y_pred_proba_whole = np.sum(fault_type_probabilities)
        # print('Probability of each fault type:')
        # for i in range(len(fault_type_probabilities)):
        #      print(f'Fault type {i + 1}: {fault_type_probabilities[i]}')


        # fault_type_probs=fault_type_probs.to_html(classes='table table-striped')
        fig = go.Figure(data=[go.Bar(x=fault_type_probs['Fault_types'], y=fault_type_probs['OccurrenceRating'],name='OccurrenceRating',marker_color='darkblue')])
        print(fault_type_probs['Fault_types'])
        # Customize the layout
        fig.update_layout(
            title='Chart-1(FAULT TYPE VS OCCURRENCE)',
            xaxis_title='Fault_types',
            yaxis_title='OccurrenceRating',
            showlegend=True
        )

        fig_severity = go.Figure(data=[go.Bar(x=fault_type_probs['Fault_types'], y=fault_type_probs['Severity'],name='Severity',marker_color='darkblue')])

        # Customize the layout
        fig_severity.update_layout(
            title='Chart-2(FAULT TYPE VS SEVERITY)',
            xaxis_title='Fault_types',
            yaxis_title='Severity',
            showlegend=True
        )


        # Create a figure for the fault type vs detection line chart
        fig_detection = go.Figure(data=[go.Bar(x=fault_type_probs['Fault_types'], y=fault_type_probs['Detection'],name='Detection',marker_color='darkblue')])

        # Customize the layout
        fig_detection.update_layout(
            title='Chart-3(FAULT TYPE VS DETECTION)',
            xaxis_title='Fault_types',
            yaxis_title='Detection',
            showlegend=True
        )
        
        # fault_type_labels = {
        # 0: "No FAILURE",
        # 1: "LOW",
        # 2: "MEDIUM",
        # 3: "HIGH"
        # }

        # # Convert the fault type labels to integers
        # fault_type_labels_int = [int(label) for label in fault_type_labels]

        # # Add a bar trace for each fault type
        # fig_bar= go.Figure()
        # fig_bar.add_trace(go.Bar(x=fault_type_labels_int, y=data3['Spindle_Motor_Baselooseness_Vibration'], name='Spindle Motor Baselooseness Vibration'))

        # # Customize the layout
        # fig_bar.update_layout(
        #     title='Bar Chart-3(FAULT TYPE VS DETECTION)',
        #     xaxis_title='Fault_types',
        #     yaxis_title='Spindle_Motor_Baselooseness_Vibration',
        #     showlegend=True
        # )

        # # Display the figure
        # fig_bar.show()
        # chart_html_bar = fig_bar.to_html(full_html=False)

        # # Create a pie chart for fault type vs detection
        # pie_chart_detection = go.Figure(data=[go.Pie(labels=fault_type_probs['Fault_types'], values=fault_type_probs['probability_of_failure'], name='probability_of_failure')])

        # # Customize the layout
        # pie_chart_detection.update_layout(
        #     title='Pie Chart-2(FAULT TYPE VS probability_of_failure)',
        #     showlegend=True
        # )

        fault_type_labels = ["No Failure", "Low", "Medium", "High"]

        # Iterate over the fault_type_probs['Fault_types'] list and add the corresponding label from the fault_type_labels list to the new list
        for i in range(len(fault_type_probs['Fault_types'])):
            fault_type_labels[i] = fault_type_labels[fault_type_probs['Fault_types'][i]]

        # Update the labels argument of the go.Pie() function to use the new fault_type_labels list
        pie_chart_detection_2= go.Figure(data=[go.Pie(labels=fault_type_labels, values=fault_type_probs['probability_of_failure'], name='probability_of_failure')])

        # Customize the layout
        pie_chart_detection_2.update_layout(
            title='Pie Chart-2(FAULT TYPE VS probability_of_failure)',
            showlegend=True
        )

        # # Create a figure
        # fig_bar1 = go.Figure()

        # # Add a bar trace for each fault type
        # for Fault_type_label in data3['Fault_type_label']:
        #     fig_bar1.add_trace(go.Bar(x=[Fault_type_label], y=[data3['Spindle_Motor_Baselooseness_Vibration'].loc[Fault_type_label]],name='Fault_type_label'))

        # # Customize the layout
        # fig_bar1.update_layout(
        #     title='Bar Chart-3(FAULT TYPE VS Spindle_Motor_Baselooseness_Vibration )',
        #     xaxis_title='Fault_types',
        #     yaxis_title='Spindle_Motor_Baselooseness_Vibration',
        #     showlegend=True
        # )
        # bar_chart_html_1= fig_bar1.to_html(full_html=False)

        # fig_bar = make_subplots(rows=4, cols=1,shared_xaxes=True, subplot_titles=data1.columns[:-1])
        # print(fig_bar.print_grid())
        # # Create a bar chart for each feature
        # for i, feature in enumerate(data1.columns[:-1]):
        #     trace = go.Bar(x=data1['Fault_types'], y=data1[feature], name=feature)
        #     fig_bar.add_trace(trace,row=i+1,col=1)

        # # Update layout
        # fig_bar.update_layout(
        #     title='Bar Charts: Fault Type vs Features',
        #     xaxis=dict(title='Fault types'),
        #     showlegend=True
        # )

        # # Convert the figure to HTML
        # bar_chart_html = fig_bar.to_html(full_html=False) 


        # Convert the figure to HTML
        #pie_chart_html_detection = pie_chart_detection.to_html(full_html=False)
        pie_chart_html_detection_2= pie_chart_detection_2.to_html(full_html=False)
        # Convert the figure to HTML
        chart_html_detection = fig_detection.to_html(full_html=False)

        # Convert the figure to HTML
        chart_html_severity = fig_severity.to_html(full_html=False)



        # Convert the figure to HTML
        chart_html = fig.to_html(full_html=False)


        fault_type_probs=fault_type_probs.to_html(classes='table table-striped',index=False)

        #data_counts=data1['Fault_types'].value_counts()
        return render_template('data_template.html',data2=data2,data3=data3,fault_type_probs=fault_type_probs,chart_html=chart_html,chart_html_detection=chart_html_detection,chart_html_severity=chart_html_severity,pie_chart_html_detection_2= pie_chart_html_detection_2)

    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        conn.close()
# @app.route('/print_data.html',methods=['GET'])
# def print_data():
#     return render_template("print_data.html",final_data=data1)

# @app.route('/data')
# def visualization():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor(dictionary=True)
#         query = "SELECT * FROM pdmdata"
#         cursor.execute(query)
#         data = cursor.fetchall()
#         data1=pd.DataFrame(data,columns=['Spindle_Motor_Baselooseness_Vibration','Spindle_Motor_Bearing_Vibration','Spindle_Motor_Misalignment_Vibration','Spindle_Motor_Unbalance_Vibration'])
#         #Remove timestamp 
#         #Based on the ISO STANDARD VIBRATION  CREATE FAULT LABELS
#         classes = []
#         for i in data1['Spindle_Motor_Bearing_Vibration']:
#             if i <=0.71:
#                 classes.append(0)
#             elif 0.71 < i <= 1.80:
#                 classes.append(1)
#             elif 1.80 < i <= 4.50:
#                 classes.append(2)
#             else:
#                 classes.append(3)
#         classes=pd.DataFrame(classes,columns=['Fault_type'])
#         data1=pd.concat([data1,classes],axis=1)

#         X=data1.drop(["Fault_type"],axis=1)
#         Y=data1["Fault_type"]
#         from sklearn.model_selection import train_test_split
#         X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size=0.3, random_state=42)
#         model=pd.read_pickle('mlp_clf_pdm.pkl')
        
#         y_pred = model.predict(X_val)
#         y_pred =pd.DataFrame(y_pred)

#         y_pred_1= model.predict(X_train)
#         y_pred_1=pd.DataFrame(y_pred_1)

#         fault_types=pd.concat([y_pred_1,y_pred])

#         fault_types=fault_types.add_prefix('class__')

#         data1['Fault_types']=fault_types['class__0'].values

#         data1=data1.drop(['Fault_type'],axis=1)

#         data1=data1.to_html(classes='table table-striped')
#         data_counts=data1['Fault_types'].value_counts().to_dict()
#         return render_template('data_template.html',data_counts=data_counts)
        

#     except Exception as e:
#         return str(e)

#     finally:
#         cursor.close()
#         conn.close()

@app.route('/get_data1')
def get_data1():
    try:
        # Your existing code for processing data1 ...
        # Connect to the database
        conn = mysql.connector.connect(**db_config)

        # Create a cursor
        cursor = conn.cursor(dictionary=True)

        # SQL query to retrieve data
        query = "SELECT * FROM pdmdata"
        cursor.execute(query)

        # Fetch all rows
        data = cursor.fetchall()
        data1=pd.DataFrame(data,columns=['Spindle_Motor_Baselooseness_Vibration','Spindle_Motor_Bearing_Vibration','Spindle_Motor_Misalignment_Vibration','Spindle_Motor_Unbalance_Vibration'])
        #Remove timestamp 
        #Based on the ISO STANDARD VIBRATION  CREATE FAULT LABELS
        classes = []
        for i in data1['Spindle_Motor_Bearing_Vibration']:
            if i <=0.71:
                classes.append(0)
            elif 0.71 < i <= 1.80:
                classes.append(1)
            elif 1.80 < i <= 4.50:
                classes.append(2)
            else:
                classes.append(3)
        classes=pd.DataFrame(classes,columns=['Fault_type'])
        data1=pd.concat([data1,classes],axis=1)

        # Calculate the counts of each fault type
        data_counts = data1['Fault_types'].value_counts().to_dict()
        
        
        return jsonify(data_counts)
    
    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    app.run(debug=True) 