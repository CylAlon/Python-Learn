from django.db import models

# Create your models here.
class InfoFilesBeaseMessage(models.Model):
    admin_number = models.CharField(max_length=255)
    file_path = models.FileField(upload_to='bease_message')

    class Meta:
        db_table = 'info_files_bease_message'
