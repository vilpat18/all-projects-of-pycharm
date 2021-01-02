from OneToOne.models import Creator,Page
from rest_framework.serializers import ModelSerializer

class CreatorSerialiser(ModelSerializer):
    class Meta:
        model = Creator
        fields = ('first_name','last_name')


class PageSerialiser(ModelSerializer):
    class Meta:
        model = Page
        fields = ('page_name','page_type','page_publish')