import streamlit as st
import pandas as pd
import pickle as pk


model = pk.load(open('model.pkl','rb'))
scaler = pk.load(open('scaler.pkl','rb'))

st.header('Loan Prediction App')
no_of_dependents = st.slider('choose no of dependents',0,5)
grad = st.selectbox('choose education',['Graduated','Non-graduated'])
self_emp = st.selectbox('Are you self employed',['Yes','No'])
Annual_income = st.slider('choose the annual income',0,10000000)
Laon_amount = st.slider('choose the loan amount',0,10000000)
Loan_dur = st.slider('Choose duration',0,20)
Civil = st.slider('Choose the credit the score',0,1000)
Assets = st.slider('Choose the assets',0,10000000)

if grad == 'Graduated':
    grad_s = 1
else:
    grad_s = 0

if self_emp == 'Yes':
    emp_s = 1
else:
    emp_s = 0

if st.button('Predict'):
    pred_data = pd.DataFrame([[no_of_dependents,grad_s,emp_s,Annual_income,Laon_amount,Loan_dur,Civil,Assets]],
                            columns=['no_of_dependents','education','self_employed','income_annum','loan_amount','loan_term','cibil_score','Assets'])
    pred_data = scaler.transform(pred_data)
    predict = model.predict(pred_data)
    if predict[0] == 1:
        st.markdown("Loan is approved")
    else:
        st.markdown("Loan is Rejected")
