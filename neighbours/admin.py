from django.contrib import admin
from .models import Neighbourhood, Person, Business, Post

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Person)
admin.site.register(Business)
admin.site.register(Post)
