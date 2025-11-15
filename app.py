import streamlit as st
st.title('CALCULATE YOUR BMI')
h=1
wt=st.number_input('Enter your weight in kgs:')
h=st.number_input('Enter your height in ms:')
if h==0:
    bmi=0
else: 
    bmi=wt/h**2
st.success(f'Your BMI is {bmi} kg/m^2')

