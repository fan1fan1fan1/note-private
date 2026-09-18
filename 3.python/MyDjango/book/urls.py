from django.urls import path
from . import views

app_name = 'book' # 指定应用名称(应用命名空间)

urlpatterns = [
    path('list', views.movie_list,name='movie_list'),
    path('detail/<int:movie_id>', views.movie_detail, name='movie_detail'),

    # view中 route以book/开头的都可以转到这里 然后前缀book/可以删掉
]