# from  django.conf.urls import url "never use it"
from django.urls import path
from first_app import views

urlpatterns = [
   # path('', views.index , name='index'),
   # path('add_musician/', views.musician_form, name='musician_form'),
   # path('add_album/', views.album_form, name='album_form'),
   # path('album_list/<int:artist_id>/', views.album_list, name='album_list'),
   # path('edit_artist/<int:artist_id>/', views.edit_artist, name='edit_artist'),
   # path('edit_album/<int:album_id>/', views.edit_album, name='edit_album'),
   # path('delete_album/<int:album_id>/', views.delete_album, name='delete_album'),
   # path('delete_artist/<int:artist_id>/', views.delete_musician, name='delete_artist'),

   path('', views.IndexView.as_view(), name='index'),
   path('musician_details/<pk>/', views.MusicanDetail.as_view(), name='musician_details'),
   path('add_musician/', views.AddMusician.as_view(), name='add_musician'),
   path('musician_update/<pk>/', views.UpdateMusician.as_view(), name='musician_update'),
   path('musician_delete/<pk>/', views.DeleteMusician.as_view(), name='musician_delete'),

]
