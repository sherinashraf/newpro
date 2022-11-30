from django.urls import path
from . import views
app_name = 'common'

urlpatterns = [
    path('index',views.common_index,name = 'index'),
    path('sofa',views.common_sofa,name = 'sofa'),
    path('beds',views.common_beds,name = 'beds'),
    path('storage',views.common_storage,name = 'storage'),
    path('dining',views.common_dining,name = 'dining'),
]