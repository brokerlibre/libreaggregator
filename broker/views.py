from rest_framework import generics
                                                                                
from .models import Broker
from .serializers import BrokerSerializer                                     
                                                                                
                                                                                
class BrokerList(generics.ListAPIView):                                       
    queryset = Broker.objects.all()                                           
    serializer_class = BrokerSerializer                                       
                                                                                
                                                                                
class BrokerDetail(generics.RetrieveUpdateDestroyAPIView):                    
    queryset = Broker.objects.all()                                           
    serializer_class = BrokerSerializer   
