#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 02:28:25 2024

@author: siddharth
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load models in binary mode
with open("/home/siddharth/Documents/gettin_better/mutiple_disease_prediction_sys/diabetes_model.sav", "rb") as file:
    diabetes_model = pickle.load(file)

with open("/home/siddharth/Documents/gettin_better/mutiple_disease_prediction_sys/heart_disease_model.sav", "rb") as file:
    heart_disease_model = pickle.load(file)

# Set the page config
st.set_page_config(page_title="DiseasePrognosis AI", page_icon="💉", layout="wide")

# Sidebar with Bootstrap icons
with st.sidebar:
    selected = option_menu(
        "DiseasePrognosis AI",
        ['Diabetes Prediction', 'Heart Disease Prediction'],
        icons=['activity', 'heart'],
        default_index=0
    )

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title('Diabetes Insight AI')
    st.write("Please enter the following details to predict the likelihood of diabetes:")

    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        glucose = st.text_input('Glucose Level')
    with col3:
        blood_pressure = st.text_input('Blood Pressure (mm Hg)')

    with col1:
        skin_thickness = st.text_input('Skin Thickness (mm)')
    with col2:
        insulin = st.text_input('Insulin Level (IU/mL)')
    with col3:
        bmi = st.text_input('BMI')

    with col1:
        dpf = st.text_input('Diabetes Pedigree Function')
    with col2:
        age = st.text_input('Age')

    # Code for Prediction
    diab_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Get Diabetes Test Result'):
        user_input = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]
        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is likely to have diabetes.'
        else:
            diab_diagnosis = 'The person is unlikely to have diabetes.'

    st.success(diab_diagnosis)

# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.title("CardioPredict AI")
    st.write("Please enter the following details to predict the likelihood of heart disease:")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain Types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure (mm Hg)')
    with col2:
        chol = st.text_input('Serum Cholesterol (mg/dL)')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dL (1 = true; 0 = false)')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)')

    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise')
    with col2:
        slope = st.text_input('Slope of the Peak Exercise ST Segment')
    with col3:
        ca = st.text_input('Number of Major Vessels Colored by Flourosopy')

    with col1:
        thal = st.text_input('Thalassemia (3 = normal; 6 = fixed defect; 7 = reversible defect)')

    # Code for Prediction
    heart_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Get Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is likely to have heart disease.'
        else:
            heart_diagnosis = 'The person is unlikely to have heart disease.'

    st.success(heart_diagnosis)
