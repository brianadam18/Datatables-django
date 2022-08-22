from django.shortcuts import render
from App.models import Item
from django.http import HttpResponseRedirect
from django.contrib import messages

# Function to render Homepage


def home(request):
    item_list = Item.objects.all()
    return render(request, 'home.html', {"items": item_list})

# Function to ADD Item


def add_item(request):
    if request.method == "POST":
        if request.POST.get('nama_barang') \
                and request.POST.get('no_sku') \
                and request.POST.get('ukuran') \
                and request.POST.get('jumlah_barang') \
                and request.POST.get('Jenis_barang') \
                or request.POST.get('note'):
            item = Item()
            item.nama_barang = request.POST.get('nama_barang')
            item.no_sku = request.POST.get('no_sku')
            item.ukuran = request.POST.get('ukuran')
            item.jumlah_barang = request.POST.get('jumlah_barang')
            item.Jenis_barang = request.POST.get('Jenis_barang')
            item.note = request.POST.get('note')
            item.save()
            messages.success(request, 'Item added successfully')
            return HttpResponseRedirect('/')
    else:
        return render(request, 'add.html')

# Function to View Item


def item(request, item_id):
    item = Item.objects.get(id=item_id)
    if item != None:
        return render(request, 'edit.html', {'item': item})

# Function to Edit Item


def edit_item(request):
    if request.method == "POST":
        item = Item.objects.get(id=request.POST.get('id'))
        if item != None:
            item.nama_barang = request.POST.get('nama_barang')
            item.no_sku = request.POST.get('no_sku')
            item.ukuran = request.POST.get('ukuran')
            item.jumlah_barang = request.POST.get('jumlah_barang')
            item.Jenis_barang = request.POST.get('jenis_barang')
            item.save()
            messages.success(request, 'Item updated successfully')
            return HttpResponseRedirect('/')

# Function to Delete Item


def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if item != None:
        item.delete()
        messages.success(request, 'Item deleted successfully')
        return HttpResponseRedirect('/')
