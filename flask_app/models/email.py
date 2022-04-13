from xml.dom.pulldom import default_bufsize
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Email:
    def __init__(self,data) -> None:
        self.email = data['email']
    @staticmethod
    def validate_email(email):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(email['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid
    
    @classmethod
    def add_email( cls, data):
        query="INSERT INTO emails (email,created_at,updated_at) VALUES (%(email)s, NOW(), NOW())"
        return connectToMySQL ("email_schema").query_db(query, data)
    
    @classmethod
    def get_email( cls ): 
        query= "SELECT * FROM emails"
        results = connectToMySQL('email_schema').query_db(query)
        emails = []
        for email in results :
            emails.append(cls(email))
        return emails
    