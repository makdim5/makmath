from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.checks import messages
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, TemplateView

from .forms import *
from .models import *
from .utils import StatisticsManager

menu = [
    {'title': "О сайте", 'url_name': 'about'},
]


def show_topic(request, topic_slug):
    topic = get_object_or_404(Topic, slug=topic_slug)
    tasks = Task.objects.filter(topic=topic)
    context = {
        'topic': topic,
        'menu': menu,
        'title': topic.topic_name,
        'lection': topic.content,
        'tasks': tasks,
        'forms': "",
        'section_link': topic.section.get_absolute_url(),
    }
    forms = []
    if request.user.is_authenticated:

        i = 0
        if request.method == 'POST':
            keys = list(request.POST.keys())
        for t in tasks:
            form = TaskForm(request.POST)
            form.fields['answer'].label = t.task_info
            form.prefix = i + 1
            form.flag = True if TaskComplition.objects.filter(
                task=t, user=request.user) else False
            i += 1
            if request.method == 'POST':
                if str(i) in keys[len(keys) - 1]:
                    form.flag = t.check_task(
                        request.POST[f'{i}-answer'])
                    if form.flag and \
                            not TaskComplition.objects.filter(
                                task=t, user=request.user):
                        task_completed = TaskComplition(
                            task=t, user=request.user)
                        task_completed.save()
            forms.append(form)

    context['forms'] = forms
    return render(request, 'topics/topic.html', context=context)


class MakMathHome(ListView):
    model = Section
    template_name = "topics/index.html"
    context_object_name = "sections"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'MakMath главная страница'
        return context

    def get_queryset(self):
        return Section.objects.filter(is_published=True)


class SectionShower(ListView):
    model = Topic
    template_name = "topics/section.html"
    context_object_name = "topics"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        if context['topics']:
            context['title'] = str(context['topics'][0].section)

        return context

    def get_queryset(self):
        return Topic.objects.filter(section__slug=self.kwargs['section_slug'])


def about(request):
    context = {'menu': menu, 'title': "O сайте"}
    return render(request, 'topics/about.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'topics/authorization.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'topics/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return dict(list(context.items()))


def show_user_info(request):

    context = {'menu': menu,

               'title': f"Профиль {request.user.username}",
               'stat_info':
                   StatisticsManager.get_statistics_in_html(request.user)}
    return render(request, 'topics/user_cabinet.html', context=context)


def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return HttpResponseRedirect(reverse_lazy('login'))
