from django import forms


class UploadFileForm(forms.Form):
    title1 = forms.CharField(max_length=50, required=False)
    title2 = forms.CharField(max_length=50, required=False)
    title3 = forms.CharField(max_length=50, required=False)
    title4 = forms.CharField(max_length=50, required=False)
    file1 = forms.FileField( required=False)
    file2 = forms.FileField( required=False)
    file3 = forms.FileField( required=False)
    file4 = forms.FileField( required=False)
