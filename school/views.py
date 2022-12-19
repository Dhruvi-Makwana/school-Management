from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject, Standards
from .forms import Subject1, Standard1, LoginForm
from django.views.generic import DetailView, UpdateView, DeleteView,RedirectView, ListView, CreateView
# Create your views here.

def Input1(request):
    form_input = LoginForm()
    return render(request,'school/login.html', {'form': form_input})


def get_faculty(request):
    return render(request,'school/hello.html')


class StandardDetail(ListView):
    template_name = 'school/index.html'
    # def standard_details(request):
    queryset = Standards.objects.all().order_by('name')


class UpdateStandard(UpdateView):
    model = Standards
    fields = ['class_teacher']
    template_name = 'school/updatestand.html'
    success_url = "/school"
    # form_class = Standard1


class Deletestandard(DeleteView):
    model = Standards
    template_name = 'school/deletestand.html'
    success_url = "/school"


class SubjectDetail(ListView):
    template_name = 'school/subject.html'
    queryset = Subject.objects.all()


class UpdateSubject(UpdateView):
    model = Subject
    fields = ['subject_teacher', 'standards']
    template_name = 'school/updatesubject.html'
    success_url = "/school/subject"


class DeleteSubject(DeleteView):
    model = Subject
    template_name = 'school/deletesubject.html'
    success_url = "/school/subject"


class AddSubject(CreateView):
    # import pdb;pdb.set_trace()
    template_name = 'school/addsubject.html'
    form_class = Subject1

    def get(self, request, *args, **kwargs):
        form = Subject1()
        return render(request, 'school/addsubject.html', {'form': form})

    def post(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace()
        form = Subject1(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = Subject1()
        return render(request, 'school/addsubject.html', {'form': form})


class AddStandard(CreateView):
    template_name = 'school/addstandards.html'
    form_class = Standard1

    def get(self, request, *args, **kwargs):
        add_stand = Standard1()
        return render(request, 'school/addstandards.html', {'add': add_stand})

    def post(self, request, *args, **kwargs):
    # import pdb; pdb.set_trace()
    #     if request.method == "POST":
        add_stand = Standard1(request.POST)
        if add_stand.is_valid():
            add_stand.save()
            add_stand = Standard1()
        # else:
        #     add_stand = Standard1()
        return render(request, 'school/addstandards.html', {'add': add_stand})
