from django.db import models

class Hall(models.Model):      #For Every Hall I have its Condition/Status.
    name=models.CharField(max_length=200,primary_key = True,blank=False)
    maxcapacity=models.IntegerField()
    vacancy=models.IntegerField()

    def __str__(self):
        return self.name


class Condition(models.Model):
    hall=models.ForeignKey(Hall,on_delete=models.CASCADE,related_name="condition")
    day=models.DateField(auto_now_add=False)
    time = models.TimeField(auto_now_add=False)
    status=models.CharField(max_length=200,default="available")
    mems=models.IntegerField(default=0)


    def __str__(self):
        return self.status
