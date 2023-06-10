from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from entities.ReviewPostModel import ReviewPostModel

from services.ReviewService import ReviewService
from services.JSONEncoder import JSONEncoder
from mappers.ReviewMapper import ReviewMapper
from mappers.ProductMapper import ProductMapper

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/products")
async def products():
    # get the reviews that are flagged as negative by a sentiment analysis model
    reviewService = ReviewService()
    negativeReviews = reviewService.getReviews()
    negativeReviews = negativeReviews.drop_duplicates(subset=['name'], keep='first')

    # negativeReviews['name'] = negativeReviews['name'].unique()

    # encode the dataframe into json
    productEntities = ProductMapper.MapFromDataFrameToProductViewModel(negativeReviews)

    json = JSONEncoder.fromEntities(productEntities)
    return Response(content=json, media_type="application/json")

@app.get("/reviews")
async def reviews():
    # get the reviews that are flagged as negative by a sentiment analysis model
    reviewService = ReviewService()
    negativeReviews = reviewService.getNegativeReviews()
    
    # encode the dataframe into json
    negativeReviewsEntities = ReviewMapper.MapFromDataFrameToReviewViewModel(negativeReviews)
    
    json = JSONEncoder.fromEntities(negativeReviewsEntities)
    return Response(content=json, media_type="application/json")

@app.post('/reviews')
async def createReview(request: ReviewPostModel):
    reviewService = ReviewService()
    review = reviewService.generateReview(request)

    json = JSONEncoder.fromEntities([review])

    return Response(content=json, media_type="application/json")
