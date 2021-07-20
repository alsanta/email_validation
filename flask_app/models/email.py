from flask.helpers import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re

class Email():

    def __init__(self,data):
        self.id = data['id']
        self.address = data['address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_email(cls,data):
        query = 'INSERT INTO email (address) VALUES (%(address)s)'

        results = connectToMySQL('emails').query_db(query,data)
    
        return results

    @classmethod
    def get_all_emails(cls):
        query = 'SELECT * FROM email'

        results = connectToMySQL('emails').query_db(query)

        email_list =[]
        for x in results:
            email_list.append(x)
        
        return email_list

    @classmethod
    def delete(cls,data):
        query = 'DELETE FROM email Where id = %(id)s'

        result = connectToMySQL('emails').query_db(query,data)

        return result

    @staticmethod
    def validate_email(user):
        all_emails = Email.get_all_emails()
        email_regex = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
        is_valid = True

        if not email_regex.match(user['address']):
            flash('Please insert a valid email. Ex.. username@somedomain.com')
            is_valid = False
        return is_valid