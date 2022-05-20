from django.views import View, generic
from django.shortcuts import render, redirect
from .static.text import static_text
from django.urls import reverse_lazy
from .forms import SignUpForm, SelfUserChangeForm
from django.contrib.auth.decorators import login_required
from .models import MainUser


class MainPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'first_page.html')


class AboutUs(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resume_page.html', {'work_list': static_text.work_list,
            'skill_list': static_text.skills_list, 'about_me': static_text.about_me, 'contact': static_text.contact})


class ErrorView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'error_page.html')


class SignView(generic.CreateView):
    #Create new user
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required(login_url='/accounts/login')
def user_change_settings(request):
    #Update user profile
    template_name = 'registration/change_user.html'
    user = MainUser.objects.get(pk=request.user.pk)
    if request.method == 'POST':
        form = SelfUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(to='/')
    else:
        form = SelfUserChangeForm(instance=user)
    return render(request, template_name, {'form': form})



