# Generated by Django 4.0.2 on 2022-02-08 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_brand_color_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='product_imgs/')),
                ('slug', models.CharField(max_length=100)),
                ('detail', models.TextField()),
                ('specs', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.color')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.size')),
            ],
        ),
    ]
