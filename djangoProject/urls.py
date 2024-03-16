from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
import DGKP
from DGKP import views
from DGKP.models import Breaking

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='sign_in.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('accounts/profile/', DGKP.views.profile, name='profile'),
    path('', DGKP.views.index, name='index'),
    path('journal', DGKP.views.journal, name='journal'),
    path('journal/edit/<int:breaking_id>', views.edit_breaking, name='edit_breaking'),
    path('material/add/breaking/<int:breaking_id>/', views.add_material_breaking, name='add_material_breaking'),
    path('material/delete/breaking/<int:breaking_id>/<int:material_id>/', views.delete_material,
         name='delete_material_breaking'),
    path('staff/delete/<int:staff_id>/', views.delete_staff,
         name='delete_staff'),
    path('staff/edit/<int:staff_id>', views.edit_staff, name='edit_staff'),
    path('report', views.report, name='report'),
    path('staff/', views.staff, name='staff'),
    path('staff/edit/<int:staff_id>', views.edit_breaking, name='edit_staff'),
    path('send/', views.send_email, name='send_email')
]


7