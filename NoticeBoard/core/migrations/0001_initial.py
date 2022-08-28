# Generated by Django 4.1 on 2022-08-28 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', django_quill.fields.QuillField()),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp ')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rejoinder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.person')),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.notice')),
            ],
        ),
        migrations.CreateModel(
            name='NoticeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.notice')),
            ],
        ),
        migrations.AddField(
            model_name='notice',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.person'),
        ),
        migrations.AddField(
            model_name='notice',
            name='category',
            field=models.ManyToManyField(through='core.NoticeCategory', to='core.category'),
        ),
    ]
