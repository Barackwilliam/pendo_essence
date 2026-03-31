from django.db import migrations, models


class Migration(migrations.Migration):
    """
    0002: Badilisha ImageField → CharField(max_length=255)
    kwa ajili ya kuhifadhi Uploadcare UUID badala ya file path ya local
    """

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        # Category.image
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.CharField(
                blank=True, null=True, max_length=255,
                help_text='Uploadcare file UUID e.g. 7a8c0d2c-bfa3-491a-afb0-83b9471ffa3e'
            ),
        ),
        # Product.image
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(
                blank=True, null=True, max_length=255,
                help_text='Uploadcare file UUID — picha kuu ya bidhaa'
            ),
        ),
        # Product.image2
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.CharField(
                blank=True, null=True, max_length=255,
                help_text='Uploadcare file UUID — picha ya pili'
            ),
        ),
        # Product.image3
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.CharField(
                blank=True, null=True, max_length=255,
                help_text='Uploadcare file UUID — picha ya tatu'
            ),
        ),
        # ProductImage.image
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.CharField(
                max_length=255,
                help_text='Uploadcare file UUID'
            ),
        ),
    ]
