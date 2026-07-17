import streamlit as st
import pandas as pd
import joblib
import os


st.set_page_config(
    page_icon="❤️",
    page_title="Heart Disease Prediction",
    layout="wide"
)


# Get current project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Model path
MODEL_PATH = os.path.join(
    BASE_DIR,
    "notebook",
    "log_model.joblib"
)


# Dataset path
DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "cleaned_data.csv"
)


# Image paths
HEART_LOW = os.path.join(
    BASE_DIR,
    "static",
    "heart2.jpeg"
)

HEART_HIGH = os.path.join(
    BASE_DIR,
    "static",
    "heart1.jpeg"
)


# Load model
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()


with st.sidebar:
    st.title("❤️ HEART DISEASE PREDICTION")


# Load data (optional)
try:
    df = pd.read_csv(DATA_PATH)
except Exception:
    df = None


with st.container(border=True):

    col1, col2 = st.columns(2)


    with col1:

        age = st.number_input(
            "AGE",
            min_value=1,
            max_value=100,
            step=1
        )


        gender = st.radio(
            "GENDER",
            options=["Male", "Female"],
            horizontal=True
        )

        gender = 1 if gender == "Male" else 0


        chest_dict = {
            "Typical angina": 0,
            "Atypical angina": 1,
            "Non-anginal pain": 2,
            "Asymptomatic": 3
        }

        chest_pain = st.selectbox(
            "CHEST PAIN TYPE",
            options=list(chest_dict.keys())
        )

        chest_pain = chest_dict[chest_pain]


        resting_bp = st.number_input(
            "RESTING BP",
            min_value=50,
            max_value=250,
            step=10
        )


        cholesterol = st.number_input(
            "CHOLESTEROL",
            min_value=50,
            max_value=600,
            step=10
        )


        fbs = st.radio(
            "FASTING BLOOD SUGAR",
            options=["Yes", "No"]
        )

        fbs = 1 if fbs == "Yes" else 0



    with col2:

        restecg_dict = {
            "Normal": 0,
            "ST-T wave abnormality": 1,
            "Left ventricular hypertrophy": 2
        }


        restecg = st.selectbox(
            "RESTING ECG",
            options=list(restecg_dict.keys())
        )

        restecg = restecg_dict[restecg]


        max_heart = st.number_input(
            "MAXIMUM HEART RATE",
            min_value=50,
            max_value=250,
            step=5
        )


        exang = st.radio(
            "EXERCISE INDUCED ANGINA",
            options=["Yes", "No"]
        )

        exang = 1 if exang == "Yes" else 0



        oldpeak = st.number_input(
            "OLDPEAK",
            min_value=0.0,
            max_value=10.0,
            step=0.1
        )


        slope_dict = {
            "Upsloping": 0,
            "Flat": 1,
            "Downsloping": 2
        }


        slope = st.selectbox(
            "SLOPE",
            options=list(slope_dict.keys())
        )

        slope = slope_dict[slope]


        num_vessels = st.selectbox(
            "NUMBER OF MAJOR VESSELS",
            options=[0,1,2,3]
        )


        thal_dict = {
            "Normal": 1,
            "Fixed defect": 2,
            "Reversible defect": 3
        }


        thal = st.selectbox(
            "THAL",
            options=list(thal_dict.keys())
        )

        thal = thal_dict[thal]



    if st.button("PREDICT"):

        input_data = [[
            age,
            gender,
            chest_pain,
            resting_bp,
            cholesterol,
            fbs,
            restecg,
            max_heart,
            exang,
            oldpeak,
            slope,
            num_vessels,
            thal
        ]]


        prediction = model.predict(input_data)[0]


        if prediction == 0:

            st.subheader(
                "🟢 LOW RISK OF HEART DISEASE"
            )

            if os.path.exists(HEART_LOW):
                st.image(
                    HEART_LOW,
                    width=200
                )


        else:

            st.subheader(
                "🔴 HIGH RISK OF HEART DISEASE"
            )

            if os.path.exists(HEART_HIGH):
                st.image(
                    HEART_HIGH,
                    width=200
                )