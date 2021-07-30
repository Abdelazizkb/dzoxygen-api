
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author_id','id','size',"price",'description','city',"phone","datetime"]
