import streamlit as st
import numpy as np
import joblib

model = joblib.load('medical_nb.pkl')

disease_dict = {'Acne':0, 'Allergy':1, 'Diabetes':2, 'Fungal infection':3,
       'Urinary tract infection':4, 'Malaria':5, 'Migraine':6, 'Hepatitis B':7,
       'AIDS':8}
    
gender_dict = {
    'Male':1,
    'Female':0,
}

#main app started
st.header("Drug Prediction")

gender = st.selectbox(
    "Select Gender",
    ("Male", "Female")
)

age = st.text_input("Enter your Age:")

disease = st.selectbox(
    "Select the Disease:",
    ('Acne', 'Allergy', 'Diabetes', 'Fungal infection',
       'Urinary tract infection', 'Malaria', 'Migraine', 'Hepatitis B',
       'AIDS'
    )
)


submit = st.button("Submit")

if submit:
    gen = gender_dict[gender]
    dis = disease_dict[disease]
    age = int(age)
  
    test = [dis, gen, age]
    test = np.array(test)#List to numpy Array
    test = np.array(test).reshape(1,-1)# Convert 1d to 2d array 

    prediction = model.predict(test)
    st.write()
    st.write("Predicted Drug :-")
    st.subheader(prediction[0])
    st.write("NOTE:THIS IS SYSTEM GENERATED PREDICTION PLEASE CONSULT WITH YOUR DOCTOR/PHARMACIST BEFORE TAKING ANY ACTION BASED ON THIS PREDICTION")
