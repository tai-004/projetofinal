from django import forms
from .models import File

# Model form
class FileUploadModelForm(forms.ModelForm):
    
    class Meta:
        model = File
        fields =["file", "titulo", "texto", "equipe", "turma", "curso", "orientador", "postar"]


    def clean_file(self):
        file = self.cleaned_data['file']
        ext = file.name.split('.')[-1].lower()
        if ext not in ["jpg", "pdf", "xlsx", "png", "jpeg"]:
            raise forms.ValidationError("Only jpg, pdf, xlsx, png and jpeg files are allowed.")
        
        # return cleaned data is very important.
        return file
      
