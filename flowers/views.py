from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Flower
from .serializers import FlowersSerializer
from .permissions import ISAuthorOrReadOnly

class FlowersList(ListCreateAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowersSerializer

class FlowersDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (ISAuthorOrReadOnly)
    queryset = Flower.objects.all()
    serializer_class = FlowersSerializer

