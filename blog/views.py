from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from . forms import *
from django.contrib.auth import get_user_model
from . models import *
from authentication.forms import *
from django.forms import formset_factory
from django.db.models import Q
from itertools import chain
from django.core.paginator import Paginator

@login_required
def home(request):
        user = request.user
        print(f'users is : {user}')
        followed_users = request.user.follows.all()
        print(f'les utilisateurs suivis sont :{followed_users}')
        blogs = Blog.objects.filter(
                contributors__in=followed_users
        )
        print(f'Voici les instances blog récupérées : {blogs}')
        blogs_id=blogs.values_list('id', flat=True)
        uploader = request.user.follows.all()
        print(f'Voici les utilisateurs qui ont télversés des images : {uploader}')
        Photos = Photo.objects.filter(
                uploader__in=request.user.follows.all()
        ).exclude(blog__id__in=blogs_id)

        blogs_and_photos = sorted(
                chain(blogs, Photos),
                key = lambda instance:instance.date_created,
                reverse = True
        )
        print(f'Voici les données passées au gabarit: {blogs_and_photos}')

        paginator = Paginator(blogs_and_photos, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {'page_obj': page_obj, 'user': user}
        return render(request, 'blog/home.html', context)


@login_required
@permission_required('blog.add_photo', raise_exception=True)
def photo_upload(request):
        if request.method == 'POST':
                form = PhotoForm(request.POST, request.FILES)
                if form.is_valid():
                        photo = form.save(commit=False)
                        photo.uploader = request.user
                        photo.save()
                        return redirect('home')
        else:
                form = PhotoForm()
        context = {'form':form}
        return render(request, 'blog/photo_upload.html', context)

@login_required
def profil_photo(request):
        if request.method == 'POST':
                form = ProfilPhotoForm(request.POST, request.FILES, instance=request.user)
                if form.is_valid():
                        form.save()
                        return redirect('home')
        else:
                form = ProfilPhotoForm(instance=request.user)
        context = {'form': form}
        return render(request, 'blog/photo_de_profil.html', context)

@login_required
@permission_required('blog.add_blog', raise_exception=True)
def billet_de_blog(request):
        if request.method == 'POST':
                photo_form = PhotoForm(request.POST, request.FILES)
                blog_form = BlogForm(request.POST)
                if all( [photo_form.is_valid(), blog_form.is_valid()] ):
                        photo = photo_form.save(commit=False)
                        photo.uploader = request.user
                        photo.save()
                        blog = blog_form.save(commit=False)
                        blog.author = request.user
                        blog.photo = photo
                        blog.save()
                        blog.contributors.add(request.user, through_defaults={'contribution': 'Auteur principal'})
                        return redirect('home')
        else:
                photo_form = PhotoForm()
                blog_form = BlogForm()
        context = {'photo_form': photo_form, 'blog_form': blog_form}
        return render(request, 'blog/billet_de_blog.html', context)

@login_required
@permission_required('blog.view_blog', raise_exception=True)
def billets_de_blog(request):
        billets_blog = Blog.objects.all()
        context = {'billets_blog': billets_blog}
        return render(request, 'blog/billets_de_blog.html', context)

@login_required
@permission_required('blog.view_blog', raise_exception=True)
def description_billet(request, id):
        billet = Blog.objects.get(id=id)
        context = {'billet': billet}
        return render(request, 'blog/liste_des_billets_de_blog.html', context)

@login_required
@permission_required('blog.delete_blog', raise_exception=True)
@permission_required('blog.change_blog', raise_exception=True)
def delete_or_edit_billet(request, blog_id):
        billet = Blog.objects.get(id=blog_id)
        if request.method == 'POST':
                if 'edit_blog' in request.POST:
                        blog_form = BlogForm(request.POST, instance=billet)
                        if blog_form.is_valid():
                                billet = blog_form.save()
                                billet.contributors.add(request.user, through_defaults = {'contribution': 'Acteur Secondaire'})
                                return redirect('home')
                if 'delete_blog' in request:
                        # delete_form = DeleteBlogForm(request.POST)
                        # if delete_form.is_valid():
                        billet.delete()
                        return redirect('billets_de_blog')
        else:
                blog_form = BlogForm(instance=billet)
                delete_form = DeleteBlogForm()  
        context = {'blog_form': blog_form, 'delete_form': delete_form} 
        return render(request, 'blog/update_or_delete_blog.html', context)   

@login_required
@permission_required('blog.add_photo', raise_exception=True)
def create_formset_photo(request):
        PhotoFormSet = formset_factory(PhotoForm, extra=5)
        if request.method == 'POST':
                PhotoSets = PhotoFormSet(request.POST, request.FILES)
                if PhotoSets.is_valid():
                        for PhotoSet in PhotoSets:
                                if PhotoSet.cleaned_data:
                                        PhotoSet.save(commit=False)
                                        PhotoSet.uploader = request.user
                                        PhotoSet.save()
                        return redirect('home')
        else:
                PhotoSets = PhotoFormSet()
        context = {'PhotoSets': PhotoSets}
        return render(request, 'blog/formset.html', context)
        
@login_required
def follows_creators(request):
        if request.method == 'POST':
                follow_form = FollowUserForm(request.POST, instance=request.user)
                if follow_form.is_valid():
                        follow_form.save()
                        return redirect('home')
        else:
                follow_form = FollowUserForm(instance=request.user)
        context = {'follow_form': follow_form}
        return render(request, 'blog/follows_creators.html', context)

@login_required
def flux_feed(request):
        user = request.user
        user_follow = user.follows.all()
        print(f'user follows : { user_follow} ')
        # Je récupère les photos publiées par les utilisateurs que suivent mon utilisateur qui ont contribué aux billets de blog
        photos = Photo.objects.filter(blog__contributors__in=user_follow).distinct()
        print(f'Les photos sont : {photos}')
        paginator = Paginator(photos, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'page_obj': page_obj}
        return render(request, 'blog/photo_feed.html', context)


        
       

        





        






# Create your views here.
