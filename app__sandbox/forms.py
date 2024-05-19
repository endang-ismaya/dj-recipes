from django import forms

feedback_choices = [
    ("happy", "Happy"),
    ("neutral", "Neutral"),
    ("sad", "Sad"),
]


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    feedback = forms.CharField(max_length=255)
    satisfaction = forms.ChoiceField(
        choices=feedback_choices, widget=forms.RadioSelect
    )

    def clean_email(self):
        email = self.cleaned_data["email"]
        if "yupanatech.com" not in email:
            raise forms.ValidationError("Please use your yupanatech.com email")

        return email
