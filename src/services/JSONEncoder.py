import json
import pandas as pd

class JSONEncoder:
    def fromDataFrame(self, dataframe: pd.DataFrame):
        jsonData = json.dumps(
            json.loads(
                dataframe.reset_index()
                    .to_json(orient='records')
            ), indent=2
        )
        return jsonData