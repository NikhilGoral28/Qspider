import pandas as pd
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from kneed import KneeLocator


#set the page config
st.set_page_config(page_icon="🛃", page_title="Customer Segmentation", layout='wide')

#load the data
file = st.file_uploader(" ",type=['csv'])

df = None

if file:
    df = pd.read_csv(file)

with st.sidebar:
    st.title("Customer Segmentation")
    if df is not None:
        features = st.multiselect("Select Features: ",options=df.columns, default=["Annual Income (k$)","Spending Score (1-100)"])
        df = df.loc[:,features]


def preprocessing(df):
    #encoding
    encoder = LabelEncoder()
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = encoder.fit_transform(df[col])
    
    return df


def elbow():
    out = []
    k_values = range(1,11)
    for i in k_values:
        model = KMeans(n_clusters=i)
        model.fit(df)
        out.append(model.inertia_)

    kL = KneeLocator(k_values,out,curve="convex",direction="decreasing")
    df1 = pd.DataFrame({"k_values":k_values,"intertia":out})

    st.subheader("ELBOW CURVE")

    fig = st.line_chart(data=df1,x="k_values",y='intertia')
    return kL.elbow


if df is not None:
    st.header("sample Data")
    st.write(df.sample(10))
    df = preprocessing(df)

    #optimized k value
    k = elbow()

    #model training
    model = KMeans(n_clusters=k)
    model.fit(df)

    labels = model.labels_

    df['clusters'] = labels

    #visualizationof culster
    st.subheader("Clustered Data")
    st.scatter_chart(data=df,x='Annual Income (k$)',y="Spending Score (1-100)",color='clusters')