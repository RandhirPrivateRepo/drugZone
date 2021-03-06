# Generated by Django 2.0 on 2020-04-26 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CategoryAndSubcategory', '0003_auto_20200426_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufaturerName', models.CharField(blank=True, max_length=255, null=True, verbose_name='Manufacturer Name')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicineName', models.CharField(blank=True, max_length=255, null=True, verbose_name='Medicine Name')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantity')),
                ('decsription', models.TextField(blank=True, null=True, verbose_name='Medicine Description')),
                ('batchNumber', models.CharField(blank=True, max_length=255, null=True, verbose_name='Batch No.')),
                ('expiryDate', models.DateField(blank=True, null=True, verbose_name='Expiry-Date')),
                ('actualPrice', models.FloatField(default=0.0, verbose_name='Actual Price (MRP)')),
                ('discountedPrice', models.FloatField(default=0.0, verbose_name='Price After Discount')),
                ('gstTax', models.IntegerField(default=0, verbose_name='GST/Other Tax')),
                ('rackNumber', models.CharField(blank=True, max_length=255, null=True, verbose_name='Rack-Number')),
                ('selfNumber', models.CharField(blank=True, max_length=255, null=True, verbose_name='Self-Number')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='Remarks')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CategoryAndSubcategory.Category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='MedicineImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/uploads/')),
            ],
        ),
        migrations.AddField(
            model_name='medicine',
            name='images',
            field=models.ManyToManyField(to='Medicines.MedicineImage'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='manufaturerName',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Medicines.Manufacturer', verbose_name='Manufacturer'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='subCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CategoryAndSubcategory.SubCategory', verbose_name='Sub Category'),
        ),
    ]
