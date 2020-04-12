from django.shortcuts import render

# Create your views here.
from .serializers import * 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import DatabaseError, transaction
import traceback
from .models import *
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import traceback
from .utils import *



class UserProfile(APIView):
	permission_classes = ()
	
	def post(self, request):
		data = request.data
		
		if CustomUser.objects.filter(email = data.get('email')).exists():
			return Response({'Error': "user with this email already exists"}, status = status.HTTP_400_BAD_REQUEST)

		if 'password' not in data:
			return Response({'Error': "please provide password"}, status = status.HTTP_400_BAD_REQUEST)

		if 'email' not in data:
			return Response({'Error': "please provide email"}, status = status.HTTP_400_BAD_REQUEST)


		try:
			with transaction.atomic():
				user = CustomUser.objects.create_user(
					email = data.get('email', None),
					password = data.get('password', None))

				user.name = data.get('name', None)
				user.profileImage = data.get('profileImage', None)
				user.deviceToken = data.get('deviceToken', None)
				user.phone = data.get('phone', None)
				user.deviceType = data.get('deviceType', None)
				# user.role = 3
				user.save()
				

				serialized = CustomUserSerializer(user)
				
				token_obj = Token.objects.get(user = user)
				response = {'key': token_obj.key}

				return Response(response, status = status.HTTP_201_CREATED)
		except Exception as e:
			traceback.print_exc()
			return Response({'Error': str(e)}, status = status.HTTP_400_BAD_REQUEST)



class ProfileAPIView(APIView):

	def get(self,request):
		user = request.user
		try:
			serialized = UserProfileSerializer(user, context = {'request': request})
			return Response(serialized.data,status=status.HTTP_200_OK)
		except Exception as e:
			return Response({"Error":str(e)},status=status.HTTP_400_BAD_REQUEST)

	def put(self,request):
		user = request.user
		data = request.data
		
		try:
			Obj = get_object_or_404(CustomUser, id = user.id)
			Obj.name = data.get('name')
			Obj.phone = data.get('phone')
			Obj.profileImage = data.get('profileImage')
			Obj.save()
			
			return Response({"success": 'Profile updated successfully.'}, status=status.HTTP_200_OK)

		except Exception as e:
			traceback.print_exc()
			return Response({'Error':str(e)}, status = status.HTTP_400_BAD_REQUEST)
		


