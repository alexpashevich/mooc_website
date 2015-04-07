from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from moocs.models import Mooc, Lesson, Module
# from moocs.submission_testing import test_submission


def index(request):
    moocs = Mooc.objects.all()
    return render(request, 'index.html', {'moocs': moocs})


def mooc(request, mooc_id):
    mooc = Mooc.objects.get(id=mooc_id)
    return render(request, 'mooc.html', {'mooc': mooc})

@login_required(login_url='/login')
def lesson(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    modules = lesson.module_set.order_by('number')
    return render(request, 'lesson.html', {'lesson': lesson, 'modules': modules})

@login_required(login_url='/login')
def module(request, module_id):
    module = Module.objects.get(id=module_id)
    return render(request, 'module.html', {'module': module})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })

def load_description_full(request):
    print("we are here")
    mooc = Mooc.objects.get(id=int(request.GET['mooc_id']))
    # lessons_json = [lesson.as_dict() for lesson in mooc.lesson_set.all()]
    response_data = {
        'description_full': mooc.description_full
    }

    return HttpResponse(json.dumps(response_data),
                        content_type="application/json")









