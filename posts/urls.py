from django.urls import path
from .views import home,about, post_list, post_detail, leave_feedback, feedback_list, feedback_success
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",home,name="home"),
    path("about/",about,name="about"),
    path('posts/', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),  # Детальная страница для поста
    path('leave_feedback/', leave_feedback, name='leave_feedback'),  # Оставить отзыв
    path('feedback_list/', feedback_list, name='feedback_list'),  # Все отзывы
    path('feedback_success/', feedback_success, name='feedback_success'),  # Успех (после отзыва)
]
if settings.DEBUG:  # Обслуживаем медиа файлы только в режиме DEBUG
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)