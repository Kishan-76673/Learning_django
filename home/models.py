from django.db import models

# Create your models here.

# Models in Django are Python classes that define the structure of your database tables. Each model class corresponds to a database table, and each attribute of the class represents a field in that table.

class student(models.Model):
    id = models.AutoField(primary_key=True) # Auto-incrementing primary key field, this field is optional as Django automatically adds an id field if not specified
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    address = models.TextField()
    image = models.ImageField()
    file = models.FileField()

    def __str__(self):
        return self.name   


# After defining models, you typically run migrations to create the corresponding database tables.
# Commands: python manage.py makemigrations
#           python manage.py migrate

