from django.db import models
from accounts.models import CustomUser
from mdeditor.fields import MDTextField


class Diary(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="ユーザー", on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    image_path = models.CharField(verbose_name='画像パス', max_length=255, blank=True)
    subtitle = models.CharField(verbose_name='サブタイトル', max_length=255, null=True)
    # content = models.TextField(verbose_name='本文', blank=True, null=True)
    content = MDTextField()
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = "Diary"


