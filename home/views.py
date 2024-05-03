from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from home.models import *
from django_filters import rest_framework as filter
from rest_framework.serializers import ModelSerializer
from rest_framework.generics import RetrieveAPIView



class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'



class BookFilter(filter.FilterSet):
    author_name = filter.CharFilter(field_name='author__name', lookup_expr='icontains')
    name = filter.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['author_name', 'name']


class OrderFilter(filter.FilterSet):
    client_phone = filter.CharFilter(field_name='client__phone', lookup_expr='icontains')
    product = filter.CharFilter(field_name='product__name', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = ['client_phone', 'product']


class AboutView(APIView):
    def get(self, req: Request):
        return Response({'data': About.objects.all().values()})
    
class CatView(APIView):
    def get(self, req: Request):
        return Response({'data': Category.objects.all().values()})
    

class BookList(APIView):
    
    def get(self, req: Request, format=None):
        queryset = Book.objects.all()

        filter_backends = [filter.DjangoFilterBackend]
        filterset = BookFilter(req.query_params ,queryset=queryset)
        queryset = filterset.qs


        books = BookSerializer(queryset, many=True)
   
        return Response({'data': books.data})
    

class BookDetail(RetrieveAPIView):
    queryset = Book
    serializer_class = BookSerializer



class OrderCreateList(APIView):
    def post(self, req: Request):
        ...
    
    def get(self, req: Request, format=None):
        queryset = Order.objects.all()

        filter_backends = [filter.DjangoFilterBackend]
        filterset = OrderFilter(req.query_params ,queryset=queryset)
        queryset = filterset.qs


        books = OrderSerializer(queryset, many=True)
   
        return Response({'data': books.data})
    

class OrderDetail(RetrieveAPIView):
    queryset = Order
    serializer_class = OrderSerializer