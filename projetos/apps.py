from django.apps import AppConfig
from django.contrib.auth import get_user_model




class ProjetosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projetos'

    def ready(self):
        import os

        User = get_user_model()

        email= os.getenv("EMAIL_ADMIN")
        senha = os.getenv("SENHA_ADMIN")
        

        usuarios = User.objects.filter(email=email)


        if not usuarios:
            User.objects.create_superuser(username='eu nao sei meu nome', email=email, password=senha, is_staff=True)

