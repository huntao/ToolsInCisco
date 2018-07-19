from django import forms


class UploadFileForm(forms.Form):
    title1 = forms.CharField(max_length=50)
    title2 = forms.CharField(max_length=50)
    file1 = forms.FileField()
    file2 = forms.FileField()
