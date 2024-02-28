# -*- coding: utf-8 -*-


import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np




# loading the saved models

weather_model = pickle.load(open('weather_model.sav', 'rb'))




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('England_weather',
                          
                          ['England_weather_prediction_System'],
                          icons=['activity'],
                          default_index=0)
    
    

        
    
    

# Parkinson's Prediction Page
if (selected == "England_weather_prediction_System"):
    
    # page title
    st.title("England_weather_prediction_System using ML")
    
    col1, col2, col3, col4 = st.columns(4)  
    
    with col1:
        Temperature = st.text_input('Temperature (C)')
        
    with col2:
       Speed = st.text_input('Wind Speed (km/h)')
        
    with col3:
       Pressure = st.text_input('Pressure (millibars)')
        
    with col4:
        Humidity = st.text_input('Humidity')

        

        
    
    
    # code for Prediction
    England_weather = ''
    
    # creating a button for Prediction    
    if st.button("England_weather_prediction_System_Test_Result"):
        # Assuming Time, V1 to V28, and Amount are variables with proper numeric values
        input_data = np.array([[Temperature,Speed,Pressure, Humidity]], dtype=float)

        # Now use this input_data for prediction
        England_weather_prediction_System = weather_model.predict(input_data)
        #Credit_Card_Fraud_Detection = credit_model.predict([[Time,V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount]])                          
        
        if (England_weather_prediction_System[0] == 0):
          England_weather = "Rain"
        else:
         England_weather = "Snow"
        
    st.success(England_weather)






