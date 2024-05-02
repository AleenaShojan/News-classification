import streamlit as st
import joblib
#load the trained model
model= joblib.load("news-classification-model.pkl")
#Define sentiment labels
news_labels = {'1': 'Technical' , '2': 'Business' , '3': 'Sports' , '4': 'Politics'}

#create Streamlit app
st.title("News Classification")

#Input text area

user_input =st.text_area("Enter news here")

#Prediction button

if st.button("Predict"):
    #perform sentiment prediction
    #print(user_input)
    Predicted_sentiment = model.predict([user_input])[0]
    #print("predicted_sentiment_label = sentiment_labels:"+str(Predicted_sentiment))
    predicted_news_label = news_labels[str(Predicted_sentiment)]

    #Display predicted sentlement
    st.info(f"Predicted category: {predicted_news_label}")
