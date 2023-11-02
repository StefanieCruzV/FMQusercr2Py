# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email= data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"

        results = connectToMySQL('usersHw').query_db(query)
        # guarda el resultado de la bd
        
        users = []
        # crea arreglo para guiardar los valores 
        for user in results: #itera los nombres de la base de datos 
            users.append(cls(user))
            # flos mete en el arreglo -y los convierte en una clkase ususario
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(uname)s , %(ulastname)s , %(uemail)s , NOW() , NOW() );"
        # los nombres deben ser los de la bd / los valores los del html
        return connectToMySQL('usersHw').query_db(query, data)
