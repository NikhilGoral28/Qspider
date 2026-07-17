"""
Extend your streamlit tokenizer to:

tokenize at sentence level
display number of sentences
display first and last word of user input

hint:
use nltk.sent_tokenize() and list indexing
"""


import streamlit as st
from nltk.tokenize import word_tokenize, sent_tokenize
text = st.text_area("Enter your text: ")

if st.button("Anlyze"):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    st.write("Sentence count: ", len(sentences))
    st.write("First word: ",words[0] if words else "")
    st.write('Last Word: ', words[-1] if words else "")