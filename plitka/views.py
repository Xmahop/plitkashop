from django.shortcuts import render
from django.shortcuts import get_object_or_404
from plitka.models import Category, Item

def main(request):
    category_list = Category.objects.all()
    return render(request, 'plitka/index.html',context = {
                'category_list': category_list,
    })
def about(request):
    category_list = Category.objects.all()
    return render(request, 'plitka/about.html',context = {
                'category_list': category_list,
    })

def gallery(request):
    category_list = Category.objects.all()
    return render(request,'plitka/gallery.html',context = {
                'category_list': category_list,
    })
def category(request):
    category_list = Category.objects.all()

    return render(request,'plitka/production.html',context = {
                'category_list': category_list,
    })

def single_category(request,slug):
    get_category = get_object_or_404(Category, slug=slug)
    category = Category.objects.filter(name = get_category)
    category_list = Category.objects.all()
    item = Item.objects.filter(category = get_category)
    return render(request,'plitka/single_category.html',context = {
                'category': category,
                'get_category':get_category,
                'item':item,
                'category_list':category_list
    })