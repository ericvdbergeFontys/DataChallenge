import pandas as pd
import numpy as np
from entities.ReviewViewModel import ReviewViewModel

class ReviewMapper:
    def MapFromDataFrameToReviewViewModel(dataframe: pd.DataFrame):
        reviews = []

        # Iterate over all the rows using iterrows()
        for _, row in dataframe.iterrows():
            reviews = reviews + [
                ReviewViewModel(
                    row['reviews.text'], 
                    row['sentiment'],
                    row['emotion'],
                    row['cluster']
                )
            ]
        
        return reviews
