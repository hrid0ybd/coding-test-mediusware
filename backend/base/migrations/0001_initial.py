# Generated by Django 4.0 on 2021-12-25 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sku', models.SlugField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant_title', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('stock', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product')),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariantPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product')),
                ('product_variant_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variant_one', to='base.productvariant')),
                ('product_variant_three', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variant_three', to='base.productvariant')),
                ('product_variant_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variant_two', to='base.productvariant')),
            ],
        ),
        migrations.AddField(
            model_name='productvariant',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.variant'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.URLField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product')),
            ],
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('personId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='pics')),
                ('division', models.CharField(blank=True, choices=[('Dhaka', 'Dhaka'), ('Khulna', 'Khulna'), ('Chattogram', 'Chattogram'), ('Barishal', 'Barishal'), ('Syhlet', 'Syhlet'), ('Rajshahi', 'Rajshahi'), ('Rangpur', 'Rangpur'), ('Mymensingh', 'Mymensingh')], max_length=100)),
                ('district', models.CharField(blank=True, choices=[('Barguna', 'Barguna'), ('Barishal', 'Barishal'), ('Bhola', 'Bhola'), ('Jhalokati', 'Jhalokati'), ('Patuakhali', 'Patuakhali'), ('Pirojpur', 'Pirojpur'), ('Bandarban', 'Bandarban'), ('Brahmanbaria', 'Brahmanbaria'), ('Chandpur', 'Chandpur'), ('Chattogram', 'Chattogram'), ('Cumilla', 'Cumilla'), ("Cox's Bazar", "Cox's Bazar"), ('Feni', 'Feni'), ('Khagrachhari', 'Khagrachhari'), ('Lakshmipur', 'Lakshmipur'), ('Noakhali', 'Noakhali'), ('Rangamati', 'Rangamati'), ('Dhaka', 'Dhaka'), ('Faridpur', 'Faridpur'), ('Gazipur', 'Gazipur'), ('Gopalganj', 'Gopalganj'), ('Kishoreganj', 'Kishoreganj'), ('Madaripur', 'Madaripur'), ('Manikganj', 'Manikganj'), ('Munshiganj', 'Munshiganj'), ('Narayanganj', 'Narayanganj'), ('Narsingdi', 'Narsingdi'), ('Rajbari', 'Rajbari'), ('Shariatpur', 'Shariatpur'), ('Tangail', 'Tangail'), ('Bagerhat', 'Bagerhat'), ('Chuadanga', 'Chuadanga'), ('Jashore', 'Jashore'), ('Jhenaidah', 'Jhenaidah'), ('Khulna', 'Khulna'), ('Kushtia', 'Kushtia'), ('Magura', 'Magura'), ('Meherpur', 'Meherpur'), ('Narail', 'Narail'), ('Satkhira', 'Satkhira'), ('Jamalpur', 'Jamalpur'), ('Mymensingh', 'Mymensingh'), ('Netrokona', 'Netrokona'), ('Sherpur', 'Sherpur'), ('Bogura', 'Bogura'), ('Joypurhat', 'Joypurhat'), ('Naogaon', 'Naogaon'), ('Natore', 'Natore'), ('Chapainawabganj', 'Chapainawabganj'), ('Pabna', 'Pabna'), ('Rajshahi', 'Rajshahi'), ('Sirajganj', 'Sirajganj'), ('Dinajpur', 'Dinajpur'), ('Gaibandha', 'Gaibandha'), ('Kurigram', 'Kurigram'), ('Lalmonirhat', 'Lalmonirhat'), ('Nilphamari', 'Nilphamari'), ('Panchagarh', 'Panchagarh'), ('Rangpur', 'Rangpur'), ('Thakurgaon', 'Thakurgaon'), ('Habiganj', 'Habiganj'), ('Moulvibazar', 'Moulvibazar'), ('Sunamganj', 'Sunamganj'), ('Sylhet', 'Sylhet')], max_length=100)),
                ('upozila', models.CharField(blank=True, max_length=100)),
                ('village', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('date_of_birth', models.DateField()),
                ('marital_status', models.CharField(blank=True, choices=[('Married', 'Married'), ('Unmarried', 'Unmarried'), ('Divorced', 'Divorced')], max_length=100)),
                ('nid_bid', models.CharField(blank=True, max_length=50)),
                ('dna_sample_id', models.CharField(blank=True, max_length=100)),
                ('date_created', models.DateField()),
                ('is_late', models.BooleanField(blank=True, default=False)),
            ],
            options={
                'ordering': ('division', 'district', 'marital_status'),
                'unique_together': {('nid_bid', 'dna_sample_id')},
            },
        ),
    ]
