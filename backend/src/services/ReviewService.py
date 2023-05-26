import pandas as pd

class ReviewService:
    def __init__(self):
        self.reviews = []
        self.negativeReviews = []
        self.useColumns = ["reviews.text", 'sentiment', 'emotion']
        self.maxnRows = 250

    def getReviews(self):
        if len(self.reviews) <= 0:
            data = pd.read_csv("./data/amazon_product_reviews.csv", usecols=self.useColumns, nrows=self.maxnRows)
            self.reviews = data
            return data
        else:
            return self.reviews
    
    def getNegativeReviews(self):
        if len(self.negativeReviews) <= 0:
            # amazon_negative_sentiment&emotion_reviews.csv is created in a jupyter notebook with a sentiment analysis and a
            # emotion classification model.I saved that dataframe into this new csv, this is what we are reading into memory here.
            data = pd.read_csv("./data/amazon_negative_sentiment&emotion_reviews.csv", usecols=self.useColumns, nrows=self.maxnRows)
            self.negativeReviews = data
            return data
        else:
            return self.negativeReviews

