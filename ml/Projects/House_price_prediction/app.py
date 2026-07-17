
import os
import joblib
import streamlit as st
import pandas as pd


# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)


# -----------------------------------
# Base Directory
# -----------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# -----------------------------------
# File Paths
# -----------------------------------
MODEL_PATH = os.path.join(
    BASE_DIR,
    "notebook",
    "rf_model.joblib"
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "Cleaned_bangloreHousePrice_df.csv"
)

LOGO_PATH = os.path.join(
    BASE_DIR,
    "house_logo.png"
)


# -----------------------------------
# Load Model
# -----------------------------------
try:
    model = joblib.load(MODEL_PATH)

except Exception as e:
    st.error("Unable to load model")
    st.write(e)
    st.stop()



# -----------------------------------
# Load Dataset
# -----------------------------------
try:
    df = pd.read_csv(DATA_PATH)

except Exception as e:
    st.error("Unable to load dataset")
    st.write(e)
    st.stop()



# -----------------------------------
# Sidebar
# -----------------------------------
with st.sidebar:

    st.title("🏠 House Price Prediction")

    if os.path.exists(LOGO_PATH):
        st.image(
            LOGO_PATH,
            width=250
        )



# -----------------------------------
# Main Page
# -----------------------------------
st.header("🏠 Bangalore House Price Prediction")


if os.path.exists(LOGO_PATH):
    st.image(
        LOGO_PATH,
        width=300
    )



# -----------------------------------
# User Inputs
# -----------------------------------
with st.container(border=True):

    col1, col2 = st.columns(2)


    with col1:

        location = st.selectbox(
            "Location",
            sorted(df["location"].unique())
        )


        total_sqft = st.number_input(
            "Total Sqft",
            min_value=300,
            value=1000
        )



    with col2:

        bath = st.selectbox(
            "Bathrooms",
            sorted(df["bath"].unique())
        )


        bhk = st.selectbox(
            "BHK",
            sorted(df["bhk"].unique())
        )



# -----------------------------------
# Location Encoding
# -----------------------------------
def get_encoded_location(location):

    result = df.loc[
        df["location"] == location,
        "encoded_loc"
    ]

    if len(result) > 0:
        return result.iloc[0]

    return None



# -----------------------------------
# Prediction
# -----------------------------------
if st.button("Predict Price"):


    encoded_loc = get_encoded_location(location)


    if encoded_loc is None:

        st.error(
            "Location encoding not found"
        )


    else:


        # IMPORTANT:
        # Feature names must match training data exactly

        input_data = pd.DataFrame(
            [[
                total_sqft,
                bath,
                bhk,
                encoded_loc
            ]],
            columns=[
                "total_sqft",
                "bath",
                "bhk",
                "encoded_loc"
            ]
        )


        try:

            prediction = model.predict(
                input_data
            )[0]


            price = prediction * 100000


            st.success(
                f"Estimated Price: ₹ {price:,.2f}"
            )


        except Exception as e:

            st.error(
                "Prediction failed"
            )

            st.write(e)

