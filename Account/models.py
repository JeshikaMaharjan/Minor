from django.db import models


class Roles(object):
  ADMIN = 1
  STAFF = 2
  STUDENT = 3

class User(models.Model):
  userName = models.CharField(max_length=100, unique=True)
  firstName = models.CharField(max_length=100)
  lastName = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  role = models.IntegerField(null=True)
  
# class Fee(models.Model):
#   student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_fee")
#   totalFee = models.FloatField()
#   admissionFee = models.FloatField()
#   firstSem = models.FloatField()
#   secondSem = models.FloatField()
#   thirdSem = models.FloatField()
#   fourthSem = models.FloatField()
#   fifthSem = models.FloatField()
#   sixthSem = models.FloatField()
#   seventhSem = models.FloatField()
#   eighthSem = models.FloatField()
#   scholarship = models.FloatField(null=True)
  
# # # payment model
# class Payment(models.Model):
#   student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_scholarship")
#   payment = models.FloatField()

# f'select * from User where role = {Roles.STUDENT}
#query ma garni minus