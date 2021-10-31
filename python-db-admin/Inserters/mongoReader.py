import pandas as pd
import datetime


class MongoInserter:

    def readCsv(self,dbClient,path):
        name = path.split(" - ").pop()
        name = name.split(".")[0]
        collection = dbClient[name]
        df = pd.read_csv(path)
        for index, row in df.iterrows():
            self.insert(row, collection)
        print(df)

    def insert(self,row, dbCollection):
        dict = row.to_dict()
        if "created_at" in dict.keys():
            dict["created_at"] = datetime.datetime.strptime(dict["created_at"],"%Y-%m-%dT%H:%M:%SZ")
            
        dbCollection.insert(dict)
