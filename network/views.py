from rest_framework import viewsets
from network.serializers import NetworkNodeSerializer
from network.models import NetworkNode
from users.permissions import IsActiveEmployee
from django_filters.rest_framework import DjangoFilterBackend


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["country"]

    def get_queryset(self):
        return NetworkNode.objects.select_related("supplier").prefetch_related("product")

