from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Выводит список тем"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Выводит одну тему и все ее записи"""
    topic = get_object_or_404(Topic, id=topic_id)
    #Проверка того, что тема принадлежит текущему пользователю.
    check_topic_owner(request, topic)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(reqest):
    """Определяет новую тему"""
    if reqest.method != 'POST':
        #Данные не отправлялись; создается пустая форма.
        form = TopicForm()
    else:
        #Отправлены данные POST; обработать данные.
        form = TopicForm(reqest.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = reqest.user
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(reqest, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Добавляет новую запись по конкретной теме"""
    topic = Topic.objects.get(id=topic_id)

    check_topic_owner(request, topic)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                 args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """"Редактирует существуюшую запись."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    check_topic_owner(request, topic)

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

#Проверка того, что тема принадлежит текущему пользователю.
def check_topic_owner(request, topic):
    if topic.owner != request.user:
        raise Http404