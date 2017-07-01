from django.contrib import admin
from .models import Event, Guide, Review, Attachment
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, Textarea
# Register your models here.


class AttachmentForm(ModelForm):
    class Meta:
        model=Attachment
        fields = ['text','embed']
        widgets = {
                'text': CKEditorUploadingWidget(),
                }

class AttachmentInline(admin.StackedInline):
    model = Attachment
    form = AttachmentForm

class MyAttachment(admin.ModelAdmin):
    form = AttachmentForm

class MyEvent(admin.ModelAdmin):
    inlines = [AttachmentInline]


admin.site.register(Event, MyEvent)
admin.site.register(Guide)
admin.site.register(Review)
admin.site.register(Attachment, MyAttachment)
