import streamlit as st
import plotly.express as px
import glob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def read_files(sentiment_string):
    """Read all the text files in the diary folder and determines the sentiment of each text file"""
    polarity_list = []
    days = []
    text_files = glob.glob("diary/*.txt")
    for file_path in text_files:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            result = analyzer.polarity_scores(text)
            polarity_list.append(result[sentiment_string])
            days.append(f"Oct {file_path[14:16]}")
    return polarity_list, days

st.title("Diary Sentiment Analyzer")

analyzer = SentimentIntensityAnalyzer()

st.subheader("Positivity")

data_set1 = read_files("pos")
graph2 = px.line(x=data_set1[1], y=data_set1[0], 
                labels={"x":"Date", "y":"Negativity"})
st.plotly_chart(graph2)

st.subheader("Negativity")

data_set2 = read_files("neg")
graph2 = px.line(x=data_set2[1], y=data_set2[0], 
                labels={"x":"Date", "y":"Negativity"})
st.plotly_chart(graph2)