# Generated by Django 4.0.6 on 2022-08-03 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('final_project', '0002_shoppingcart_shoppingcartcourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='final_project.student'),
        ),
        migrations.AlterField(
            model_name='shoppingcartcourse',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='final_project.course'),
        ),
    ]