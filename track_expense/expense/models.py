from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
        #Creating one to one relationship with user model
        user = models.OneToOneField(settings.AUTH_USER_MODEL)
        #null is True related to default null in db
        #blank is True related to form validation,field can be left blank in form
        date_of_birth = models.DateField(blank=True, null=True)
        #defining the image field
        photo = models.ImageField(upload_to='users/%Y/%m/%d',
                                  blank=True)
        #The below method is for human readable representaion of an object
        #Here we are represtig user object
        def __str__(self):
                return 'Profile for user {}'.format(self.user.username)
 
#Creating a Expense Model 
class Expense(models.Model):
        #User who creates expense
        user_tar = models.ForeignKey(to=User, related_name="bets", blank=True, null=True)
        expense_name=models.CharField(max_length=250)
        #Creating a text area filed for description
        expense_description=models.TextField(max_length=1024*2)
        price=models.FloatField(null=True, blank=True)
        #Upload image to specific direactory based on date
        expense_image = models.ImageField(upload_to='images/%Y/%m/%d',
                                  blank=True)
        created = models.DateTimeField(auto_now_add=True)
        def __str__(self):
            return self.expense_name