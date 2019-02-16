from rest_framework import generics
                                                                                
from .models import Insurer
from .serializers import InsurerSerializer                                     
                                                                                
                                                                                
class InsurerList(generics.ListAPIView):                                       
    queryset = Insurer.objects.all()                                           
    serializer_class = InsurerSerializer                                       
                                                                                
                                                                                
class InsurerDetail(generics.RetrieveUpdateDestroyAPIView):                    
    queryset = Insurer.objects.all()                                           
    serializer_class = InsurerSerializer   
