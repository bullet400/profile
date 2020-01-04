from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    title =models.CharField(max_length=50)
    pub_date=models.DateTimeField()
    body =models.TextField()
    url =models.TextField()
    image =models.ImageField(upload_to='images/')
    icon=models.ImageField(upload_to='images/')
    vote_total=models.IntegerField(default=1)
    hunter =models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def home_body(self):
        return self.body[:150]


    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e ,%Y')
