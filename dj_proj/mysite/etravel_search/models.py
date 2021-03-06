from django.db import models

class Search(models.Model):
    From=models.CharField(max_length=200)
    To=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    def __str__(self):
        return str(self.To)+' '+str(self.From)+' '+str(self.date)

class Bus(models.Model):
    bus_name=models.CharField(max_length=250)
    bus_type=models.CharField(max_length=200)
    dep_time=models.CharField(max_length=10)
    arr_time=models.CharField(max_length=10)
    travel_time=models.CharField(max_length=50)
    ratings=models.CharField(max_length=200)
    seats=models.CharField(max_length=10)
    price=models.CharField(max_length=200)

    def __str__(self):
        return self.bus_name+' '+self.bus_type+' '+self.dep_time+' '+self.arr_time+' '+self.travel_time+' '+self.ratings+' '+self.seats+' '+self.price

class User_Journey(models.Model):
    User_id=models.CharField(max_length=10)
    Journey_id=models.CharField(max_length=10)
    Session_id=models.BooleanField(default=False)

    def __str__(self):
        return str(self.User_id)+' '+str(self.Journey_id)+' '+str(self.Session_id)


class Passenger(models.Model):
    User_id=models.CharField(max_length=10)
    User_name=models.CharField(max_length=50)
    Credit=models.CharField(max_length=8)

    def __str__(self):
        return str(self.User_id)+' '+str(self.User_name)+' '+str(self.Credit)