from __future__ import unicode_literals
from django.db import models


class user(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "user object: ---,{} ----{}, ----{}".format(self.firstname, self.lastname, self.email)