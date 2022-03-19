from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    Hosteler_or_DayScholar_Choices = [
    (None, 'None'),
    ('Home', 'Day Scholar'),
    ('Pg', 'Pg'),
    ('Shukuna 1', 'Shukuna 1'),
    ('Shukuna 2', 'Shukuna 2'),
    ('Govind 1', 'Govind 1'),
    ('Govind 2', 'Govind 2'),
    ('LC1', 'NC 1'),
    ('LC2', 'NC 2'),
    ('LC3', 'NC 3'),
    ('LC4', 'NC 4'),
    ('NC1', 'NC 1'),
    ('NC2', 'NC 2'),
    ('NC3', 'NC 3'),
    ('NC4', 'NC 4'),
    ('NC5', 'NC 5'),
    ('NC6', 'NC 6'),
    ('Tagore', 'Tagore'),
    ('Zakir A', 'Zakir A'),
    ('Zakir B', 'Zakir B'),
    ]
    Branch_Choice = [ 
        ('Bachelor of Computer Science Engineering', 'Bachelor of Computer Science Engineering'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
        ('Electrical and Electronics Engineering', 'Electrical and Electronics Engineering'),
        ('Electronics and Communications Engineering', 'Electronics and Communications Engineering'),
        ('Aerospace Engineering', 'Aerospace Engineering'),
        ('Aeronautical Engineering', 'Aeronautical Engineering'),
        ('Bachelor of Business Administration', 'Bachelor of Business Administration'),
        ('Master of Business Administration', 'Master of Business Administration'),
        ('Hotel Management', 'Hotel Management'),
        ('Agricultural Science', 'Agricultural Science'),
        ('Biotechonology', 'Biotechonology'),
        ('Chemical Engineering', 'Chemical Engineering'),
        ('Fashion Techonology', 'Fashion Techonology'),
        ('Master of Business Administration', 'Master of Business Administration'),
        (None, 'None'),
    ]
    state_choices = [("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh"),("Assam","Assam"),("Bihar","Bihar"),
    ("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),
    ("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),(
        "Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),
        ("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),
        ("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),
        ("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),(
            "Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),
            ("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry")]
    year = [  
        ('2012', '2012'),
        ('2013', '2013'),
        ('2014', '2014'),
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, default='user_profile_default.png')
    dob = models.DateField(blank=True, null=True)
    full_name = models.CharField(max_length=55)
    Section     = models.CharField(max_length=100, blank=True)
    Branch     = models.CharField(max_length=100, choices=Branch_Choice, default='None') 
    year_joined = models.CharField(max_length=5, choices=year )
    Hosteler_or_DayScholar  = models.CharField(max_length=100, choices=Hosteler_or_DayScholar_Choices, default='None', blank=True)
    Hostel_Room_No   = models.PositiveIntegerField(default=None,blank=True, null=True)
    bio = models.TextField(blank=True)

    Native_Language = models.CharField(max_length=10)#mandatory # add languages functionality for next update
    Languages_Known = models.CharField(max_length=100)
# add languages functionality for next update
    Address     = models.TextField(default=None, blank=True, null=True)
    State = models.CharField(choices=state_choices,max_length=255, null=True, blank=True)
    foreigners_can_enter_their_states_here = models.CharField(max_length=100, blank=True)
    Country     = models.CharField(max_length=20, default='India')

    whatsapp = models.CharField(max_length=10, blank=True) 
    instagram_username = models.CharField(max_length=50 ,blank = True)
    facebook = models.URLField(blank = True)
    linkdin_profile_link = models.URLField(blank = True)
    gmail = models.EmailField(blank=True)
    
    def __str__(self):
        return self.full_name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="user_posts", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}'