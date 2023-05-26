import pandas as pd
# from transformers import pipeline

class ReviewService:
    def __init__(self):
        self.reviews = []
        self.negativeReviews = []
        self.useColumns = ["reviews.text", 'sentiment']

    def getReviews(self):
        if len(self.reviews) <= 0:
            data = pd.read_csv("./data/amazon_product_reviews.csv", usecols=self.useColumns).sample(250)
            self.reviews = data
            return data
        else:
            return self.reviews
    
    def getNegativeReviews(self):
        if len(self.negativeReviews) <= 0:
            # amazon_negative_product_reviews.csv is created in a jupyter notebook with a sentiment analysis model
            # I saved that dataframe into this new csv
            data = pd.read_csv("./data/amazon_negative_product_reviews.csv", usecols=self.useColumns).sample(250)
            self.negativeReviews = data
            return data
        else:
            return self.negativeReviews
        # sentiment_pipeline = pipeline("sentiment-analysis", model='distilbert-base-uncased-finetuned-sst-2-english')
        
        # for index, row in reviews.iterrows():
        #     text = row['reviews.text']
        #     truncated_text = text[:512]  # Truncate to the first 512 tokens
        #     sentiment = sentiment_pipeline(truncated_text)
        #     reviews.loc[index, "sentiment"] = sentiment[0]["label"]
        
        # return reviews[
        #     reviews["sentiment"] == "NEGATIVE"
        # ]
    # def createReview(self, review):

