from django.urls import include, path
from . import views
from mptt.models import MPTTModel, TreeForeignKey



app_name = 'BlogV2'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('search/', views.post_search, name='post_search'),
    path('<slug:post>/', views.post_single, name='post_single'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
]
