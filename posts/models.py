from django.db import models

class Feedback(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    review_text = models.TextField()
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
class Post(models.Model):
    title = models.CharField(max_length=255)  # Заголовок
    content = models.TextField()             # Основной текст
    image = models.ImageField(upload_to='posts/', blank=True, null=True)  # Картинка (опционально)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return self.title