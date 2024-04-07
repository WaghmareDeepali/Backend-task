from django.urls import path
from Users.views import UserRegistrationView,UserDetailsView,ReferralsAPIView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(),
         name='register'),
     path('details/', UserDetailsView.as_view(), name='details'),
     path('referrals/', ReferralsAPIView.as_view(), name='referrals'),




]
