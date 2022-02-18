# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Class(models.Model):
    course = models.CharField(primary_key=True, max_length=30)
    faculty = models.CharField(max_length=30, blank=True, null=True)
    teacher = models.CharField(max_length=30, blank=True, null=True)
    learningtime = models.IntegerField(blank=True, null=True)
    student = models.IntegerField(blank=True, null=True)
    class_last_update = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'class'


class Classroom(models.Model):
    classname = models.ForeignKey(Class, models.DO_NOTHING, db_column='classname')
    roomforclass_id = models.IntegerField(primary_key=True)
    classroom = models.ForeignKey('Laboratory', models.DO_NOTHING, db_column='classroom')

    class Meta:
        managed = True
        db_table = 'classroom'
        unique_together = (('roomforclass_id', 'classname', 'classroom'), ('roomforclass_id', 'classname', 'classroom'),)


class Configuration(models.Model):
    pcname = models.CharField(db_column='pcName', primary_key=True, max_length=30)  # Field name made lowercase.
    cpu = models.CharField(db_column='CPU', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mainboard = models.CharField(max_length=20, blank=True, null=True)
    memory = models.CharField(max_length=30, blank=True, null=True)
    harddisk = models.CharField(max_length=30, blank=True, null=True)
    vc = models.CharField(db_column='VC', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'configuration'


class Installing(models.Model):
    lab = models.ForeignKey('Laboratory', models.DO_NOTHING, db_column='lab')
    software = models.ForeignKey('Softwareinfo', models.DO_NOTHING)
    software_last_update = models.DateTimeField()
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'installing'


class Laboratory(models.Model):
    labname = models.CharField(db_column='labName', primary_key=True, max_length=20)  # Field name made lowercase.
    location = models.CharField(max_length=20, blank=True, null=True)
    manager = models.ForeignKey('Users', models.DO_NOTHING, db_column='manager', blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    computer = models.ForeignKey(Configuration, models.DO_NOTHING, db_column='computer', blank=True, null=True)
    lab_last_update = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'laboratory'


class Softwareinfo(models.Model):
    softwarename = models.CharField(db_column='softwareName', max_length=30)  # Field name made lowercase.
    category = models.CharField(max_length=20, blank=True, null=True)
    version = models.CharField(max_length=10, blank=True, null=True)
    architecture = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    soft_id = models.IntegerField(primary_key=True)
    size = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'softwareinfo'


class Softwareuse(models.Model):
    software_class = models.ForeignKey(Softwareinfo, models.DO_NOTHING)
    class_field = models.OneToOneField(Class, models.DO_NOTHING, db_column='class', primary_key=True)  # Field renamed because it was a Python reserved word.
    softuse_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'softwareuse'
        unique_together = (('class_field', 'software_class'), ('class_field', 'software_class'),)


class Users(models.Model):
    password = models.CharField(max_length=20)
    permission = models.IntegerField()
    user_id = models.CharField(primary_key=True, max_length=16)

    class Meta:
        managed = True
        db_table = 'users'
