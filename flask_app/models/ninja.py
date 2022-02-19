from winreg import QueryInfoKey
from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __int__(self,db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.dojo_id = db_data
    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age ) VALUES (%(dojo_id)s,%(first_name)s, %(last_name)s, %(age)s);"

        return connectToMySQL('dojo_ninjas').query_db(query, data)

    @classmethod
    def get_ninjas(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s"
        return connectToMySQL('dojo_ninjas').query_db(query,data)