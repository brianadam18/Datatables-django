from django.contrib import admin
from App.models import Item

class ItemAdmin(admin.ModelAdmin) :
    list_display = ['no_barang','nama_barang', 'no_sku', 'ukuran', 'jumlah_barang', 'Jenis_barang','create_at']
    list_per_page = 8
    search_fields = ['nama_barang','no_sku',]
    
admin.site.register(Item, ItemAdmin)