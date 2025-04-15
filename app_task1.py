import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.title("Mind-Blowing Word Cloud Generator")
st.write("Paste your text below and hit the button to generate an awesome word cloud!")

text = st.text_area("Enter your text here:", "")

if st.button("Generate Word Cloud"):
    if text:
        wc = WordCloud(
            width=800,
            height=400,
            background_color='white',
            colormap='viridis'
        ).generate(text)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wc, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.error("Please enter some text!")
