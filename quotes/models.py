from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.CharField(max_length=300)
    time_stamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.author.username} - {self.quote[:50]}...'
    
    class Meta:
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'
    
