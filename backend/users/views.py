from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SignUpSerializer, LoginSerializer, UserSerializer

class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    'user': UserSerializer(user, context=self.get_serializer_context()).data, 
                    'token': token.key}, 
                    status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        print(request.data)
        # serializer = LoginSerializer(data=request.data)
        
        # if serializer.is_valid():
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user).data, 
            'token': token.key}, 
            status=status.HTTP_200_OK)
        
        