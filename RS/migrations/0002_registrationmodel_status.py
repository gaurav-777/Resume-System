
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationmodel',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]
