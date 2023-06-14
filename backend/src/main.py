from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from entities.ReviewPostModel import ReviewPostModel
from entities.ProductAnalyticsPostModel import ProductAnalyticsPostModel

from services.ReviewService import ReviewService
from services.AnalyticsService import AnalyticsService

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

@app.post('/analytics/product')
async def productAnalytics(product: ProductAnalyticsPostModel):
    analyticsService = AnalyticsService()
    valueCounts = analyticsService.productAnalytics(product.productName);
    json = JSONEncoder.fromObjects(valueCounts)
    return Response(content=json, media_type="application/json")

@app.get('/analytics/worst-products')
async def worstProductsAnalytics():
    analyticsService = AnalyticsService()
    worstProductNames = analyticsService.worstProductAnalysis()
    json = JSONEncoder.fromDataFrame(worstProductNames)
    return Response(content=json, media_type="application/json")

@app.get('/analytics/worst-issues')
async def worstProblemsAnalytics():
    analyticsService = AnalyticsService()
    worstProblems = analyticsService.worstProbmlemAnalysis()
    json = JSONEncoder.fromDataFrame(worstProblems)
    return Response(content=json, media_type="application/json")
    
