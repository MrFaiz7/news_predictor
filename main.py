import joblib
from fastapi import FastAPI
import streamlit as st
from processtxt import process_text

app = FastAPI()

vect = joblib.load("vectorizer.pkl")
model = joblib.load("classifier.pkl")
id_to_category = {0: 'business', 4: 'tech', 2: 'politics', 3: 'sport', 1: 'entertainment'}


@app.get("/")
def read_root():
    return {"Hello Everyone and Welcome to News Article Classifier"}


@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To News Article Classifier': f'{name}'}


@app.post('/predict')
def predict_news_genre(article: str):
    clean_text = process_text(article)
    texts = [clean_text]
    text_features = vect.transform(texts)
    predictions = model.predict(text_features)
    for text, predicted in zip(texts, predictions):
        return "  - Predicted as: '{}'".format(id_to_category[predicted])


def main():
    st.title("News Article Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">News Classifier ML App </h2>
    </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    str = st.text_input("Article", "Type Here")
    result = ""
    if st.button("Predict"):
        result = predict_news_genre(str)
    st.success(result)

    if st.button("About"):
        st.text("Implementing a machine learning model to read the news headline or the content of the news and classifies the genre of the news accordingly. ")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()
