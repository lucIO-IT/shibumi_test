from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .config.serializers import TodoSerializer
from .models import Todo

# Create your views here.


class TodoListAPIView(ListCreateAPIView):

    model = Todo
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)
