from django.db import models
from datetime import datetime

# Create your models here.

class Posts(models.Model):
    
    """
        Depois de criar o modelo, basta digitar no terminal: [ python manage.py makemigrations nome_modulo (E.: posts) ]
        Assim, é criado na pasta de migrations um esquema de ano de dados, facilitando na criação da taela do banco,
        após isso, no terminal digitar: python manage.py migrate, e então é criado no banco de dados a tabela seguindo
        especificação do modelo.

        Isso facilita pois não é preciso uma classe PDO por exemplo e nem trabalho manual de criação e configuração
        na base de dados
    """

    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    # para fixar na lista retornada de dados, o titulo iniccial
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural = "Posts" # Isso evita o nome com o 's' no final do admin do django
