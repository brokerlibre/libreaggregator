from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from .models import Customer
from .models import Sale
from .models import Broker

from .serializers import SaleSerializer


#class SaleList(generics.ListAPIView):
#    queryset = Sale.objects.all()
#    serializer_class = SaleSerializer


class SaleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


@api_view(['GET', 'POST'])
def SaleList(request):
    serializer_class = SaleSerializer
    if request.method == 'GET':
        sale = Sale.objects.all()
        sale = SaleSerializer(sale, many=True)
        return Response(sale.data)

    elif request.method == 'POST':
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

