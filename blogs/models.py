from django.db import models



class Food(models.Model):

    CHOICES = {
        ("Pizza" , "pizza") ,
        ("Drink" , "drink") ,
        ("Sandwich" , "sandwich") ,
        ("Others" , "others") ,
    }

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='foods/')
    price = models.IntegerField()
    kind = models.CharField(choices=CHOICES)
    description = models.TextField(blank=True)

    def __str__(self):
        return  self.name
