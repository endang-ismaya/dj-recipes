from django import forms

from app__comment.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
        labels = {"text": ""}
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "placeholder": "The recipe is really great!.",
                    "class": "form-control",
                    "rows": "4",
                }
            )
        }
