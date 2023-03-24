from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from blogs.models import Posts
from api.serializers import PostsSerializer


class BlogApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('posts')
        posts = Posts.objects.all()
        serializer_data = PostsSerializer(posts, many=True).data
        response = self.client.get(url)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

