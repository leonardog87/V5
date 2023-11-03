from django.db import models
from django.contrib.auth.models import User
  
class Blog(models.Model):
    imagen=models.ImageField(upload_to="blog")
    titulofoto=models.CharField(max_length=30)
    titulomessage=models.CharField(max_length=30)
    message=models.TextField(null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.titulofoto}"

class Mensaje(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    blog=models.ForeignKey(Blog, related_name='mensajes', on_delete=models.CASCADE, null=True)
    message=models.TextField(null=True, blank=True)    
    def __str__(self):
        return f"{self.message} - {self.blog}"
    
class MensajeUser(models.Model):
    user_transmitter=models.ForeignKey(User, related_name='emisor', on_delete=models.CASCADE, null=True, blank=True)
    user=models.ForeignKey(User, related_name='receptor',on_delete=models.CASCADE, null=True, blank=True)
    message=models.TextField(null=True, blank=False)
    fecha=models.DateField(auto_now_add=True)
    hora=models.TimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user_transmitter, self.message}"


    


 