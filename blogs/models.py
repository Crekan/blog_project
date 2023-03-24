from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Posts(models.Model):
    image = models.ImageField(upload_to='posts/', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class Comment(models.Model):
    name = models.CharField(max_length=250, null=True)
    mail = models.EmailField(null=True)
    text = models.TextField(null=True)
    data_add = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.name} - {self.text}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
