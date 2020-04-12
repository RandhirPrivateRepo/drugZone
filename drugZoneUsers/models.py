from django.db import models

# Create your models here.
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
# from .managers import UserManager
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.conf import settings


DEVICE_TYPE = (
        ('I', 'IOS'),
        ('A', 'ANDROID'),
    )

ROLE_TYPE= (
		('1', 'Sub-Admin'),
        ('2', 'Lab-Admin'))

class UserManager(BaseUserManager):
	use_in_migrations = True

	def create_user(self,email,password):
		user = self.model(email = self.normalize_email(email))
		user.username = email
		user.set_password(password)
		user.is_active = True
		user.save()
		return user


	def create_superuser(self,username,email,password):
		user = self.create_user(email = email,password = password)
		user.is_staff = True
		user.is_superuser = True
		user.save()
		return user



class CustomUser(AbstractUser):
	name = models.CharField(max_length = 100, null = True, blank = True)
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length = 100, null = True, blank = True)
	role = models.CharField(max_length = 2, choices = ROLE_TYPE, null = True, blank = True)
	profileImage = models.ImageField(upload_to= "media/uploads/",null = True, blank = True ,verbose_name='Profile Image')
	deviceToken = models.CharField(max_length = 255, null = True, blank = True)
	deviceType = models.CharField(max_length = 2, choices = DEVICE_TYPE, null = True, blank = True)
	otpVerified = models.BooleanField(default=False)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	

	objects = UserManager()
	
	def __str__(self):
		return str(self.email)

	class Meta:
		verbose_name_plural = "Users"

	REQUIRED_FIELDS = ['email']

	@receiver(post_save,sender = settings.AUTH_USER_MODEL)
	def create_auth_token(sender,instance = None, created = False,**kwargs):
		if created:
			Token.objects.create(user = instance)


class ContactUs(models.Model):
	user = models.ForeignKey('CustomUser',on_delete = models.CASCADE,null = True,blank =True)
	email = models.EmailField()
	message = models.TextField()

	class Meta:
		verbose_name_plural = "Contact Us"