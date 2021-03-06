from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
import jwt


from .serializers import UserSerializer
User = get_user_model()


class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_with_same_email = User.objects.filter(email=request.data['email'])
            if user_with_same_email:
              return Response({'message': 'Email already exists'})
            serializer.save()
            return Response({'message': 'Registration successful'})

        return Response(serializer.errors, status=422)


class LoginView(APIView):

    def post(self, request):

        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid credentials'})

        if not user.check_password(password):
            raise PermissionDenied({'message': 'Invalid credentials'})

        #!Create Expiration:
        dt = datetime.now() + timedelta(hours=6)

        token = jwt.encode(
          #!payload:
            {
              'sub': user.id,
              'exp': int(dt.strftime('%s'))
            }, 
            settings.SECRET_KEY, 
            algorithm='HS256')


        return Response({'token': token, 'message': f'Welcome back {user.username}!'})

class CredentialsView(APIView):

    permission_classes = [IsAuthenticated,]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)