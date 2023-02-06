from django.db import models

class Author(models.Model):
    author = models.CharField(max_length=70,blank=True,null=True)
    added_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.author


class Book(models.Model):
    book = models.CharField(max_length=200,blank=True,null=True)
    added_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

