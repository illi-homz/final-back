# Generated by Django 3.0.6 on 2020-07-02 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200702_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='groups',
            field=models.ManyToManyField(to='app.GroupInTestModel'),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='questions',
            field=models.ManyToManyField(to='app.QuestionInTestModel'),
        ),
    ]
