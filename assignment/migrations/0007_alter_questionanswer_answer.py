# Generated by Django 4.2.3 on 2023-08-15 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0006_exam_examquestion_questionanswer_examresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionanswer',
            name='answer',
            field=models.TextField(),
        ),
    ]
