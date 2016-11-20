from django import forms




class ContactForm(forms.Form):
    FEEDBACK = 'F'
    CORRECTION = 'C'
    SUPPORT = 'S'
    REASON_CHOICES = (
        (FEEDBACK, 'Feedback'),
        (CORRECTION, 'Correction'),
        (SUPPORT, 'Support'),
    )
    reason = forms.ChoiceField(
        choices=REASON_CHOICES,
        initial=FEEDBACK)
    email = forms.EmailField(initial='youremail@domain.com')
    text = forms.CharField(widget=forms.Textarea)
