from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from api.serializers import ProductSerializer
from api.models import Product


class ProductListAPIView(APIView):
    serializer_class = ProductSerializer()
    def get(self,request,*args,**kwargs):
        products = Product.objects.all()
        serializer = self.serializer_class(products,many=True)
        return Response(serializer.data)
    
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer()
    @action(detail=True,method=["get"])
    def getAll(self,request,*args,**kwargs):
        products = Product.objects.all()
        serializer = self.serializer_class(products,many=True)
        return Response(serializer.data)