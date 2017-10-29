from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Flavour
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'product/index.html'
    context_object_name = 'all_flavours'

    def get_queryset(self):
        return Flavour.objects.all()


class DetailView(generic.DetailView):
    model = Flavour
    template_name = 'product/detail.html'


class FlavourCreate(CreateView):
    model = Flavour
    fields = ['company', 'flavour_title', 'made_in', 'flavour_image']


class FlavourUpdate(UpdateView):
    model = Flavour
    fields = ['company', 'flavour_title', 'made_in', 'flavour_image']


class FlavourDelete(DeleteView):
    model = Flavour
    success_url = reverse_lazy()


class UserFormView(View):
    form_class = UserForm
    template_name = 'product/registration_form.html'

    # /displays blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Adds to daataa base
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('product:index')

        return render(request, self.template_name, {'form': form})
    # cannie login? try again.

























