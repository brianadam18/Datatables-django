from django.contrib import admin
from django.urls import path
from App import views   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    # Path to ADD Item
    path('add_item', views.add_item, name='add_item'),
    # Path to View Item
    path('edit/<str:no_barang>', views.item, name='item'),
    # Path to Edit Item
    path('edit_item', views.edit_item, name='edit_item'),
    # Path to Delete Item
    path('delete_item/<str:no_barang>', views.delete_item, name='delete_item'),
]
