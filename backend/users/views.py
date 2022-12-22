from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from .serializers import SignUpSerializer, LoginSerializer, UserSerializer, TokenSerializer

class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    'user': UserSerializer(user).data, 
                    'token': token.key}, 
                    status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
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
        
class TokenView(APIView):
    def get(self, request):
        key = request.headers.get('Authorization')
        if key is None:
            return Response({'error': 'Authentication is null'}, status=status.HTTP_400_BAD_REQUEST)
        user = CustomUser.objects.get_user_from_token(key=key)
        return Response({
            'user': UserSerializer(user).data},
            status=status.HTTP_200_OK)



        # serializer = TokenSerializer(data=request.headers)
        # if serializer.is_valid():
        #     key = serializer.validated_data['key']
        #     print(key)
        #     token = Token.objects.get(key=key)
        #     user = token.user
        #     return Response({
        #         'user': UserSerializer(user).data},
        #         status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        