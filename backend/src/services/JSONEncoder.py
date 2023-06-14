import json
import pandas as pd

class JSONEncoder:
    def fromDataFrame(dataframe: pd.DataFrame):
        jsonData = json.dumps(
            json.loads(
                dataframe.reset_index()
                    .to_json(orient='records')
            ), indent=2
        )
        return jsonData
    
    def fromEntities(entities):
        jsonData =  json.dumps([e.__dict__ for e in entities], indent=4)
        return jsonData
    
    def fromObjects(objects):
        jsonData = json.dumps(objects.to_dict())
        return jsonData;