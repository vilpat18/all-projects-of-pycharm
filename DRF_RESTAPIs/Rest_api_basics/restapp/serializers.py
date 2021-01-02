from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['url','id','user','title','content','timestamp']
        # read_only_fields = ['user']

    # def get_url(self,obj):
    #     return obj.get_api_url()