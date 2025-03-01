from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import arrr
from .serializers import ArrrSerializer

class ArrrViewSet(viewsets.ModelViewSet):
    queryset = arrr.objects.all()
    serializer_class = ArrrSerializer

    @action(detail=False, methods=['get'])
    def get_data(self, request):
        """Получить данные"""
        arrs = self.get_queryset()
        serializer = self.get_serializer(arrs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def write_data(self, request):
        """Записать данные"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)