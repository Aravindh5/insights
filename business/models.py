from django.db import models


# Create your models here.
class Userprofiles(models.Model):

    s_no = models.AutoField(db_column='S.No', primary_key=True)  # Field name made lowercase. Field renamed to
    #                                                              remove unsuitable characters.
    usertoken = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserToken')  # Field name made lowercase.
    profileid = models.CharField(db_column='ProfileID', max_length=7)  # Field name made lowercase.
    profilename = models.CharField(db_column='ProfileName', max_length=50)  # Field name made lowercase.
    masterflag = models.CharField(db_column='MasterFlag', max_length=2)  # Field name made lowercase.
    dateofbirth = models.DateTimeField(db_column='DateOfBirth')  # Field name made lowercase.
    birthlatitude = models.FloatField(db_column='BirthLatitude')  # Field name made lowercase.
    birthlongitude = models.FloatField(db_column='BirthLongitude')  # Field name made lowercase.
    birthoffset = models.FloatField(db_column='BirthOffset')  # Field name made lowercase.
    otherdetail1 = models.CharField(db_column='OtherDetail1', max_length=50)  # Field name made lowercase.
    otherdetail2 = models.CharField(db_column='OtherDetail2', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userprofiles'


class Users(models.Model):

    s_no = models.AutoField(db_column='S.No', primary_key=True)  # Field name made lowercase. Field renamed to remove
    #                                            unsuitable characters.
    username = models.CharField(db_column='UserName', max_length=50)  # Field name made lowercase.
    usertoken = models.CharField(db_column='UserToken', max_length=7)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.
    dateofbirth = models.DateTimeField(db_column='DateOfBirth')  # Field name made lowercase.
    birthlocation = models.CharField(db_column='BirthLocation', max_length=50)  # Field name made lowercase.
    birthlatitude = models.CharField(db_column='BirthLatitude', max_length=50)  # Field name made lowercase.
    birthlongitude = models.CharField(db_column='BirthLongitude', max_length=50)  # Field name made lowercase.
    birthoffset = models.IntegerField(db_column='BirthOffset')  # Field name made lowercase.
    primarylocation = models.CharField(db_column='PrimaryLocation', max_length=50)  # Field name made lowercase.
    primarylatitude = models.FloatField(db_column='PrimaryLatitude')  # Field name made lowercase.
    primarylongitude = models.FloatField(db_column='PrimaryLongitude')  # Field name made lowercase.
    primaryoffset = models.IntegerField(db_column='PrimaryOffset')  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
        constraints = [
            models.UniqueConstraint(
                fields=('s_no', 'usertoken'), name='unique_migration_host_combination'
            )
        ]


class UsersSnsTable(models.Model):

    s_no = models.AutoField(db_column='S.No', primary_key=True)   # Field name made lowercase. Field renamed to remove unsuitable characters.
    usertoken = models.CharField(db_column='UserToken', max_length=7)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    firebasetoken = models.TextField(db_column='FirebaseToken')  # Field name made lowercase.
    amazonarn = models.TextField(db_column='AmazonARN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_sns_table'


class Languagetable(models.Model):

    s_no = models.AutoField(db_column='S.No', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    messageid = models.IntegerField(db_column='MessageID')  # Field name made lowercase.
    messageen = models.TextField(db_column='MessageEN')  # Field name made lowercase.
    messagehi = models.TextField(db_column='MessageHI')  # Field name made lowercase.
    messagege = models.TextField(db_column='MessageGE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'languagetable'
