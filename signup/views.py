import io
from django import forms
from django.shortcuts import redirect, render
from core.models import Gn_user
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class UserForm(forms.ModelForm):
    class Meta:
        model = Gn_user
        fields = ['name', 'surname', 'mail', 'username', 'password', 'profile_picture']

    def clean_profile_picture(self):
        profile_picture = self.cleaned_data.get('profile_picture')
        if profile_picture:
            if profile_picture.name.split('.')[-1].lower() not in ['jpg', 'jpeg', 'png']:
                raise forms.ValidationError("Yalnızca JPG ve PNG dosyaları kabul edilir.")
        return profile_picture

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            profile_picture = form.cleaned_data.get('profile_picture')
            if profile_picture:
                # Resmi boyutlandır
                image = Image.open(profile_picture)
                image.thumbnail((80, 80), Image.ANTIALIAS)

                # BytesIO'ya kaydet
                output = io.BytesIO()
                image.save(output, format='PNG')
                output.seek(0)

                # Küçültülmüş resmi kaydet
                user.profile_picture.save(profile_picture.name, ContentFile(output.read()), save=False)
            user.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})
