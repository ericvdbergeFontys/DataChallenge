import pandas as pd
from services.ReviewService import ReviewService

class AnalyticsService:
    def __init__(self):
        self.reviews = ReviewService().getNegativeReviews()

    def productAnalytics(self, productName: str):
        filtered_data = self.reviews[self.reviews['name'] == productName]
        grouped = filtered_data['cluster'].value_counts()
        return grouped
    
    def worstProductAnalysis(self):
        top_5_names = self.reviews['name'].value_counts().nlargest(5)
        name_count_df = pd.DataFrame({'name': top_5_names.index, 'count': top_5_names.values})
        return name_count_df
    
    def worstProbmlemAnalysis(self):
        top_5_clusters = self.reviews['cluster'].value_counts().nlargest(3)
        cluster_count_df = pd.DataFrame({'cluster': top_5_clusters.index, 'count': top_5_clusters.values})
        return cluster_count_df


