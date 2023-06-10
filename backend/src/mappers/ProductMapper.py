import pandas as pd
from entities.ProductViewModel import ProductViewModel

class ProductMapper:
    def MapFromDataFrameToProductViewModel(dataframe: pd.DataFrame):
        products = []

        # Iterate over all the rows using iterrows()
        for _, row in dataframe.iterrows():
            products = products + [
                ProductViewModel(
                    row['name'], 
                )
            ]
        
        return products