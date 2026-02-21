from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Question
from .forms import QuestionForm

def index(request):
    q = request.GET.get("q", "").strip()

    qs = Question.objects.order_by("-pub_date")
    if q:
        qs = qs.filter(question_text__icontains=q) | qs.filter(car_model__icontains=q)

    context = {
        "latest_question_list": qs,
        "q": q,
    }
    return render(request, "polls/index.html", context)



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def add(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.pub_date = timezone.now()
            obj.save()
            messages.success(request, "点検を登録しました。")
            return redirect("polls:index")
        else:
            messages.error(request, "入力内容を確認してください。")
    else:
        form = QuestionForm()
    return render(request, "polls/add.html", {"form": form})


def edit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, "点検を更新しました。")
            return redirect("polls:detail", question_id=question.id)
        else:
            messages.error(reqest, "入力内容を確認してください。")
    else:
        form = QuestionForm(instance=question)

    return render(request, "polls/edit.html", {"form": form, "question": question})


@require_POST
def delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    messages.success(request, "点検を削除しました。")
    return redirect("polls:index")
