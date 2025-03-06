from django.db import models

# Create your models here.
class TaskManager(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('COMPLETED','Completed')
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, default='pending',max_length=20)

    def __str__(self):
        return self.title
    