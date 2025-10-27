from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='highlight',
            field=models.BooleanField(default=False),  # adjust default if needed
        ),
    ]
