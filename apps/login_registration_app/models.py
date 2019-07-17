from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def register_validation(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors["first_name"] = "Fisrt name should be at least 2 caracters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name shoud be at least 2 caracter"
        if not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at leasr 8 character"
        if postData['password'] != postData["confirm_password"]:
            errors["confirm_password"] = "password and Condirm PW shoud match"
        return errors

    def login_validation(self, postData):
        errors = {}
        try:
            user = User.objects.get(email=postData["email"])
        except:
            errors["email"] = "Not matching out database" 
            if not bcrypt.checkpw(postData["password"].encode(), user.password):
                errors["password"] = "Not matching our Database"
        return errors

    

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.TextField(max_length=255)
    objects = UserManager()

    def __repr__(self):
        return f"<User object: {self.first_name} ({self.id})"