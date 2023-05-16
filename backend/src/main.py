from fastapi import FastAPI, Response
from services.ReviewService import ReviewService
from services.JSONEncoder import JSONEncoder
from entities.ReviewViewModel import ReviewViewModel

import numpy as np

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/reviews")
async def reviews():
    # get the reviews that are flagged as negative by a sentiment analysis model
    reviewService = ReviewService()
    reviews = reviewService.getReviews()
    negativeReviews = reviewService.getNegativeReviews(reviews)

    # encode the dataframe into json
    json = JSONEncoder().fromDataFrame(negativeReviews)
    return Response(content=json, media_type="application/json")