from mysql.connector import MySQLConnection, Error
 
def connect():
    """ Connect MySql """
    db_config = {
        'host': 'localhost',
        'database': 'DatingApp',
        'user': 'root',
        'password': 'Anhtung777'
    }
 
    conn = None
 
    try:
        conn = MySQLConnection(**db_config)
 
        if conn.is_connected():
            return conn
 
    except Error as error:
        print(error)
 
    return conn

#----------------------------------------------------------------------------------------------------

#get data from db

def counts():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT User_id FROM User_account")
        rows = cursor.fetchall()
        
        return(cursor.rowcount)
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()

def show_account():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User_account")
        rows = cursor.fetchall()
 
        return(rows)
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def show_info(i):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT User_name, User_dob, User_gender, User_location, User_bio FROM User_Information WHERE id = %s", (i,))
        rows = cursor.fetchall()
 
        return(rows[0])
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def show_new_added_dob():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT User_dob FROM User_information WHERE id = (SELECT MAX(id) FROM User_information);")
        rows = cursor.fetchall()
 
        return(rows[0][0])
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()       

def show_name(i):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT User_name FROM User_Information WHERE id = %s", (i,))
        rows = cursor.fetchall()
 
        return(rows[0])
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def show_basics(i):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT Basics_height, Basics_weight, Basics_zodiac, Basics_education, Basics_workout, Basics_smoke, Basics_drink FROM User_basics WHERE id = %s", (i,))
        rows = cursor.fetchall()
 
        return(rows[0])
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def show_interests(i):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT interest1, interest2, interest3, interest4, interest5 FROM User_interests WHERE id = %s", (i,))
        rows = cursor.fetchall()
 
        return(rows[0])
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def show_seen():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT Seen FROM User_match")
        rows = cursor.fetchall()
 
        return(rows)
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def update_seen(new_seen, user_id):
    query = """ UPDATE User_match
                SET Seen = %s
                WHERE id = %s """
 
    data = (new_seen, user_id)
    try:
        conn = connect()
        
        cursor = conn.cursor()
        cursor.execute(query, data)
        
        conn.commit()
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def show_liked(i):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT Liked FROM User_match WHERE id = %s", (i,))
        rows = cursor.fetchall()
 
        return(rows)
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def show_disliked(i):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT Disliked FROM User_match WHERE id = %s", (i,))
        rows = cursor.fetchall()
 
        return(rows)
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def show_matched(user_id):        
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT Matched FROM User_match WHERE id = %s", (user_id,))
        rows = cursor.fetchall()
 
        return(rows)
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()

def update_liked(new_liked, user_id):
    query = """ UPDATE User_match
                SET Liked = %s
                WHERE id = %s """
 
    data = (new_liked, user_id)
    try:
        conn = connect()
        
        cursor = conn.cursor()
        cursor.execute(query, data)
        
        conn.commit()
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def update_disliked(new_liked, user_id):
    query = """ UPDATE User_match
                SET Disliked = %s
                WHERE id = %s """
 
    data = (new_liked, user_id)
    try:
        conn = connect()
        
        cursor = conn.cursor()
        cursor.execute(query, data)
        
        conn.commit()
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def update_matched(new_matched, user_id):
    query = """ UPDATE User_match
                SET Matched = %s
                WHERE id = %s """
 
    data = (new_matched, user_id)
    try:
        conn = connect()
        
        cursor = conn.cursor()
        cursor.execute(query, data)
        
        conn.commit()
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
#----------------------------------------------------------------------------------------------------
#set data to db

def insert_account(Account_username, Account_password):
    query = "INSERT INTO User_account(Account_username, Account_password) " \
            "VALUES(%s,%s)"
    args = (Account_username, Account_password)
 
    try:
 
        conn = connect()
 
        cursor = conn.cursor()
        cursor.execute(query, args)
  
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        # close connection
        cursor.close()
        conn.close()

def insert_matching(seen):
    query = "INSERT INTO User_match(Seen) " \
            "VALUES(%s)"
    args = (seen,)
 
    try:
 
        conn = connect()
 
        cursor = conn.cursor()
        cursor.execute(query, args)
  
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        # close connection
        cursor.close()
        conn.close()

