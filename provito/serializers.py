from .models import *
from rest_framework import serializers


class BoardSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Board
       fields = ['id', 'title', ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Category
       fields = ['id', 'name', ]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Comment
       fields = ['id', 'text', ]