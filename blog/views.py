from django.shortcuts import render_to_response
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm
from django.views import generic
from .models import post
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.
def index(request):
    entries = post.objects.all()
    return render_to_response("abhi.html",{'entries':entries})

def detail(request,album_id):
    query=post.objects.get(pk=album_id)
    return render(request, 'blog/detail.html', {'query':query})

class postCreate(CreateView):
    model = post
    fields = ['title','author','date','body','logo']

class UserFormView(View):
    form_class = UserForm
    template_name='registration_form.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username = username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('/blog/')
        return render(request,self.template_name,{'form':form})