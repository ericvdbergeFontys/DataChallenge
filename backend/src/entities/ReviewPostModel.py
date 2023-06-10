from pydantic import BaseModel

class ReviewPostModel(BaseModel):
   productName: str
   text: str

   