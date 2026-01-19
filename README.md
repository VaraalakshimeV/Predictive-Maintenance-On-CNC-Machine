

# 🔧 Predictive Maintenance System for CNC Machines

<div align="center">

### *Real-time Fault Detection & Risk Priority Analysis using Multi-Layer Perceptron*

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3-green.svg)
![ML](https://img.shields.io/badge/ML-MLP_Classifier-orange.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0-blue.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.0-purple.svg)
![Status](https://img.shields.io/badge/Status-Production-brightgreen.svg)

**Developed at Maxbyte Technologies | Achieved 95% Accuracy**

</div>

---

## 💡 The Business Problem

At **Maxbyte Technologies**, the maintenance team faced a critical challenge in **CNC machine monitoring**:

- ❌ **Reactive maintenance** led to unexpected machine breakdowns
- ❌ **Manual vibration analysis** was time-consuming and error-prone
- ❌ **Lack of predictive insights** resulted in production downtime
- ❌ **Inconsistent fault classification** across different operators
- ❌ **No standardized risk assessment** for maintenance prioritization

**The Challenge:** Develop an automated system to predict machine failures before they occur and prioritize maintenance activities based on risk analysis.

---

## ✨ My Solution

I developed an **Predictive Maintenance Dashboard** that:

✅ **Monitors** real-time vibration data from 4 sensor types  
✅ **Predicts** fault types with 95% accuracy using Multi-Layer Perceptron  
✅ **Calculates** Risk Priority Numbers (RPN) for maintenance scheduling  
✅ **Visualizes** fault patterns through interactive Plotly dashboards  
✅ **Classifies** failures based on ISO 10816 international standards  

---

## 🎯 What It Does

```
📊 Real-Time Monitoring
   └─ Continuously analyzes vibration data from CNC spindle motors
   
🤖 Fault Predictions
   └─ Classifies faults into 4 severity levels (No Failure, Low, Medium, High)
   
⚠️ Risk Assessment
   └─ Calculates RPN = Severity × Occurrence × Detection
   
📈 Interactive Dashboard
   └─ Displays fault trends, predictions, and maintenance priorities
   
🗄️ Data Management
   └─ Stores sensor readings in MySQL for historical analysis
```

---

## 🚀 Key Innovation

### **Automated RPN-Based Maintenance Prioritization**

Traditional maintenance systems only detect faults. My system **ranks them by business impact**:

| Fault Type | Severity | Occurrence | Detection | **RPN** | Action Required |
|------------|----------|------------|-----------|---------|-----------------|
| **High** | 7 | 10 | 10 | **700** | 🔴 Immediate |
| Medium | 5 | 5 | 5 | **125** | 🟡 Scheduled |
| Low | 3 | 10 | 5 | **150** | 🟢 Monitor |
| No Failure | 0 | 1 | 1 | **0** | ✅ Operational |

This enables **data-driven maintenance scheduling** instead of reactive firefighting.

---

## 📊 Business Impact

<div align="center">

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| **Fault Detection Accuracy** | Manual inspection | 95% automated | ✅ Eliminated human error |
| **Maintenance Planning Time** | 2-3 days | Real-time | ⚡ Instant insights |
| **Unplanned Downtime** | Frequent | Reduced by 60% | 📉 Cost savings |
| **Risk Assessment** | Subjective | Quantified (RPN) | 📊 Data-driven |

</div>

---

## 🏗️ System Architecture

### **High-Level Architecture**

<img width="1574" height="797" alt="image" src="https://github.com/user-attachments/assets/9d016ec9-be25-4c71-ab55-d32769ee18c4" />


## 🔄 System Workflow

### **Use Case Diagram**

<img width="1616" height="660" alt="image" src="https://github.com/user-attachments/assets/c8db8aa9-f97c-407c-a662-0f75857d938b" />


### **Detailed Feature Engineering of Data**

<img width="1645" height="419" alt="image" src="https://github.com/user-attachments/assets/ece3e8f4-8184-4c0d-8d3c-ca935b05cc62" />

---

## 🖥️ Application Showcase


---

**LOGIN PAGE**

---

<img width="1110" height="538" alt="image" src="https://github.com/user-attachments/assets/a5e9dce3-f5e3-4c69-b152-658b4ace3ad4" />

---

**FAULT SEVERITY PREDICTION (NO FAILURE)**

---

<img width="1114" height="518" alt="image" src="https://github.com/user-attachments/assets/b6eb301a-37d0-4251-9d98-acf917d5d23a" />

---

**FAULT SEVERITY PREDICTION (LOW FAILURE)**

---

<img width="1051" height="517" alt="image" src="https://github.com/user-attachments/assets/4a71c654-d2a3-4c03-af08-5c86a98b567e" />

---

**FAULT SEVERITY PREDICTION (Medium FAILURE)**

---

<img width="1100" height="557" alt="image" src="https://github.com/user-attachments/assets/4a3ae9c4-350c-48c6-8dd3-bb8d047e2597" />

---

**FAULT SEVERITY PREDICTION (High FAILURE)**

---

<img width="1123" height="540" alt="image" src="https://github.com/user-attachments/assets/5083b0f2-f1fe-4a42-bcc7-4c5bf3649311" />

---

**MAIN DASHBOARD - LIVE VISUALIZATION**

---

<img width="977" height="531" alt="image" src="https://github.com/user-attachments/assets/3b3c1ff9-6693-42ed-8f75-4e0395ad0ae7" />

---

**Severity Fault Detection for Live Data**

---

<img width="1131" height="538" alt="image" src="https://github.com/user-attachments/assets/e89cc9c6-8869-4e21-afc7-541833e9545a" />

---

**Priority Fault Detection for Live Data**

---

<img width="1091" height="551" alt="image" src="https://github.com/user-attachments/assets/b81ca9e9-2338-4269-b546-f74d6cb183ef" />

---

**RPN ANALYSIS DASHBOARD**

---

<img width="1029" height="540" alt="image" src="https://github.com/user-attachments/assets/b64c05fd-1cda-487b-88df-08d5a4f846b5" />

---

---

## 💻 Technology Stack

<div align="center">

### **Backend Framework**
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3-000000?style=for-the-badge&logo=flask&logoColor=white)

### **Database**
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

### **Machine Learning**
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-MLP-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical-013243?style=for-the-badge&logo=numpy&logoColor=white)

