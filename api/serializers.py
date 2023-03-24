from rest_framework import serializers

from blogs.models import Posts, Comment, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'mail', 'text']


class PostsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Posts
        fields = ['id', 'image', 'title', 'category']


class PostsDetailSerializer(serializers.ModelSerializer):
    comments = CommentPostSerializer(many=True, read_only=True)
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Posts
        fields = ['image', 'title', 'description', 'category', 'comments']
