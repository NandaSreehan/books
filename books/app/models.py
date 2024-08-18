from django.db import models


class autermodel(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    rating=models.IntegerField()
    def __str__(self):
        return self.name

class booksmodel(models.Model):
    title=models.CharField(max_length=50)
    price=models.IntegerField()
    genre=models.CharField(max_length=50)
    author=models.ForeignKey('autermodel',on_delete=models.CASCADE)
    img=models.ImageField(upload_to='media',null=True)
    def __str__(self):
        return self.title

