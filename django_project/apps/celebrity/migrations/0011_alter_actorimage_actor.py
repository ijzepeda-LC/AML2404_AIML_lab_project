# Generated by Django 4.2.1 on 2023-06-15 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("celebrity", "0010_alter_elasticsearchactorimage_actor_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actorimage",
            name="actor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="celebrity.actor"
            ),
        ),
    ]