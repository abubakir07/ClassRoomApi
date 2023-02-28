from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from django.contrib.auth import get_user_model

from apps.users.serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer
                                    
from utils.permissions import IsUserOwner


User = get_user_model()

class UserApiViewSet(GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ['list']:
            return UserSerializer
        elif self.action in ['update']:
            return UserUpdateSerializer
        return UserCreateSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [AllowAny()]
        return [IsUserOwner()]
    