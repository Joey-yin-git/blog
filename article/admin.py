from django.contrib import admin
from article.models import Article
# Register your models here.
admin.site.register(Article)

Article.objects.create(title = 'Hello World', category = 'Python', content = 'Let us add a database item')

Article.objects.create(title = 'Django Blog Studying', category = 'Python', content = 'Django Blog Tutorial')
