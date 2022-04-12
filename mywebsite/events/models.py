from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=10)
    phone = models.CharField('Contact', max_length=11)
    web = models.URLField('Website')
    email = models.EmailField('E-mail')

    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField('E-mail')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_data = models.DateTimeField('Event Date', auto_now_add=True)
    # venue = models.CharField('Event Venue', max_length=120)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    imgsrc = models.CharField('Image Source', max_length=120, blank=True, null=True)
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField('Event Manager', max_length=120)
    description = RichTextField(blank=True, null=True)
    small_des = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name


class App(models.Model):
    AppBgColor = models.CharField('Card Background', max_length=30 , blank=True, null=True)
    AppName = models.CharField('Application Name', max_length=30)
    AppSmallDescription = models.TextField('App Small Description', max_length=120)
    AppImage = models.ImageField(upload_to='images', blank=True, null=True)
    AppLogo = models.ImageField(upload_to='images', blank=True, null=True)
    AppDescription = models.TextField('App Description', max_length=300)
    AppDevelopers = models.ManyToManyField(MyClubUser, blank=True)
    AppURL = models.URLField('App URL')
    AppMailID = models.EmailField('App Mail ID')

    def __str__(self):
        return self.AppName
