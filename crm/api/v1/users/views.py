from rest_framework import viewsets, permissions, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser
from oauth2_provider.models import Application
from rest_framework.decorators import action
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from django.conf import settings
from crm.models.user import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, JSONParser]

    def get_permissions(self):
        if self.action in ['get_current_user', 'change_password']:
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], detail=False, url_path="current-user")
    def get_current_user(self, request):
        return Response(self.serializer_class(request.user, context={"request": request}).data,
                        status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path="change-password")
    def change_password(self, request):
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        account = request.user

        if old_password is not None and new_password is not None and old_password != new_password:
            if not account.check_password(old_password):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            account.set_password(new_password)
            account.save()
            response = {
                'status': 'success',
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response, status=status.HTTP_200_OK)

        return Response({"Message": ["Errors."]}, status=status.HTTP_400_BAD_REQUEST)

class AuthInfo(APIView):
    def get(self, request):
        return Response(settings.OAUTH2_INFO_BASIC, status=status.HTTP_200_OK)