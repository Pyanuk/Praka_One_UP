from django.contrib import admin
from django.urls import path
from Home.views import home, company, contacts, map, products, category, full, basket

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('index.html', home),
    path('company.html', company),
    path('contacts.html', contacts),
    path('map.html', map),
    path('products.html', products),
    path('category.html', category),
    path('fullproducts.html', full),
    path('basket.html', basket),
]
