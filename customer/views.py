from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Customer
from .serializers import CustomerSerializer

#class CustomerList(generics.ListAPIView):
#    queryset = Customer.objects.all()
#    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

@api_view(['GET', 'POST'])
def CustomerList(request):
    serializer_class = CustomerSerializer
    if request.method == 'GET':
        customer = Customer.objects.all()
        customer = CustomerSerializer(customer, many=True)
        return Response(customer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
