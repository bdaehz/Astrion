from django.contrib import admin
from django.urls import path, include
from two_factor.views import SetupView  # Vista predefinida de 2FA
from landing import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.Loadlogin, name='login'),
    path('register/', views.register, name='register'),
    path('LogOut/', views.Logout, name='LogOut'),
    path('2faapp/', include(('two_factor.urls', 'two_factor'))),
    path('2fa/setup/', SetupView.as_view(), name='setup_2fa'),  # Esta vista maneja el flujo de configuración de 2FA
    path('settings/', views.Settings, name='settings'),
    path('postear/', views.Posting, name='posting'),
    path('search/', views.Buscar, name='search'),
    path('perfil/usuario/<str:username>/', views.ver_perfil, name='ver_perfil'),
    path('perfil/editar/', views.EditCuenta, name='editar_perfil'),
    path('delete/<int:id>/<str:volver>', views.DeletePost, name='DeltePost'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
