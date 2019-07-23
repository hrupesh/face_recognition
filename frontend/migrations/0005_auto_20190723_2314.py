# Generated by Django 2.2.3 on 2019-07-23 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_auto_20190723_0135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_img',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='email_default', max_length=254),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_img', models.ImageField(upload_to='user_images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.User')),
            ],
        ),
    ]
