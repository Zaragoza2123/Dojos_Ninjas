from winreg import QueryInfoKey
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']

        self.dojos = []

    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL('dojo_ninjas').query_db(query, data)

    @classmethod 
    def get_dojo_and_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(dojo_id)s"
        results = connectToMySQL('dojo_ninjas').query_db(query, data)
        return results
    @classmethod
    def get_dojos(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('dojo_ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
