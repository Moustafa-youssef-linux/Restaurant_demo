import mysql.connector


def database_con():

  dbconfig = { 'host': '127.0.0.1',
               'user': 'rest',
               'password': 'root123',
               'database': 'restaurant', 
             }

  conn = mysql.connector.connect(**dbconfig)
  cursor = conn.cursor()
  _SQL = """select rest_name from rest"""
  cursor.execute(_SQL)
  restaurants = cursor.fetchall()
  return restaurants
  #for row in res:
  #    print(row)
def get_rest():
    dbconfig = { 'host': '127.0.0.1',
               'user': 'rest',
               'password': 'root123',
               'database': 'restaurant',
             }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """select rest_name from rest"""
    cursor.execute(_SQL)
    restaurants = cursor.fetchall()
    cursor.close()
    conn.close()

    return restaurants

def auth_(username: str , password: str) -> bool:
    dbconfig = { 'host': '127.0.0.1',
               'user': 'rest',
               'password': 'root123',
               'database': 'restaurant',
             }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    user_records = cursor.fetchall()
    cursor.close()
    conn.close()
    
    #users_in_db = users_records[0][1]
    #print (user_records[0])
    for user in user_records:
        #print (user)
        if username == user[1] and password == user[6]:
            #print ("authentication is done")
            return True
    return False    

def register_(username:str,fn:str,ln:str,age:int,gender:str,password:str): -> None
    dbconfig = { 'host': '127.0.0.1',
               'user': 'rest',
               'password': 'root123',
               'database': 'restaurant',
             }
    #print (username + fn + ln + str(age) + gender + password)
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    query = "insert into users (username, fn, ln ,age ,gender ,password) values (%s, %s, %s, %s, %s, %s)"
    values = (username, fn, ln, age, gender, password)
    cursor.execute(query,values)
    #age_ = str(age)
    #cursor.execute("insert into users values (%s, %s, %s, %s, %s, $s)", (username, fn, ln, age_, gender, password))
    conn.commit()
    cursor.close()
    conn.close()


def create_(name:str,food_type:str,review:str): -> None
    dbconfig = { 'host': '127.0.0.1',
               'user': 'rest',
               'password': 'root123',
               'database': 'restaurant',
             }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    query = "insert into res (rest_name,food_type,review) values (%s, %s, %s)"
    values = (name,food_type,review)
    cursor.execute(query,values)
    conn.commit()
    cursor.close()
    conn.close()

