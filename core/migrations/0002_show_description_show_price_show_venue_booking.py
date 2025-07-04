# Generated by Django 5.2 on 2025-04-25 08:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='show',
            name='venue',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('booked_at', models.DateTimeField(auto_now_add=True)),
                ('venue', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.show')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
