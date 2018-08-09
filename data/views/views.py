from rest_framework import serializers, generics
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.decorators import api_view
from data.filter import IsOwnerFilterBackend
   
from data.models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id', 'user', 'rpm', 'speed', 'created_on', 'updated_on')

class DataList(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    filter_backends = (IsOwnerFilterBackend,)

class DataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    filter_backends = (IsOwnerFilterBackend,)

# @list_route(methods=["GET","POST" ])
# def hello_world(request):
#     # import pdb
#     # pdb.set_trace()

#     def post(self, request, format=None):
#         return Response({'received data': request.data})


