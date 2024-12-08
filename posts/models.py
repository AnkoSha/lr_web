from django.db import models

class Feedback(models.Model):
    full_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=False)
    review_text = models.TextField(blank=False)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title