from django.db import models
from django.contrib.auth.models import User


class Notebook(models.Model):
    notebook_id = models.AutoField(
        null=False,
        primary_key=True,
        unique=True
    )
    notebook_name = models.CharField(
        max_length=512,
        null=False,
        default="New Notebook"
    )
    notebook_color = models.CharField(
        max_length=128,
        null=False,
        default="Blue"
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.owner.username + " | " + self.notebook_name


class Page(models.Model):
    page_id = models.AutoField(
        null=False,
        primary_key=True,
        unique=True
    )
    page_name = models.CharField(
        max_length=256,
        null=False,
        default="New Page"
    )
    page_color = models.CharField(
        max_length=128,
        null=False,
        default="Blue"
    )
    parent_notebook = models.ForeignKey(
        Notebook,
        on_delete=models.CASCADE,
        null=False
    )
    list_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.parent_notebook + " " + self.page_id


class List(models.Model):
    list_id = models.AutoField(
        null=False,
        primary_key=True,
        unique=True
    )
    parent_page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.parent_page + " " + self.list_id


class List_object(models.Model):
    object_id = models.AutoField(
        null=False,
        primary_key=True,
        unique=True
    )
    parent_list = models.ForeignKey(
        List,
        on_delete=models.CASCADE,
        null=False
    )
    text = models.TextField(max_length=2048, null=True, default=None)
    indent_level = models.IntegerField(default=0, null=False)
    font = models.JSONField(
        null=False,
        default={
            'font': "Arial, Helvetica, sans-serif",
            'style': None,
            'size': "medium",
            "color": "black"
        }
    )
    is_checked = models.BooleanField(default=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.parent_list + " " + self.object_id
