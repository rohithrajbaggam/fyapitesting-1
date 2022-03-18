# Generated by Django 4.0.3 on 2022-03-18 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, default='profile_default.jpeg', upload_to='profile_pics')),
                ('dob', models.DateField(blank=True, null=True)),
                ('full_name', models.CharField(max_length=55)),
                ('Section', models.CharField(blank=True, max_length=100)),
                ('Branch', models.CharField(choices=[('Bachelor of Computer Science Engineering', 'Bachelor of Computer Science Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Electrical and Electronics Engineering', 'Electrical and Electronics Engineering'), ('Electronics and Communications Engineering', 'Electronics and Communications Engineering'), ('Aerospace Engineering', 'Aerospace Engineering'), ('Aeronautical Engineering', 'Aeronautical Engineering'), ('Bachelor of Business Administration', 'Bachelor of Business Administration'), ('Master of Business Administration', 'Master of Business Administration'), ('Hotel Management', 'Hotel Management'), ('Agricultural Science', 'Agricultural Science'), ('Biotechonology', 'Biotechonology'), ('Chemical Engineering', 'Chemical Engineering'), ('Fashion Techonology', 'Fashion Techonology'), ('Master of Business Administration', 'Master of Business Administration'), (None, 'None')], default='None', max_length=100)),
                ('year_joined', models.CharField(choices=[('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021')], max_length=5)),
                ('Hosteler_or_DayScholar', models.CharField(blank=True, choices=[(None, 'None'), ('Home', 'Day Scholar'), ('Pg', 'Pg'), ('Shukuna 1', 'Shukuna 1'), ('Shukuna 2', 'Shukuna 2'), ('Govind 1', 'Govind 1'), ('Govind 2', 'Govind 2'), ('LC1', 'NC 1'), ('LC2', 'NC 2'), ('LC3', 'NC 3'), ('LC4', 'NC 4'), ('NC1', 'NC 1'), ('NC2', 'NC 2'), ('NC3', 'NC 3'), ('NC4', 'NC 4'), ('NC5', 'NC 5'), ('NC6', 'NC 6'), ('Tagore', 'Tagore'), ('Zakir A', 'Zakir A'), ('Zakir B', 'Zakir B')], default='None', max_length=100)),
                ('Hostel_Room_No', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('bio', models.TextField(blank=True)),
                ('Native_Language', models.CharField(max_length=10)),
                ('Languages_Known', models.CharField(max_length=100)),
                ('Address', models.TextField(blank=True, default=None, null=True)),
                ('State', models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh ', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir ', 'Jammu and Kashmir '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], max_length=255, null=True)),
                ('foreigners_can_enter_their_states_here', models.CharField(blank=True, max_length=100)),
                ('Country', models.CharField(default='India', max_length=20)),
                ('whatsapp', models.CharField(blank=True, max_length=10)),
                ('instagram_username', models.CharField(blank=True, max_length=50)),
                ('facebook', models.URLField(blank=True)),
                ('linkdin_profile_link', models.URLField(blank=True)),
                ('gmail', models.EmailField(blank=True, max_length=254)),
                ('users', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
