from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('<int:pk>/edit/', login_required(views.EditView.as_view()), name='data_edit'),
    path('<int:pk>/delete/', login_required(views.DeleteItemView.as_view()), name='data_delete'),
    path('add/', login_required(views.index), name='add'),
    path('', login_required(views.ListListView), name='home')
]