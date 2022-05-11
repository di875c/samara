from django.views import View
from django.shortcuts import render
from .static.text import static_text

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