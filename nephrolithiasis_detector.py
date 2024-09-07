# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 23:27:07 2024

@author: SHRIYANS
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('nephrolithiasis_detection.sav', 'rb'))

def main():
    
    st.title('⚕️NephroCheck')
    
    st.caption("NephroCheck is a website application designed to assist in the early detection of nephrolithiasis(kidney stones) through urine analysis. NephroCheck aims to provide a convinient and accessible tool for individuals to monitor their kidney health and potentially identify signs of kidney stones formation.")
    
    
    st.info("🛈 Urine Parameter Information")
    st.caption("1. Gravity: Specific garvity of urine sample.")
    st.caption("2. pH: pH of urine sample.")
    st.caption("3. Osmolarity: Measure of the concentration of solutes (particles) in urine sample.")
    st.caption("4. Conductivity: Measure of urine sample's ability to conduct electric current. Conductivity is influenced by the concentration of ions (charged particles) present in the urine.")
    st.caption("6. Urea: Concentration of urea in urine sample.")
    st.caption("7. Calcium: Concentration of calcium in urine sample.")
    
    st.info("Nephrolithiasis Detector")
    st.caption("Kindly provide accurate and comprehensive details for all medical history questions to facilate accurate diagnosis.")
    
    gravity = st.text_input('Gravity')
    
    ph = st.text_input("pH")
    osmo = st.text_input("Osmolarity")
    cond = st.text_input("Conductivity")
    urea = st.text_input("Urea")
    calc = st.text_input("Calcium")
    
    nephrolithiasis_diagnosis = ''
    
    user_input = [gravity,ph,osmo,cond,urea,calc]
    
    if st.button('Predict'):
        
        if(gravity=='' or ph=='' or osmo=='' or cond=='' or urea=='' or calc==''):
            st.error("Kindly fill all the required parameters.")
        elif(float(gravity)<0):
            st.error("Specific gravity cannot be a negative value.")
        elif(float(ph)<0):
            st.error("pH cannot be a negative value.")
        elif(float(osmo)<0):
            st.error("Osmolarity cannot be a negative value.")
        elif(float(cond)<0):
            st.error("Conductivity cannot be a negative value.")
        elif(float(urea)<0):
            st.error("Urea concentration cannot be a negative value.")
        elif(float(calc)<0):
            st.error("Calcium concentration cannot be a negative value.")
        
        user_input = [ float (x) for x in user_input]
        
        nephrolithiasis_prediction = loaded_model.predict([user_input])
        
        if(nephrolithiasis_prediction[0]==0):
            nephrolithiasis_diagnosis = 'Negative for Nephrolithiasis'
        else:
            nephrolithiasis_diagnosis = 'Positive for Nephrolithiasis'
    
    st.success(nephrolithiasis_diagnosis)
    
    st.caption('Please remember that NephroCheck is not a substitute for professional medical advice, diagnosis, or treatment. If you have any health concerns, do consult a qualified healthcare provider.')
    
    st.markdown("<p style = 'text-align: center; black: red;'>Created by Shriyans Rout</p>", unsafe_allow_html=True)
    st.markdown("<p style = 'text-align: center; black: grey;'>@ NephroCheck-2024</p>", unsafe_allow_html=True)
    
    
    
if __name__=='__main__':
    main()