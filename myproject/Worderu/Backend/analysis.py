import transformers
from transformers import pipeline
from nrclex import NRCLex
import numpy as np
from textblob import TextBlob

def summary(text):

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn") #Using BART Large CNN model to summarise
    summary=summarizer(text, max_length=200, min_length=40, do_sample=False)
    summary=summary[0]['summary_text'] #This Module is Working

    return summary

def sentiment(text):

    emotion = NRCLex(text)
    detcted_emotions = emotion.raw_emotion_scores
    sentiment = emotion.top_emotions #Measuring the Top emotion in the text

    return sentiment

def positive(text):

    blob=TextBlob(text)
    sentiment_score=blob.sentiment.polarity #Returning the sentiment score from -1 to +1
    
    return sentiment_score

#This Module is working

