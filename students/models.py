from django.db import models
#Motverka fusk
class Students(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname + " " + self.lastname


