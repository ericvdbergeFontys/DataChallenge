from pydantic import BaseModel

class ProductAnalyticsPostModel(BaseModel):
   productName: str