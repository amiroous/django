# Generated by Django 2.2.5 on 2019-10-25 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessrecord',
            name='name',
        ),
        migrations.AddField(
            model_name='accessrecord',
            name='webpage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_1.WebPage'),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_1.Topic'),
        ),
    ]
