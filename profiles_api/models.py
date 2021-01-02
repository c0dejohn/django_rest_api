# para hacer login con e-amil
from django.contrib.auth.models  import (AbstractBaseUser, BaseUserManager,
                                        PermissionMixin)
from django.db import models


class UserProfileManager(BaseUserManager):
    ''' Manager para perfiles de usuario'''

    def create_user(self, email, name, password=None):
        ''' Crear nuevo user profile'''
        if not email:
            raise ValueError('Usuario debe tener un email')
        # definiendo objetos
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        # usuario necesita un password
        user.set_password(password)
        # para poder guargar nuestro usuario
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionMixin):
    """modelo BD para usuarios en el sistema """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # necesario para django para que sepa como agregar y crear ususarios
    objects = UserProfileManager()

    # campo de login que el usuario especificará
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']

    def get_full_name(self):
        ''' 'Obtener nombre completo'''
        return self.name

    def get_short_name(self):
        '''obtener nombre corto'''
        return self.name

    def __str__(self):
        ''' Retornar cadena representanto nuestro usuario'''
        return self.email
