"""
URL configuration for Conservation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ConservationForum.views import HomeView, BadgeView, SpeciesView, ForumView, AddPostView, AlterSpecies, DeletePostView, Gallery, FaqView
from accounts import views as account_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('species/', SpeciesView.as_view(), name='specList'),
    path('forum', ForumView.as_view(), name='forum'),
    path('addpost', AddPostView.as_view(), name='addPost'),
    path('login/', account_view.LoginView.as_view(), name='login_view'),
    path('logout/', account_view.LogoutView.as_view(), name='logout_view'),
    path('signup/', account_view.RegisterView.as_view(), name='register_view'),
    path('alter_species/<int:pk>/', AlterSpecies.as_view(), name='alter_species'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('gallery/', Gallery.as_view(), name='gallery'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('addbadge/<int:pk>/', BadgeView.as_view(), name='add_badge'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)