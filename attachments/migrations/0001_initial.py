# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import attachments.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('attachment_file', models.FileField(upload_to=attachments.models.Attachment.attachment_upload, verbose_name='attachment')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('creator', models.ForeignKey(related_name='created_attachments', verbose_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
                'db_table': 'attachments_attachment',
                'permissions': (('delete_foreign_attachments', 'Can delete foreign attachments'),),
            },
        ),
    ]
