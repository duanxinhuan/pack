from configparser import ConfigParser
import psycopg2
from .postReader import PostReader

class PostClient:

    def __init__(self):
        self.conn = None
        self.cur = None
        self.reader = PostReader()

    def __config(self,filename='database.ini', section='postgresql'):
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return db

    def dispose(self):
         if self.conn is not None:
                self.conn.close()
                print('Database connection closed.')    

    def connect(self):
        """ Connect to the PostgreSQL database server """
        
        try:
            # read connection parameters
            params = self.__config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(**params)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def initDatabase(self):
        commands = (
            """
            CREATE TABLE orders(
                id INTEGER PRIMARY KEY,
                created_at time NOT NULL,
                order_name VARCHAR(255),
                customer_id VARCHAR(20)
            )
            """,
            """
            CREATE TABLE order_items(
                id INTEGER PRIMARY KEY,
                order_id INTEGER,
                price_per_unit 	FLOAT8,
                quantity INTEGER,
                product VARCHAR(255),
                FOREIGN KEY (order_id) REFERENCES orders (id)
            )
            """,
            """
            CREATE TABLE deliveries(
                id INTEGER PRIMARY KEY,
                order_item_id INTEGER,
                delivered_quantity INTEGER,
                FOREIGN KEY (order_item_id) REFERENCES order_items (id)         
            )
            """
            )  
        try:
            cur = self.conn.cursor()
            # create table one by one
            for command in commands:
                cur.execute(command)
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
    def insert(self, list):
        for path in list:
            self.reader.insert(path, self.conn)
        self.conn.commit()    