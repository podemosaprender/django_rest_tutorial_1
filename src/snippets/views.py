#VER: https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import renderers

from django.contrib.auth.models import User
from .models import Snippet
from .serializers import UserSerializer, SnippetSerializer
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    #VER: https://www.django-rest-framework.org/api-guide/renderers/
    #OjO! solo funciona sin parametro format o con format=html
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def highlight(self, request, *args, **kwargs):
        try:
            snippet = self.get_object()
            return Response(snippet.highlighted)
        except Exception as ex:
            print(ex)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
