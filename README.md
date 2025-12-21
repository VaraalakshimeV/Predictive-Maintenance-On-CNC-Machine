🔧 Predictive Maintenance System for CNC Machines
Real-time fault detection and severity prediction system

This application monitors CNC machine health by analyzing live vibration sensor data from four critical components: spindle motor baselooseness, bearing, misalignment, and unbalance vibrations.
It utilizes a MySQL database that stores real-time sensor readings from CNC machines, predicting fault severity (No Failure, Low, Medium, High) based on ISO 10816 vibration standards.
The system calculates Risk Priority Numbers (RPN) using FMEA methodology (Severity × Occurrence × Detection) to prioritize maintenance actions and prevent costly machine failures.
Multi-Layer Perceptron (MLP) deep learning classifier achieves 98% accuracy, providing reliable predictions while avoiding overfitting issues found in other models tested.
Features interactive Plotly dashboards for live visualization, comprehensive fault-specific maintenance recommendations, and real-time monitoring of machine health status.

Prediction Model:

MULTI-LAYER PERCEPTRON (MLP)

Key Features:

Real-time Database Monitoring
RPN Analysis & Prioritization
Fault-Specific Recommendations
Live Interactive Dashboards


<img width="1110" height="538" alt="image" src="https://github.com/user-attachments/assets/a5e9dce3-f5e3-4c69-b152-658b4ace3ad4" />