class UserLogin(APIView):
	permission_classes = ()
	
	def post(self, request):
		try:
			data = request.data
			if 'email' not in data or 'password' not in data:
				return Response({'Error': "Please provide Email and Password"}, status = status.HTTP_400_BAD_REQUEST)
			email = data.get('email')
			password = data.get('password')

			deviceType = data.get('deviceType')
			deviceToken = data.get('deviceToken')
			if CustomUser.objects.filter(email = email).exists():
				user = CustomUser.objects.get(email = email)
				user.deviceType = deviceType
				user.deviceToken = deviceToken
				user.save()
			if custome_login(request, email, password):
				login_obj = custome_login(request, email, password)
				return Response({'key': login_obj['token']}, status = status.HTTP_200_OK)
			else:
				return Response({'Error': "Invalid Credentials"}, status = status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			traceback.print_exc()
			return Response({'Error': str(e)}, status = status.HTTP_400_BAD_REQUEST)


class ChangePassword(APIView):
	
	def put (self, request):
		data = request.data
		user = request.user

		if not data.get('old_password'):
			return Response({'Error': "Please provide old password"}, status = status.HTTP_400_BAD_REQUEST)

		if not data.get('new_password'):
			return Response({"Error": "Please Provide new  password"}, status = status.HTTP_400_BAD_REQUEST)

		if not user.check_password(data.get('old_password')):
			return Response({'Error': " Old Password not matched"}, status = status.HTTP_409_CONFLICT)

		else:
			user.set_password(data.get('new_password'))
			user.save()
			return Response({"Success": "Password has been changed"}, status = status.HTTP_200_OK)


class UserContactUs(APIView):

	def post(self,request):
		user = request.user
		data = request.data

		Obj = ContactUs.objects.create(user = user,
		email = data.get('email'),
		message = data.get('message'))

		return Response({"Success": "Response saved"}, status = status.HTTP_200_OK)


class OtpVerify(APIView):

	def get(self,request):
		user = request.user
		
		if CustomUser.objects.filter(id = user.id).exists():
			Obj = CustomUser.objects.get(id = user.id)
			if Obj.otpVerified == False:
				Obj.otpVerified = True
				Obj.save()
			else:
				return Response({"Success": "OTP Already Verified"}, status = status.HTTP_200_OK)
			return Response({"Success": "OTP Verified"}, status = status.HTTP_200_OK)
		else:
			return Response({"Error": "User not exists"}, status = status.HTTP_400_BAD_REQUEST)

	

class UserLogoutView(APIView):

	def post(self,request):
		user = request.user

		try:
			if Token.objects.filter(user = user).exists():
				token_obj = Token.objects.get(user = user)
				token_obj.delete()
			response = {"success":"Successfully logged out."}
			return Response(response , status = 200)
		except Exception as e:
			traceback.print_exc()
			return Response({'Error': str(e)}, status = status.HTTP_400_BAD_REQUEST)


class UserSessionView(APIView):

	def get(self,request):
		user = request.user
		try:
			if Token.objects.filter(user = user).exists():
				return Response({"detail":"Active"} , status = 200)
			else:
				return Response({"detail":"In-Active"} , status = 200)
		except Exception as e:
			traceback.print_exc()
			return Response({'Error': str(e)}, status = status.HTTP_400_BAD_REQUEST)



# class PasswordUpdateAPIView(APIView):
#     permission_classes = ()
#     def put(self,request):

# 		data = request.data
# 		if data.has_key('email'): 
# 			if not data.get('email'):
# 				return Response({"Error": "Please provide a valid email"}, status = status.HTTP_400_BAD_REQUEST)
# 		if not data.get("password"):
# 			return Response({'Error': "Please provide password"}, status = status.HTTP_400_BAD_REQUEST)

# 		try:
# 			if data.has_key('email'):
# 				user_obj = CustomUser.objects.get(email = data.get('email'))
# 				user_obj.set_password(data.get('password'))
# 				user_obj.save()
# 			return Response({"Sucess" :"Password is changed"},status=status.HTTP_200_OK)
		
# 		except CustomUser.DoesNotExist:
# 			traceback.print_exc()
# 			return Response({'Error': "No any user found with this email"}, status = status.HTTP_400_BAD_REQUEST)



# class ForgotPasswordAPIView(APIView):
#     permission_classes=[]
#     def post(self,request):
# 		try:
# 			data=request.data
# 			if not data.has_key('email'):
# 				return Response({"Error": "Please provide Email"})
# 			user = get_object_or_404(CustomUser, email = data.get('email'))
# 			# link = generate_forgotpassword_link(data.get('email', None))
# 			frgt_pass_obj = ForgotPasswordLink.objects.create(
# 			user = user,
# 			link = link)
# 			frgt_pass_obj.save()
			
# 			#send mail
# 			ctx={

# 			'dynamicLink': link,

# 			}
# 			subject = "Reset Password"
# 			message = get_template('send_dynamic_link.html').render(ctx)
# 			msg = EmailMessage(subject, message, to=[data.get('email',None)], from_email=settings.EMAIL_HOST_USER)
# 			msg.content_subtype = 'html'
# 			msg.send()

# 			response={"Success":"Email has been sent"}
# 			return Response(response , status = status.HTTP_200_OK)
# 		except Exception as e:
# 			traceback.print_exc(e)
# 			response = {"Error": str(e)}
# 			return Response(response ,status = status.HTTP_400_BAD_REQUEST)
