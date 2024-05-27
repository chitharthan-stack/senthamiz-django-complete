# Generated by Django 5.0.4 on 2024-05-26 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_product_special_features_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dtcp_approved',
            field=models.BooleanField(default=False, help_text='Check if the product is DTCP approved'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('rejected', 'Rejected'), ('draft', 'draft'), ('disabled', 'Disabled'), ('published', 'Published')], default='in_review', max_length=10),
        ),
    ]
