from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['full_name', 'email', 'review_text']  # Поля, которые будут отображены

        # Указываем русские подписи к полям
        labels = {
            'full_name': 'ФИО',  # Поле для имени
            'email': 'Электронная почта',  # Поле для email
            'review_text': 'Текст отзыва',  # Поле для текста отзыва
        }

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше ФИО'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш e-mail'
            }),
            'review_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите ваш отзыв'
            }),
        }
