from django.urls import path
from . views import *
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', home, name = 'home'),
    path('upload_photo/', photo_upload, name='photo_upload'),
    path('upload_profil_photo/', profil_photo, name = 'profil_photo'),
    path('upload_billet_de_blog/', billet_de_blog, name = 'billet_de_blog'),
    path('billets_de_blog/', billets_de_blog, name = 'billets_de_blog'),
    path('billet_de_blog/<int:id>/', description_billet, name = 'description_billet'),
    path('delete_or_edit_billet/<int:blog_id>/', delete_or_edit_billet, name = 'delete_or_edit_billet'),
    path('upload_multiple_photo/', create_formset_photo, name = 'create_formet_photo' ),
    path('follows_creators/', follows_creators, name='follows_creators'),
    path('flux_photos/', flux_feed, name='flux_feed'),

]

