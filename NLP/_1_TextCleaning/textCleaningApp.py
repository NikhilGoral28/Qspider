import streamlit as st
import re
import string

st.set_page_config(page_title="Text Cleaner", page_icon="🧹", layout="wide")

st.title("🧹 Text Cleaning App")
st.write("Paste your text below and choose the cleaning options.")

# Input
text = st.text_area("Enter Text", height=250)

st.subheader("Cleaning Options")

col1, col2 = st.columns(2)

with col1:
    lowercase = st.checkbox("Convert to Lowercase", value=True)
    remove_numbers = st.checkbox("Remove Numbers", value=False)
    remove_punctuation = st.checkbox("Remove Punctuation", value=True)
    remove_extra_spaces = st.checkbox("Remove Extra Spaces", value=True)

with col2:
    remove_urls = st.checkbox("Remove URLs", value=True)
    remove_emails = st.checkbox("Remove Email Addresses", value=True)
    remove_html = st.checkbox("Remove HTML Tags", value=True)
    remove_newlines = st.checkbox("Replace New Lines with Space", value=False)


def clean_text(text):
    if remove_html:
        text = re.sub(r"<.*?>", "", text)

    if remove_urls:
        text = re.sub(r"http\S+|www\S+", "", text)

    if remove_emails:
        text = re.sub(r"\S+@\S+", "", text)

    if lowercase:
        text = text.lower()

    if remove_numbers:
        text = re.sub(r"\d+", "", text)

    if remove_punctuation:
        text = text.translate(str.maketrans("", "", string.punctuation))

    if remove_newlines:
        text = text.replace("\n", " ")

    if remove_extra_spaces:
        text = re.sub(r"\s+", " ", text).strip()

    return text


if st.button("Clean Text"):
    if text.strip():
        cleaned = clean_text(text)

        st.subheader("Cleaned Text")
        st.text_area("", cleaned, height=250)

        st.download_button(
            label="📥 Download Cleaned Text",
            data=cleaned,
            file_name="cleaned_text.txt",
            mime="text/plain",
        )

        st.success("Text cleaned successfully!")
    else:
        st.warning("Please enter some text.")




import streamlit as st
import re
import contractions
import spacy
import emoji
from nltk.corpus import stopwords
import nltk

#load spacy model
nlp = spacy.load('en_core_web_sm')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
#words we want to keep after contraction expansion

important_words = {"i","am","is","are","was",
                   "were","be","been","being","have","has","had","do","does","did","not"}


#text cleaning function

def clean_text(text):

    #lowercase
    text = text.lower()
    #expand contractions
    text = contractions.fix(text)

    #Remove URLs
    text = re.sub(r'http\S+|www\S+','',text)

    #remove emails
    text = re.sub(r'\S+@\S+','',text)

    #remove emoji
    text = emoji.replace_emoji(text,replace=" ")

    #remove numbers

    text = re.sub(r'\d+','',text)

    #use spacy for punctuation removal

    doc = nlp(text)

    words = [token.text for token in doc if not token.is_punct]

    #remove stopwords but keep importanat words

    words = [word for word in words if (word not in stop_words) or (word in important_words)]

    return " ".join(words) 



#streamlit UI

st.title("Text Cleaning App")
st.set_page_config(page_icon='',page_title="Text Cleaning",'layout'='')