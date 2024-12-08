from django.shortcuts import render,get_object_or_404, redirect
from .models import Post, Feedback
from .forms import FeedbackForm
def home(request):
        return render(request,'home.html')

def about(request):
        return render(request,'about.html')

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Сортировка постов от новых к старым
    context = {'posts': posts}
    return render(request, 'post_list.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    context = {'post': post}
    return render(request, 'post_detail.html', context)

def leave_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')  # Перенаправление на страницу успеха
    else:
        form = FeedbackForm()
    context = {'form': form}
    return render(request, 'leave_feedback.html', context)

def feedback_list(request):
    feedbacks = Feedback.objects.filter(is_checked=True).order_by('-id')  # Только проверенные отзывы
    context = {'feedbacks': feedbacks}
    return render(request, 'feedback_list.html', context)

# Страница успеха (после отправки отзыва)
def feedback_success(request):
    return render(request, 'feedback_success.html')