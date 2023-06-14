import pandas as pd
import os
import pickle
import csv
from sentence_transformers import SentenceTransformer
from transformers import pipeline
from entities.ReviewPostModel import ReviewPostModel
from entities.ReviewViewModel import ReviewViewModel
from tensorflow.keras.models import load_model

class ReviewService:
    def __init__(self):
        self.reviews = []
        self.negativeReviews = []
        self.maxnRows = 250

    def getReviews(self):
        if len(self.reviews) <= 0:
            useColumns = ['reviews.text', 'name']
            data = pd.read_csv("./data/amazon_product_reviews.csv", usecols=useColumns)
            self.reviews = data
            return data
        else:
            return self.reviews
    
    def getNegativeReviews(self):
        if len(self.negativeReviews) <= 0:
            # amazon_negative_sentiment&emotion_reviews.csv is created in a jupyter notebook with a sentiment analysis and a
            # emotion classification model.I saved that dataframe into this new csv, this is what we are reading into memory here.
            useColumns = ["reviews.text", 'sentiment', 'emotion', 'name', 'cluster']
            data = pd.read_csv("./data/amazon_clustered_reviews.csv", usecols=useColumns)
            self.negativeReviews = data
            return data
        else:
            return self.negativeReviews
        
    def generateReview(self, reviewPost: ReviewPostModel):
        sentiment_pipeline = pipeline("sentiment-analysis", 'distilbert-base-uncased-finetuned-sst-2-english')
        sentiment = sentiment_pipeline(reviewPost.text)
    
        emotion_pipeline = pipeline("text-classification", "bdotloh/distilbert-base-uncased-empathetic-dialogues-context")
        emotion = emotion_pipeline(reviewPost.text)

        # load model and classify label
        current_directory = os.getcwd()  # Get the current working directory
        parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))  # Get the absolute path of the parent directory
        
        clusterClassifier = load_model(f'{parent_directory}\\src\\\models\\review_classifier.keras')
        embedder = SentenceTransformer('average_word_embeddings_glove.6B.300d')
        embeddings = embedder.encode([reviewPost.text])
        clusterEmbedding = clusterClassifier.predict(embeddings)
        # Load the LabelEncoder object from the file
        with open(f'{parent_directory}\\src\\\models\\label_encoder.pkl', 'rb') as f:
            label_encoder = pickle.load(f)
            cluster = label_encoder.inverse_transform(clusterEmbedding.argmax(axis=1))[0]
        
        #write to csv
        negative_emotions = ['annoyed', 'disappointed', 'anxious', 'jealous', 'angry', 'sentimental', 'sad',
                                 'emberrassed', 'disgusted', 'devastated', 'furious', 'afraid']
        if(sentiment[0]['label'] == "NEGATIVE" and emotion[0]['label'] in negative_emotions):
            # allowed to save into csv
            data = [reviewPost.productName, reviewPost.text, reviewPost.text, sentiment[0]['label'], emotion[0]['label'], "", "", cluster] #the data
            current_directory = os.getcwd()  # Get the current working directory
            parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))  # Get the absolute path of the parent directory
            with open(f'{parent_directory}\\src\\data\\amazon_clustered_reviews.csv', 'a', newline='') as f:
                writer = csv.writer(f) #this is the writer object
                writer.writerow(data) #this is the data

        review = ReviewViewModel(
            text= reviewPost.text,
            sentiment=sentiment[0]['label'],
            emotion=emotion[0]['label'],
            cluster=cluster
        ) 
        return review

