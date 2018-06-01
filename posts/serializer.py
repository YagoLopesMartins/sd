from rest_framework import serializers
from .models import Posts

"""
    Classe criada para realizar o envio do modelo pela aruitetura de redes como serial...
"""

class PostsSerializer(serializers.ModelSerializer):
    
    # é possível enviar todos os dados como serializado
    class Meta:
        model = Posts
        depth = 1 # profundidade para exiir os dados
        fields = ['id','title','body','created_at']