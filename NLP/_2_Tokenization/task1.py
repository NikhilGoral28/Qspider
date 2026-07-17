""""
practice projcet: Tokenizer in streamlit


Goal: Build a tokenizer app in streamlit to
accept user input
display
number of tokens
list of tokens
most frequent tokens

"""

import streamlit as st
from nltk.tokenize import word_tokenize
from collections import Counter
import nltk


nltk.download('punkt')
nltk.download('punkt-tab')

st.title("Text Tokenizer")

text = st.text_area("Enter some text: ")
if st.button("Tokenize"):

    tokens = word_tokenize(text)
    st.write("Number of tokens: ", len(tokens))
    st.write("Tokens: ",tokens)

    tokens_freq = Counter(tokens)
    st.write("Most Frequent tokens: ",tokens_freq.most_common(3))