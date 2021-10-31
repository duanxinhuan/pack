import pymongo
from Inserters import MongoInserter,PostClient
from datetime import datetime

csv_list = [
    "csvs/Test task - Postgres - orders.csv",
    "csvs/Test task - Postgres - order_items.csv",
    "csvs/Test task - Postgres - deliveries.csv",
]

client = PostClient()
client.connect()
client.initDatabase()
client.insert(csv_list)

client.dispose()
# csv_list = [
#     "csvs/Test task - Mongo - customer_companies.csv",
#     "csvs/Test task - Mongo - customers.csv",
#     "csvs/Test task - Orders.csv"
    
# ]


# myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# mydb = myclient["mydatabase"]

# # mycol = mydb["Orders"]

# reader = MongoInserter()

# mycol = mydb["Orders"]

# start = datetime(2014, 9, 24, 7, 51, 4)
# end = datetime(2022, 9, 24, 7, 52, 4)

# for x in mycol.find({ 
#     "created_at":{'$gte': start, '$lt': end},
# }):
#     print(x)

# for name in csv_list:
#     reader.readCsv(mydb,name)
