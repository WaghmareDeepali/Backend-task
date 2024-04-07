from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from Users.serializers import UserDetailsSerializer,UserRegistrationSerializer
from django.contrib.auth import authenticate
from Users.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from Users.serializers import ReferralSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from Users.models import User

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        token = get_tokens_for_user(user)
        #return Response({ 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
        return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  


class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]  # Requires Authorization header with valid token
    
    def get(self, request, format=None):
        user = request.user  # Retrieve user from request
        serializer = UserDetailsSerializer(user)  # Serialize user details
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class ReferralsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # Get the current user
            user = request.user
            
            # Filter users who registered using the current user's referral_code
            referrals = User.objects.filter(referral_code=user.referral_code)
            
            # Paginate the list of referrals
            paginator = PageNumberPagination()
            paginator.page_size = 20  # Set the page size to 20 users per page
            paginated_referrals = paginator.paginate_queryset(referrals, request)
            
            # Serialize the paginated referrals data
            serializer = ReferralSerializer(paginated_referrals, many=True)

            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)