from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import random
import string

# Create your models here.
from django.core.validators import RegexValidator

from django.contrib.auth.models import (
		BaseUserManager, AbstractBaseUser
	)


u_id = ''.join(random.choice((string.ascii_letters).upper() + string.digits) for _ in range(6))


class MyUserManager(BaseUserManager):
	def create_user(self, email, number,refercode, password=None):
		if not number:
			raise ValueError('Users must have an mobile number')

		user = self.model(
					email = self.normalize_email(email),
					number = number,
                    refercode = refercode,
				)
		user.set_password(password)
		user.save(using=self._db)
		return user
		# user.password = password # bad - do not do this

	def create_superuser(self, email,number,refercode, password=None):
		user = self.create_user(
				 email, number,refercode,password=password
			)
		user.is_admin = True
		user.is_staff = True
		user.save(using=self._db)
		return user



class MyUser(AbstractBaseUser):
	username = models.CharField(unique=True, default=u_id, max_length=6)
	email = models.EmailField(
			max_length=255,
			unique=True,
			verbose_name='email address'
		)

	number = models.CharField(max_length=100,unique=True,primary_key=True)

	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	refercode = models.CharField(max_length =30,default ='',)

	objects = MyUserManager()

	USERNAME_FIELD = 'number'
	REQUIRED_FIELDS = ['email','refercode']

	def __str__(self):
		return self.email

	def get_short_name(self):
		# The user is identified by their email address
		return self.email


	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)




