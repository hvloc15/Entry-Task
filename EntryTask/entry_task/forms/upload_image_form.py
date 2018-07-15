from django import forms
class UploadImagesForm(forms.Form):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': 'multiple'}),
                             required=True)

    def get_list_images(self):
        return [image for image in self.files.getlist('images')]

    def clean(self):
        images = self.files.getlist('images')
        for image in images:
            if image:
                if image._size > 15 * 1024 * 1024:
                    raise forms.ValidationError("Image file is too large ( > 15mb ).")
                if not image.content_type in ['image/jpeg', 'image/png']:
                    raise forms.ValidationError(
                        "Sorry, we do not support that video MIME type. Please try uploading a jpeg or png file.")
                return images
            else:
                raise forms.ValidationError("Could not read the uploaded file.")