from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

def custome_login(request, username, password):
	user = authenticate(request, username=username, password=password)

	if user is not None:
		login(request, user)
		
		if Token.objects.filter(user=user).exists():
			token = Token.objects.get(user=user)
		else:
			token = Token.objects.create(user = user)

		login_obj = {'token': token.key, 'user': user}
		return login_obj
	else:
		return False
