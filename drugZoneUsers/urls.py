from django.conf.urls import include, url
from django.contrib import admin
from .views import *
from . import views


urlpatterns = [
	# url(r'^auth/', include('rest_auth.urls')),
	url(r'^signup/$', UserProfile.as_view()),
	url(r'^get-profile/$', ProfileAPIView.as_view()),
	url(r'^update-profile/$', ProfileAPIView.as_view()),

	url(r'^change-password/$', ChangePassword.as_view()),
	url(r'^login/$', UserLogin.as_view()),
	url(r'^contactus/$', UserContactUs.as_view()),
	url(r'^otpverify/$', OtpVerify.as_view()),
	url(r'^logout/$', UserLogoutView.as_view()),
	url(r'^check/$', UserSessionView.as_view()),
	
	
]
