from django.db import models
import datetime
from django.utils import timezone

	
class Comments(models.Model):
    class Meta:
        db_table='comments'
    comments_text=models.TextField(verbose_name="")
	
	
