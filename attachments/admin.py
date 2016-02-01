from attachments.models import Attachment
from django.contrib.contenttypes import fields

class AttachmentInlines(fields.GenericStackedInline):
    model = Attachment
    extra = 1
