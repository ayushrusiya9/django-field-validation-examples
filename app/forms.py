from django import forms
from django.core.exceptions import ValidationError

class StudentForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    contact = forms.IntegerField(required=False)
    image = forms.ImageField(required=False)
    file = forms.FileField(required=False)

    # --- Field-level validations ---
    def clean_name(self):
        name = self.cleaned_data.get('name')
        print(name)
        print(type(name))
        if len(name)==0:
            raise ValidationError("Name field cannot be Empty.")
        
        elif name.isdigit():
            raise ValidationError("Name should not contain numbers.")
        
        elif name[0].isdigit():
            raise ValidationError("Name should not start with a number.")

        elif not (name.isalpha() and len(name)<20 and len(name)>3):
            raise ValidationError("Name should only contain letters and in between 4 to 20 letters")
        
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        print(email)
        print(type(email))
        if len(email)==0:
            raise ValidationError("Email cannot be Empty.")
        
        elif email.isdigit():
            raise ValidationError("Email should not contain numbers.")
        
        elif email[0].isdigit():
            raise ValidationError("Email should not start with a number.")

        elif not email.lower().endswith(('@gmail.com','@yahoo.com')):
            raise ValidationError("Only gmail and yahoo addresses are allowed.")
        
        return email

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        print(contact)
        print(type(contact))
        if contact is None:
            raise ValidationError("Contact cannot be Empty.")
        
        elif len(str(contact))<10 or len(str(contact))>10 :
            raise ValidationError("Contact must be a 10-digit number.")
        
        return contact

    def clean_image(self):
        image = self.cleaned_data.get('image')
        print(image)
        print(type(image))
        if image is None:
            raise ValidationError("Image cannot be Empty.")
        
        elif image and not image.name.lower().endswith(('.jpeg', '.png','jpg')):
            raise ValidationError("Image must be either .jpeg or .png")
        
        elif image and image.size > 2 * 1024 * 1024:
            raise ValidationError("Image size should not exceed 2MB.")
        return image

    def clean_file(self):
        file = self.cleaned_data.get('file')
        print(file)
        print(type(file))
        if file is None:
            raise ValidationError("File cannot be Empty.")
        
        elif file and not file.name.lower().endswith(('.pdf','.doc','.docx')):
            raise ValidationError("Only PDF.DOC and DOCX files are allowed.")
        
        return file

