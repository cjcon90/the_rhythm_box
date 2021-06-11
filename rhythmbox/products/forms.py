from django import forms
from .models import Review, Rating


class ProductRatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ("rating",)


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("headline", "content")
        labels = {"headline": "Review Headline", "content": "Your Review"}
        widgets = {
            "content": forms.Textarea(attrs={"rows": 10, "cols": "auto"}),
        }
