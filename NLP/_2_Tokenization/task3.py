"""
Write a function in streamlit that removes the english stopwords (like is the a)
cleaned tokens
count of removed stopwords

hint: use the nltk.corpus.stopwords

"""


import streamlit as st
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download('punkt')
nltk.download('stopwords')
st.title('Remove Stopwords')

text = st.text_area("Enter your text: ")

if st.button("Remove Stopwords"):
    tokens = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    filtered = [word for word in tokens if word.lower() not in stop_words]

    removal_count = len(tokens) - len(filtered)

    st.write("Filtered Tokens: ", filtered)
    st.write("Stopwords Removed: ", removal_count)
