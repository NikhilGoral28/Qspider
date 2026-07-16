import streamlit as st
import pandas as pd
import joblib


st.set_page_config(
    page_icon='❤️',
    page_title="Heart Disease Prediction",
    layout='wide'
)

with open('notebook/log_model.joblib','rb') as file:
    model = joblib.load(file)


with st.sidebar:
    st.title("HEART DISEASE PREDICTION")


df = pd.read_csv("data/cleaned_data.csv")

with st.container(border=True):
    col1,col2 = st.columns(2)

    with col1:
        age = st.number_input("AGE ",min_value=1,
                              max_value=100,step = 5)
        gender = st.radio("GENDER", options=['Male', "Female"],
                          horizontal=True)
        
        gender = 1 if gender == 'Male' else 0
        d = {"Typical angina":0, "Antypical angina":1,
             "non-anginal pain":2, "Asymptotic":3}
        chest_pain_type = st.selectbox("CHEST PAIN TYPE",
                                       options=d.keys())
        chest_pain_type=d[chest_pain_type]

        resting_bp = st.number_input("RESTING BP", min_value=50,max_value=250,step=10)

        cholestrol = st.number_input("CHOLESTOL",min_value=50,max_value=600,step=20)

        fbs = st.radio("FASTING BLOOD SUGAR",options=['Yes','No'])
        fbs = 1 if fbs == 'Yes' else 0


    with col2:
        d1 = {"normal":0,'having ST-T wave abnormality':1,
              "left ventricular hypertropy":2}
        
        restecg = st.selectbox("RESTING ECG",options=d1.keys())
        restecg = d1[restecg]

        max_heart = st.number_input("Maximum_heart_Rate", min_value=50,max_value=250,step=5)

        exang = st.radio("Excercise Induces Angina", options=['Yes',"No"])
        exang = 1 if exang == 'Yes' else 0

        oldpeak = st.number_input('OLDPEAK',min_value=0.0,max_value=10.0,step=1.0)

        d2 = {"upsloping":0,"flat":1,"downsloping":2}
        slope = st.selectbox("SLOPE",options=d2)
        slope = d2[slope]

        num_vessels = st.selectbox("NUMBER OF MAJOR VESSELS",options=[0,1,2,3])

        d3 = {"Normal":1,"Fixed defect":2,"reversable defect":3}
        thal = st.selectbox("THAL",options=d3.keys())
        thal = d3[thal]

    if st.button("PREDICT"):
        data = [[age,gender,chest_pain_type,resting_bp,cholestrol,fbs,
                 restecg,max_heart,exang,oldpeak,slope,num_vessels,thal]]
        
        pred = model.predict(data)[0]

        if pred == 0:
            st.subheader("LOW RISK OF HEART DISEASE")
            st.image('static/heart2.jpeg', width=200)

        else:
            st.subheader("HIGH RISK OF HEART DISEASE")
            st.image('static/heart1.jpeg',width=200)