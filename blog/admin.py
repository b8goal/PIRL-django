from django.contrib import admin
# Register your models here.
from .models import Post
from .models import M1_Train_data

admin.site.register(Post)
admin.site.register(M1_Train_data)