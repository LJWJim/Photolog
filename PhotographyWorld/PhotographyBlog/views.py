from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Photo, Theme, Author, Style

class IndexView(ListView):
    template_name = 'PhotographyBlog/index.html'
    context_object_name = 'photos'
    
    def get_queryset(self):
        return Photo.objects.order_by('-time')[:6]
        
    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['author'] = Author.objects.get(id='1')
        return context


class WorkView(IndexView):
    template_name = 'PhotographyBlog/work.html'
    
    def get_queryset(self):
        return Photo.objects.order_by('-time')
    
    '''def get_context_data(self, **kwargs):
        context = super(WorkView,self).get_context_data(**kwargs)
        context['theme'] = Theme.objects.get(name=Photo.theme)
        return context'''


class Work_detailView(DetailView):
    template_name = 'PhotographyBlog/work01.html'
    context_object_name = 'photo_detail'
    model = Photo
    pk_url_kwarg = 'id'
    
    def get_context_data(self, **kwargs):
        id = self.kwargs.get('id')
        context = super(Work_detailView,self).get_context_data(**kwargs)
        context['author'] = Author.objects.get(id='1')
        return context
'''def index(request):
    author = Author.objects.get(id='1')
    photos = Photo.objects.all()
    return render(request, 'PhotographyBlog/index.html', context={'author': author,'photos': photos})
    
    
def work(request):
    photos = Photo.objects.all()
    return render(request, 'PhotographyBlog/work.html', context={'photos': photos})
    
    
def work_detail(request, id):
    photo_detail = Photo.objects.get(id=id)
    return render(request, 'PhotographyBlog/work01.html', context={'photo_detail': photo_detail})
    '''
