# Generated by Django 4.2.8 on 2023-12-13 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0002_alter_todoitem_deadline_alter_todoitem_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('complete', 'Complete')], default='inprogress', max_length=20),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
