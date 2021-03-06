from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet,generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from cards.pagination import IdPagination
from .serializer import UserSerializer,UserCreateSerializer
from .permissions import IsOwner
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = IdPagination
    permission_classes = [IsOwner]

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self,request, *args, **kwargs):
        return super().list(request)

    @method_decorator(cache_page(60 * 60 * 2))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer

        return UserSerializer


class Logout(generics.DestroyAPIView):

    def destroy(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
