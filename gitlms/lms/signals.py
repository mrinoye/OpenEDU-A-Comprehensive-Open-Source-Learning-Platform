# accounts/signals.py
import os
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.db.models import FileField

@receiver(pre_save)
def delete_old_file_on_change(sender, instance, **kwargs):
    """
    Deletes the old file from any FileField on a model if a new file is uploaded.
    Does not delete if the file is the default value.
    """
    if not instance.pk:  # New instance, nothing to delete
        return

    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    for field in instance._meta.fields:
        if isinstance(field, FileField):
            old_file = getattr(old_instance, field.name)
            new_file = getattr(instance, field.name)
            if old_file and old_file != new_file:
                if field.default and str(old_file) == str(field.default):
                    continue
                if os.path.isfile(old_file.path):
                    os.remove(old_file.path)

@receiver(post_delete)
def delete_file_on_instance_delete(sender, instance, **kwargs):
    """
    Deletes the file from any FileField on a model when the instance is deleted,
    unless the file is set to the default value.
    """
    for field in instance._meta.fields:
        if isinstance(field, FileField):
            file_field = getattr(instance, field.name)
            if file_field:
                if field.default and str(file_field) == str(field.default):
                    continue
                if os.path.isfile(file_field.path):
                    os.remove(file_field.path)
