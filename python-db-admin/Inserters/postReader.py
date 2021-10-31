import pandas as pd
import psycopg2
from datetime import datetime
class PostReader:

    def insertOrders(self, orderList, conn):
        try:
            sql = "INSERT INTO orders(id, created_at, order_name,customer_id) VALUES(%s, %s, %s,%s)"
            cur = conn.cursor()
            # execute the INSERT statement
            cur.executemany(sql,orderList)
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)    

    def insert_order_items(self, itemList, conn):  
        try:
            sql = "INSERT INTO order_items(id, order_id, price_per_unit,quantity,product) VALUES(%s, %s, %s,%s,%s)"
            cur = conn.cursor()
            # execute the INSERT statement
            cur.executemany(sql,itemList)
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)    

    def insert_deliveries(self, deliveryList, conn):
        try:
            sql = "INSERT INTO deliveries(id, order_item_id,delivered_quantity) VALUES(%s, %s, %s)"
            cur = conn.cursor()
            # execute the INSERT statement
            cur.executemany(sql,deliveryList)
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)       
        
        
    def insert(self, path, conn):
        name = path.split(" - ").pop()
        name = name.split(".")[0]
        df = pd.read_csv(path)
        records = df.values.tolist()
        result = [tuple(x) for x in records]
        print(result[0])
        if name == "orders":
            for idx,i in enumerate(result):
                
                result[idx] = (i[0],datetime.strptime(i[1],"%Y-%m-%dT%H:%M:%SZ"), i[2], i[3])
                
                      
            self.insertOrders(result,conn) 

        elif name == "order_items":
            self.insert_order_items(result, conn)  
        else:
            self.insert_deliveries(result, conn)  

