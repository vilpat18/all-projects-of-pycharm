from nestapp.models import Author , Book
from rest_framework.serializers import ModelSerializer

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(ModelSerializer):
    books_by_author = BookSerializer(many=True,read_only=True)
    class Meta:
        model = Author
        fields = '__all__'

