from django.db import models

# Create your models here.
class User(models.Model):
  age = models.IntegerField()
  name = models.CharField(max_length=100)

  # String representation of the User model through __str__ method with name field
  # The self parameter refers to the current instance of the User model
  # and the __str__ is the name of the method that return a string representation of the object.
  def __str__(self):
    return self.name