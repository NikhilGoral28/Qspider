## Task 2


"""
after cleaning the text count the average word length show the percentage of stopword removed (if that option is selected)
"""

import streamlit as st
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import nltk

nltk.download('punkt')
nltk.download('stopwords')

st.title("Clean and Analyse Text")

text = st.text_area("Enter Text:")
remove_stop = st.checkbox("Remove Stopwords")
lowercase = st.checkbox("Convert to lowercase")
remove_punkt = st.checkbox("Remove Punctuation")

if st.button("Analyze"):

    result = text

    if lowercase:
        result = result.lower()

    if remove_punkt:
        result = re.sub(r'[^\w\s]', '', result)

    original_tokens = word_tokenize(text)
    cleaned_tokens = word_tokenize(result)

    if remove_stop:
        stop_words = set(stopwords.words("english"))
        filtered_tokens = [w for w in cleaned_tokens if w.lower() not in stop_words]
        result = " ".join(filtered_tokens)
    else:
        filtered_tokens = cleaned_tokens

    # Average word length
    word_length = [len(word) for word in filtered_tokens]
    avg_length = round(sum(word_length) / len(word_length), 3) if word_length else 0

    st.subheader("Cleaned Text")
    st.write(result)

    st.write("Word Count:", len(filtered_tokens))
    st.write("Average Word Length:", avg_length)

    if remove_stop:
        removed = len(original_tokens) - len(filtered_tokens)
        percent = (removed / len(original_tokens) * 100) if original_tokens else 0
        st.write(f"Stopwords removed: {removed} ({percent:.2f}%)")

    freq = Counter(filtered_tokens)
    st.write("Top 3 Words:", freq.most_common(3))