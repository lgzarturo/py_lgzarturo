from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from articles.views import index as blog_index, category_article, show as blog_show
from catalogs.views import index as home
from profiles.views import index as profiles_index, Pdf
from projects.views import index as projects_index, show as project_show

urlpatterns = [
    path('', home, name='index'),
    path('blog/', blog_index, name='blog'),
    path('blog/category/<slug:slug>/', category_article, name='category'),
    path('blog/<slug:slug>/', blog_show, name='blog_show'),
    path('projects/', projects_index, name='projects'),
    path('projects/<slug:slug>/', project_show, name="projects_show"),
    path('profile/', profiles_index, name='profile'),
    path('profile-pdf/', Pdf.as_view(), name='profile-pdf'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
