from django.db import models


class Persons(models.Model):
    personId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics', blank=True)
    bivag = (
            ('Dhaka', 'Dhaka'),
            ('Khulna', 'Khulna'),
            ('Chattogram', 'Chattogram'),
            ('Barishal', 'Barishal'),
            ('Syhlet', 'Syhlet'),
            ('Rajshahi', 'Rajshahi'),
            ('Rangpur', 'Rangpur'),
            ('Mymensingh', 'Mymensingh'),
    )
    division = models.CharField(max_length=100, choices=bivag, blank=True)

    zilla = (
            ('Barguna', 'Barguna'),
            ('Barishal', 'Barishal'),
            ('Bhola', 'Bhola'),
            ('Jhalokati', 'Jhalokati'),
            ('Patuakhali', 'Patuakhali'),
            ('Pirojpur', 'Pirojpur'),
            ('Bandarban', 'Bandarban'),
            ('Brahmanbaria', 'Brahmanbaria'),
            ('Chandpur', 'Chandpur'),
            ('Chattogram', 'Chattogram'),
            ('Cumilla', 'Cumilla'),
            ("Cox's Bazar", "Cox's Bazar"),
            ('Feni', 'Feni'),
            ('Khagrachhari', 'Khagrachhari'),
            ('Lakshmipur', 'Lakshmipur'),
            ('Noakhali', 'Noakhali'),
            ('Rangamati', 'Rangamati'),
            ('Dhaka', 'Dhaka'),
            ('Faridpur', 'Faridpur'),
            ('Gazipur', 'Gazipur'),
            ('Gopalganj', 'Gopalganj'),
            ('Kishoreganj', 'Kishoreganj'),
            ('Madaripur', 'Madaripur'),
            ('Manikganj', 'Manikganj'),
            ('Munshiganj', 'Munshiganj'),
            ('Narayanganj', 'Narayanganj'),
            ('Narsingdi', 'Narsingdi'),
            ('Rajbari', 'Rajbari'),
            ('Shariatpur', 'Shariatpur'),
            ('Tangail', 'Tangail'),
            ('Bagerhat', 'Bagerhat'),
            ('Chuadanga', 'Chuadanga'),
            ('Jashore', 'Jashore'),
            ('Jhenaidah', 'Jhenaidah'),
            ('Khulna', 'Khulna'),
            ('Kushtia', 'Kushtia'),
            ('Magura', 'Magura'),
            ('Meherpur', 'Meherpur'),
            ('Narail', 'Narail'),
            ('Satkhira', 'Satkhira'),
            ('Jamalpur', 'Jamalpur'),
            ('Mymensingh', 'Mymensingh'),
            ('Netrokona', 'Netrokona'),
            ('Sherpur', 'Sherpur'),
            ('Bogura', 'Bogura'),
            ('Joypurhat', 'Joypurhat'),
            ('Naogaon', 'Naogaon'),
            ('Natore', 'Natore'),
            ('Chapainawabganj', 'Chapainawabganj'),
            ('Pabna', 'Pabna'),
            ('Rajshahi', 'Rajshahi'),
            ('Sirajganj', 'Sirajganj'),
            ('Dinajpur', 'Dinajpur'),
            ('Gaibandha', 'Gaibandha'),
            ('Kurigram', 'Kurigram'),
            ('Lalmonirhat', 'Lalmonirhat'),
            ('Nilphamari', 'Nilphamari'),
            ('Panchagarh', 'Panchagarh'),
            ('Rangpur', 'Rangpur'),
            ('Thakurgaon', 'Thakurgaon'),
            ('Habiganj', 'Habiganj'),
            ('Moulvibazar', 'Moulvibazar'),
            ('Sunamganj', 'Sunamganj'),
            ('Sylhet', 'Sylhet'),
    )
    district = models.CharField(max_length=100, choices=zilla, blank=True)
    upozila = models.CharField(max_length=100, blank=True)
    village = models.CharField(max_length=100, blank=True)

    address = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField()
    #age = models.IntegerField()
    is_married = (
        ('Married', 'Married'),
        ('Unmarried', 'Unmarried'),
        ('Divorced', 'Divorced'),
    )
    marital_status = models.CharField(
        max_length=100, choices=is_married, blank=True)
    nid_bid = models.CharField(max_length=50, blank=True)
    dna_sample_id = models.CharField(max_length=100, blank=True)
    date_created = models.DateField()
    is_late = models.BooleanField(default=False, blank=True)

    class Meta:
        unique_together = (("nid_bid", "dna_sample_id"),)
        ordering = ('division', 'district', 'marital_status',)

    def __str__(self):
        return self.name
