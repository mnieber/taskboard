from django import forms


class AbstractRejectionForm(forms.Form):
    send_email = forms.BooleanField(label="Send email", required=False)


class RejectionFormWithoutEmail(AbstractRejectionForm):
    pass


class RejectionFormWithEmail(AbstractRejectionForm):
    email_subject = forms.CharField(required=True,)
    email_body = forms.CharField(required=True,)


class RequestOnboardingCallForm(forms.Form):
    email_subject = forms.CharField(required=True,)
    email_body = forms.CharField(required=True,)
    google_doc_url = forms.CharField(required=True,)
    calendar_url = forms.CharField(required=True,)


class RequestQuizResultsForm(forms.Form):
    email_subject = forms.CharField(required=True,)
    email_body = forms.CharField(required=True,)
    quiz_url = forms.CharField(required=True,)


class ApproveForm(forms.Form):
    email_subject = forms.CharField(required=True,)
    email_body = forms.CharField(required=True,)
