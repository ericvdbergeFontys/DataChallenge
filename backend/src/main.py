from fastapi import FastAPI, Response
from services.ReviewService import ReviewService
from services.JSONEncoder import JSONEncoder
from mappers.ReviewMapper import ReviewMapper

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/reviews")
async def reviews():
    # get the reviews that are flagged as negative by a sentiment analysis model
    reviewService = ReviewService()
    negativeReviews = reviewService.getNegativeReviews()
    
    # encode the dataframe into json
    negativeReviews_formatted = ReviewMapper.MapFromDataFrameToReviewViewModel(negativeReviews)
    
    json = JSONEncoder.fromEntities(negativeReviews_formatted)
    return Response(content=json, media_type="application/json")

@app.post('/reviews')
async def createReview():
    print('test')
    return {"message": "Succeeded!"}
