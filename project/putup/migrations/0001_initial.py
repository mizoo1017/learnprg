# Generated by Django 3.2.5 on 2022-01-04 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='商品名')),
                ('description', models.TextField(max_length=2000, verbose_name='商品説明')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='商品画像')),
                ('start_price', models.PositiveIntegerField(default=0, verbose_name='開始価格')),
                ('condition', models.CharField(choices=[('new', '新品'), ('like_new', '新古品'), ('used_better', '良中古品'), ('used_worse', '悪中古品'), ('junk', 'ジャンク品')], max_length=20, verbose_name='商品状態')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='出品日')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='出品者名')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
    ]
