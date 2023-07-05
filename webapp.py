# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 22:09:55 2023

@author: gourav
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('G:/ML_ABA/trained_model.sav','rb'))

def insurance_predicition(input_data):
    # changing input_data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    return 'The insurance cost is USD ' + str(prediction[0])

def main():
    
    st.title('Insurance Prediction Web Application')
    
    age = st.number_input('Age of the person', key='age_input')
    sex = st.number_input('Sex of the person', key='sex_input')
    bmi = st.number_input('BMI of the person', key='bmi_input')
    children = st.number_input('Number of childern', key='children_input')
    smoker = st.number_input('Smoker (1 - yes /0 - no)', key='smoker_input')
    region = st.number_input('Region? southeast:0,southwest:1,northeast:2,northwest:3', key='region_input')

    predict = ''
    
    if st.button('Calculate Insurance'):
        predict = insurance_predicition([age,sex,bmi,children,smoker,region])
    
    st.success(predict)
    

if __name__ == '__main__':
    main()