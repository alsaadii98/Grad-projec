from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from .models import PasswordsManger
from .forms import PasswordForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

def index(request):
    # initial the form
    form = PasswordForm
    # Check the method & is the form is valid
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            forma = form.save(commit=False)
            forma.author = request.user
            forma.save()
            form = PasswordForm()
            return redirect('home')

    context = {'form': form}
    return render(request, 'form.html', context)


# class HomeView(ListView, LoginRequiredMixin):
#     model = PasswordsManger
#     template_name = 'home.html'
#     context_object_name = 'datas'

def ListListView(request):
    user_data = PasswordsManger.objects.filter(author=request.user)
    return render(request, 'home.html', {'user_data': user_data})
    # current_user = request.user
    # user_list = PasswordsManger.objects.filter(author=current_user)
    # user = {
    #     'user_list': user_list
    # }
    # return render(request, 'home.html', user)


class EditView(UpdateView, LoginRequiredMixin):
    model = PasswordsManger
    fields = ('site_name', 'site_url', 'site_username', 'site_password')
    template_name = 'data_edit.html'
    success_url = reverse_lazy('home')


class DeleteItemView(DeleteView, LoginRequiredMixin):
    model = PasswordsManger
    template_name = 'data_delete.html'
    success_url = reverse_lazy('home')
