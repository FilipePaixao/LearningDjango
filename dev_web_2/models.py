from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    ## Comando para criar um migration  python manage.py makemigrations dev_web_2
    ## Depois usar o comando python manage.py migrate         
    
    # 1
    ## Comandos para visualizar conteudo da tabela Students
    # psql -U root -d pwpessoas
    
   # 2
    #SELECT table_name
    #FROM information_schema.tables
    #WHERE table_schema = 'public'
    # AND table_type = 'BASE TABLE';
    
    # 3
    # SELECT * FROM django_content_type;
    
    #4
    # SELECT * FROM dev_web_2_students
    