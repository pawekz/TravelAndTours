from django import forms
from django.core.exceptions import ValidationError
from .models import Review, TourPackage


class ReviewForm(forms.ModelForm):
    tour_package = forms.ModelChoiceField(queryset=TourPackage.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = Review
        fields = ['customername', 'rating', 'comment', 'tour_package']

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating and (rating < 1 or rating > 5):
            raise ValidationError('Rating should be between 1 and 5.')
        return rating
