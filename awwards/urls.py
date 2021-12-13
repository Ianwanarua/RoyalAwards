from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name = 'index'),
    path('signup/', views.signup, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('update/<id>', views.update_profile, name='update_profile'),
    path('upload/',views.post_project,name='post_prj'),
    path('project_info/(?P<id>\d+)', views.view_project, name='viewProject'),

    #api endpoints
    path('api/v1/profile',views.ProfileList.as_view(),name='profileEndpoint'),
    path('api/v1/projects',views.ProjectList.as_view(),name='projectsEndpoint')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)