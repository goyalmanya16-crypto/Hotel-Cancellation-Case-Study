import numpy as np 
import pandas as pd
import streamlit as st 
import joblib 

# Lets load all the instances required over here 
with open('transformer.joblib','rb') as file:
    transformer=joblib.load(file)

# Lets load the model 
with open('final_model.joblib','rb') as file:
    model=joblib.load(file)

st.title('INN HOTEL GROUP')
st.header(':blue[This application will predict the chances of booking cancellation]')

# Lets Take input from user 
amnth=st.slider('Select Your Month of Arrival',min_value=1,max_value=12,step=1)
wkd_lambda=(lambda x:0 if x=='Mon' else 1 if x=='Tue' else 2 if x=='Wed' else 3 if x=='Thu'
            else 4 if x=='Fri' else 5 if x=='Sat' else 6)
awkd=wkd_lambda(st.selectbox('Select Your Weekday of Arrival',['Mon','Tue','Wed','Thu','Fri','Sat','Sun']))
dwkd=wkd_lambda(st.selectbox('Select Your Weekday of Departure',['Mon','Tue','Wed','Thu','Fri','Sat','Sun']))
wkend=st.number_input('Enter how many weekend nights are there in stay',min_value=0)
wk=st.number_input('Enter how many week nights are there in stay',min_value=0)
tootn=wkend+wk
mkt=(lambda x:0 if x=='Offline' else 1)(st.selectbox('How the booking has been made',['Offline','Online']))
lt=st.number_input('How many days prior the booking was made',min_value=0)
price=st.number_input('What is the average price per room',min_value=0)
adults=st.number_input('How many adults members in booking ',min_value=0)
spcl=st.selectbox('Select the number of special requests made',[0,1,2,3,4,5])
park=(lambda x:0 if x=='No' else 1)(st.selectbox('Does guest need parking space',['Yes','No']))

# Lets transform the data 
lt_t,price_t=transformer.transform([[lt,price]])[0]


# Create the input list 
input_list=[lt_t,spcl,price_t,adults,wkend,park,wk,mkt,amnth,awkd,tootn,dwkd]

# Make predictions 
prediction=model.predict_proba([input_list])[:,1][0]

# Lets show the probability 
if st.button('Predict'):
    st.success(f'Cancellation Chances {round(prediction,4)*100}%')