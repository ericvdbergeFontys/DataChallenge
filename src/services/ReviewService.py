import pandas as pd
import numpy as np
from transformers import pipeline

class ReviewService:
    def __init__(self):
        useColumns = ["reviews.text"]
        data = pd.read_csv("./data/amazon_product_reviews.csv", usecols=useColumns).sample(50)
        self.data = data
    
    def getReviews(self):
        return self.data
    
    def getNegativeReviews(self, reviews: pd.DataFrame):
        sentiment_pipeline = pipeline("sentiment-analysis")
        
        for index, row in reviews.iterrows():
            sentiment = sentiment_pipeline(row['reviews.text'])
            reviews.loc[index, "sentiment"] = sentiment[0]["label"]
        
        return reviews[
            reviews["sentiment"] == "NEGATIVE"
        ]    