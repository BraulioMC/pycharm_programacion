import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                user='root',
                password='abc123.',
                db='daw',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)

def registerUser(user, password):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `user`, `password` FROM `login` WHERE `user` = %s and `password` = %s"
            cursor.execute(sql, (user, password))
            result = cursor.fetchone()

            if not result:
                # Create a new record
                sql = "INSERT INTO `login` (`user`, `password`) VALUES (%s, %s)"
                cursor.execute(sql, (user, password))
                
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()
                return True
            
            else:
                return False

    except:
        return False

def loginDB(user, password):
    try:
        connection

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `user`, `password` FROM `login` WHERE `user`=%s"
            cursor.execute(sql, (user,))
            result = cursor.fetchone()

            if not result:
                return False
            elif (result['password'] == password and result['user'] == user):
                return True


    finally:
        pass

def closeDB():
    connection.close()