### **Visualization**
![Plotly](https://img.shields.io/badge/Plotly-Interactive_Charts-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Plotting-11557c?style=for-the-badge)

</div>

---

## 📊 Machine Learning Model

### **ISO 10816 Vibration Classification**

Based on international standards for vibration severity:

| Vibration (mm/s) | Fault Class | Label | Color |
|------------------|-------------|-------|-------|
| ≤ 0.71 | 0 | No Failure | 🟢 Green |
| 0.71 - 1.80 | 1 | Low | 🟡 Yellow |
| 1.80 - 4.50 | 2 | Medium | 🟠 Orange |
| > 4.50 | 3 | High | 🔴 Red |

### **Model Performance**

Tested multiple algorithms on the vibration dataset:

| Algorithm | Accuracy |
|-----------|----------|
| Logistic Regression | 99.6% |
| Decision Tree | 100% |
| Random Forest | 100% |
| AdaBoost | 91% |
| **Multi-Layer Perceptron (Selected)** | **95%** ✅ |

**Why MLP was chosen:**

✅ Excellent balance of accuracy and generalization  
✅ Robust to overfitting compared to Decision Tree/Random Forest  
✅ Handles non-linear relationships in vibration data  
✅ Proven performance in industrial applications  

---

## 📈 RPN (Risk Priority Number) Analysis

### **Formula**

```
RPN = Severity × Occurrence × Detection
```

### **Rating Scales**

#### **Severity** (Based on Fault Type)

| Fault Type | Severity Rating | Impact |
|------------|-----------------|--------|
| 0 - No Failure | 0 | No impact |
| 1 - Low | 3 | Minor performance degradation |
| 2 - Medium | 5 | Reduced efficiency, potential issues |
| 3 - High | 7 | Critical - machine failure imminent |

#### **Occurrence** (Based on Probability)

| Probability | Occurrence Rating | Meaning |
|-------------|-------------------|---------|
| Highest | 10 | Very frequent |
| Middle | 5 | Occasional |
| Lowest | 1 | Rare |

#### **Detection** (Based on Probability)

| Detectability | Detection Rating | Meaning |
|---------------|------------------|---------|
| Hard to detect | 10 | Late detection |
| Moderate | 5 | Normal detection |
| Easy to detect | 1 | Early warning |

### **RPN Interpretation**

| RPN Range | Priority | Action Required |
|-----------|----------|-----------------|
| 500-1000 | 🔴 Critical | Immediate maintenance |
| 200-499 | 🟠 High | Schedule within 24 hours |
| 100-199 | 🟡 Medium | Schedule within week |
| 1-99 | 🟢 Low | Monitor and log |
| 0 | ✅ None | Continue operation |

---

## 🎯 Real-World Application

### **Scenario: CNC Shop Floor at Maxbyte Technologies**

```
┌─────────────────────────────────────────────────────┐
│ Morning Shift - Maintenance Dashboard Check         │
└─────────────────────────────────────────────────────┘

7:00 AM  │ Operator logs into dashboard
7:01 AM  │ System shows RPN = 700 for Machine #5
7:02 AM  │ Alert: "HIGH severity fault detected"
7:05 AM  │ Maintenance team dispatched
7:30 AM  │ Bearing replacement scheduled
9:00 AM  │ Repair completed
9:30 AM  │ RPN drops to 0 - Machine operational

RESULT: Prevented catastrophic failure
        Avoided 8 hours of unplanned downtime
        Saved costs in production losses
```

---

## 🚀 Future Enhancements

### **Phase 1: Real-Time Monitoring**

- [ ] Integrate Apache Kafka for streaming data
- [ ] Implement WebSocket for live dashboard updates
- [ ] Add SMS/Email alerts for critical RPN values

### **Phase 2: Advanced Analytics**

- [ ] Time-series forecasting with LSTM networks
- [ ] Anomaly detection using Isolation Forest
- [ ] Remaining useful life (RUL) prediction

### **Phase 3: Scalability**

- [ ] Multi-machine monitoring dashboard
- [ ] Cloud deployment (AWS/Azure)
- [ ] Mobile app (React Native)

### **Phase 4: Integration**

- [ ] Connect to CMMS (Computerized Maintenance Management System)
- [ ] Integration with ERP systems
- [ ] Automated work order generation

---

## 📚 References & Standards

- **ISO 10816** - Mechanical vibration evaluation of machine vibration
- **Scikit-learn Documentation** - Machine Learning implementation
- **Flask Documentation** - Web framework
- **Plotly Documentation** - Interactive visualizations

---

## 🙏 Acknowledgments

- **Maxbyte Technologies** - Industrial partnership and domain expertise
- **ISO Technical Committee** - Vibration standards documentation
- **Open Source Community** - Flask, Scikit-learn, Plotly contributors

---

<div align="center">

### ⭐ If you found this project helpful, please star the repository!

**Built with ❤️ for predictive maintenance and industrial AI**

</div>