def insert_info(User_name, User_dob, User_gender, User_location, User_bio):
    query = "INSERT INTO User_information(User_name, User_dob, User_gender, User_location, User_bio) " \
            "VALUES(%s,%s,%s,%s,%s)"
    args = (User_name, User_dob, User_gender, User_location, User_bio)
 
    try:
 
        conn = connect()
 
        cursor = conn.cursor()
        cursor.execute(query, args)
  
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def insert_baiscs(Basics_height, Basics_weight, Basics_zodiac, Basics_education, Basics_workout, Basics_smoke, Basics_drink):
    query = "INSERT INTO User_basics(Basics_height, Basics_weight, Basics_zodiac, Basics_education, Basics_workout, Basics_smoke, Basics_drink) " \
            "VALUES(%s,%s,%s,%s,%s,%s,%s)"
    args = (Basics_height, Basics_weight, Basics_zodiac, Basics_education, Basics_workout, Basics_smoke, Basics_drink)
 
    try:
 
        conn = connect()
 
        cursor = conn.cursor()
        cursor.execute(query, args)
  
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def insert_interest(in1, in2, in3, in4, in5):
    query = "INSERT INTO User_interests(interest1, interest2, interest3, interest4, interest5) " \
            "VALUES(%s,%s,%s,%s,%s)"
    args = (in1, in2, in3, in4, in5)
 
    try:
 
        conn = connect()
 
        cursor = conn.cursor()
        cursor.execute(query, args)
  
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
              
        
#insert Image
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData
def insert_image(photo1, photo2, photo3):
    query = "INSERT INTO User_photo(image1, image2, image3) " \
            "VALUES(%s, %s, %s)"
    args = (convertToBinaryData(photo1), convertToBinaryData(photo2), convertToBinaryData(photo3))
 
    try:
 
        conn = connect()
 
        cursor = conn.cursor()
        cursor.execute(query, args)
  
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def show_photo(id):
    query = """ SELECT image1, image2, image3 FROM User_photo WHERE id = %s """
    data = (id,)
    
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query, data)
        rows = cursor.fetchall()
 
        return(rows[0])
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
        
#----------------------------------------------------------------------------------------------------
#auto delete invalid user in database
def get_invalid_id():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(User_id) FROM User_account")
        rows1 = cursor.fetchall()
        
        cursor.execute("SELECT MAX(id) FROM User_information")
        rows2 = cursor.fetchall()
        
        cursor.execute("SELECT MAX(id) FROM User_basics")
        rows3 = cursor.fetchall()
        
        cursor.execute("SELECT MAX(id) FROM User_interests")
        rows4 = cursor.fetchall()
        
        cursor.execute("SELECT MAX(id) FROM User_photo")
        rows5 = cursor.fetchall()

        return min(rows1[0][0], rows2[0][0], rows3[0][0], rows4[0][0], rows5[0][0]) + 1
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()

def delete_invalid_id():       
    invalid_id = get_invalid_id()  
    
    try:
        conn = connect()
        cursor = conn.cursor()
        #delete invalid user
        cursor.execute("DELETE FROM User_account WHERE User_id = %s", (invalid_id,))
        cursor.execute("DELETE FROM User_information WHERE id = %s", (invalid_id,))
        cursor.execute("DELETE FROM User_basics WHERE id = %s", (invalid_id,))
        cursor.execute("DELETE FROM User_interests WHERE id = %s", (invalid_id,)) 
        cursor.execute("DELETE FROM User_photo WHERE id = %s", (invalid_id,))
        cursor.execute("DELETE FROM User_match WHERE id = %s", (invalid_id,))
        
        #reset the id auto-increment
        cursor.execute("ALTER TABLE User_account AUTO_INCREMENT = %s", (invalid_id - 1,))
        cursor.execute("ALTER TABLE User_information AUTO_INCREMENT = %s", (invalid_id - 1,))
        cursor.execute("ALTER TABLE User_basics AUTO_INCREMENT = %s", (invalid_id - 1,))
        cursor.execute("ALTER TABLE User_interests AUTO_INCREMENT = %s", (invalid_id - 1,))
        cursor.execute("ALTER TABLE User_photo AUTO_INCREMENT = %s", (invalid_id - 1,))
        cursor.execute("ALTER TABLE User_match AUTO_INCREMENT = %s", (invalid_id - 1,))
 
        conn.commit()
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
        
#------------------------------------------------------------------------------------------------------
#ADMIN MODE

#get password with username
def get_password_w_username(username):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT Account_password FROM User_account WHERE Account_username = %s", (username,))
        rows = cursor.fetchall()
        
        return(rows[0][0])
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()

def delete_user(invalid_id):        
    
    try:
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT MAX(User_id) FROM User_account")
        row = cursor.fetchall()
        max_id = row[0][0]


        #delete invalid user
        cursor.execute("DELETE FROM User_account WHERE User_id = %s", (invalid_id,))
        cursor.execute("DELETE FROM User_information WHERE id = %s", (invalid_id,))
        cursor.execute("DELETE FROM User_basics WHERE id = %s", (invalid_id,))
        cursor.execute("DELETE FROM User_interests WHERE id = %s", (invalid_id,)) 
        cursor.execute("DELETE FROM User_photo WHERE id = %s", (invalid_id,))
        cursor.execute("DELETE FROM User_match WHERE id = %s", (invalid_id,))
        
        if invalid_id == max_id:
            #reset the id auto-increment
            cursor.execute("ALTER TABLE User_account AUTO_INCREMENT = %s", (invalid_id - 1,))
            cursor.execute("ALTER TABLE User_information AUTO_INCREMENT = %s", (invalid_id - 1,))
            cursor.execute("ALTER TABLE User_basics AUTO_INCREMENT = %s", (invalid_id - 1,))
            cursor.execute("ALTER TABLE User_interests AUTO_INCREMENT = %s", (invalid_id - 1,))
            cursor.execute("ALTER TABLE User_photo AUTO_INCREMENT = %s", (invalid_id - 1,))
            cursor.execute("ALTER TABLE User_match AUTO_INCREMENT = %s", (invalid_id - 1,))
 
        conn.commit()
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()