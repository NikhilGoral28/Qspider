import os
import joblib
import streamlit as st
import pandas as pd


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_icon="🏠",
    page_title="House Price Prediction",
    layout="wide"
)


# -----------------------------
# Base Path
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# -----------------------------
# Load Model
# -----------------------------
MODEL_PATH = os.path.join(
    BASE_DIR,
    "notebook",
    "rf_model.joblib"
)

try:
    model = joblib.load(MODEL_PATH)

except FileNotFoundError:
    st.error(f"Model file not found: {MODEL_PATH}")
    st.stop()


# -----------------------------
# Load Dataset
# -----------------------------
DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "Cleaned_bangloreHousePrice_df.csv"
)

try:
    df = pd.read_csv(DATASET_PATH)

except FileNotFoundError:
    st.error(f"Dataset file not found: {DATASET_PATH}")
    st.stop()


# -----------------------------
# Logo Path
# -----------------------------
LOGO_PATH = os.path.join(
    BASE_DIR,
    "House_logo.png"
)


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🏠 House Price Prediction")

    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, width=250)


# -----------------------------
# Main UI
# -----------------------------
st.header("House Price Prediction 🏠")


if os.path.exists(LOGO_PATH):
    st.image(LOGO_PATH, width=300)


with st.container(border=True):

    col1, col2 = st.columns(2)


    with col1:

        location = st.selectbox(
            "Location",
            options=sorted(df["location"].unique())
        )


        sqft = st.number_input(
            "Total Sqft",
            min_value=300,
            value=1000
        )


    with col2:

        bath = st.selectbox(
            "Bathrooms",
            options=sorted(df["bath"].unique())
        )


        bhk = st.selectbox(
            "BHK",
            options=sorted(df["bhk"].unique())
        )



# -----------------------------
# Encode Location
# -----------------------------
def get_encoded_location(location):

    result = df.loc[
        df["location"] == location,
        "encoded_loc"
    ]

    if len(result) > 0:
        return result.iloc[0]

    return None



# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Price"):

    encoded_loc = get_encoded_location(location)


    if encoded_loc is None:

        st.error(
            "Location encoding not found."
        )

    else:

        input_data = pd.DataFrame(
            [[
                sqft,
                bath,
                bhk,
                encoded_loc
            ]],
            columns=[
                "sqft",
                "bath",
                "bhk",
                "encoded_loc"
            ]
        )


        prediction = model.predict(input_data)[0]


        price = prediction * 100000


        st.success(
            f"Estimated Price: ₹ {price:,.2f}"
        )