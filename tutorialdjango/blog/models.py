from django.db import models
from django.contrib.auth.models import User

# fonte única e definitiva de informações sobre os nossos dados (te os campos e 
# comportamentos essenciais dos dados que agente armazena. Cada model é uma classe 
# python que herda a classe model do Django

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
