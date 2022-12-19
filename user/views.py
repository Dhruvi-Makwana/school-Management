from django.http import HttpResponse
from .models import User
from django.shortcuts import render, get_object_or_404, redirect
from .forms import Adduser

from django.views.generic import ListView
from django.views.generic import DetailView, UpdateView, DeleteView,RedirectView,CreateView


class UserDetail(ListView):
    template_name = 'user/index.html'
    # queryset = User.objects.filter(id__lt=7)

    def get_queryset(self):
        # return User.objects.filter(id__lt=7)
        return User.objects.all().order_by('id')


class Detail(DetailView):
    template_name = 'user/detail.html'
    model = User


class AddUser(CreateView):
    template_name = 'user/adduser.html'
    form_class = Adduser
    success_url = '/user'

    def get(self, request, *args, **kwargs):
        data = {"user_type": "student"}
        form = Adduser(initial = data)
        # breakpoint()
        return render(request, 'user/adduser.html', {'form': form})

    def post(self, request, *args, **kwargs):
        data = {"user_type" :"student"}
        form = Adduser(request.POST, initial = data)
        # import pdb;pdb.set_trace()
        if form.is_valid():
            form.save()
        return render(request, 'user/adduser.html', {'form': form})
























#     def detail(request, user_id):
#     get_data = get_object_or_404(User, pk=user_id)
#     return render(request, 'user/detail.html', {'s1': get_data})


# class View1(ListView):
#     model = User
#     queryset = User.objects.filter(id__gt=5) #it wrote id which is grater than 5
#     # queryset = User.objects.filter(username__contains='he')
#
#
# class View2(DetailView):
#     model = User


# class View3(UpdateView):
#     model = User
#     fields = ['username']
#     success_url = "/"
#
#
# class View4(DeleteView):
#     model = User
#     success_url = "/"

#example of redirect method

def example(request):
    return redirect('/user/')
