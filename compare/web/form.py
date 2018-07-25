from django import forms


class UploadFileForm(forms.Form):
    title_a1 = forms.CharField(max_length=50, required=False)
    title_a2 = forms.CharField(max_length=50, required=False)
    title_a3 = forms.CharField(max_length=50, required=False)
    title_a4 = forms.CharField(max_length=50, required=False)
    file_a1 = forms.FileField( required=False)
    file_a2 = forms.FileField( required=False)
    file_a3 = forms.FileField( required=False)
    file_a4 = forms.FileField( required=False)
    title_b1 = forms.CharField(max_length=50, required=False)
    title_b2 = forms.CharField(max_length=50, required=False)
    title_b3 = forms.CharField(max_length=50, required=False)
    title_b4 = forms.CharField(max_length=50, required=False)
    file_b1 = forms.FileField( required=False)
    file_b2 = forms.FileField( required=False)
    file_b3 = forms.FileField( required=False)
    file_b4 = forms.FileField( required=False)