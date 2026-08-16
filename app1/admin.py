from django.contrib import admin

# Register your models here.
from .models import Book, Church, MortgagePool
#resgister book model
admin.site.register(Book)
admin.site.register(Church)
admin.site.register(MortgagePool)
