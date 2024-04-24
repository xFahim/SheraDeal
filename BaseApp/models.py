from django.db import models

class Gadget_Data(models.Model):
    gadget_id = models.AutoField(primary_key=True)
    category = models.TextField()
    product_url = models.TextField()
    name = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    InStock = models.BooleanField()
    LastUpdate = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Gadget_keywords(models.Model):
    Gadget_id = models.ForeignKey(Gadget_Data, on_delete=models.CASCADE)
    Keyword = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name


class Location(models.Model):
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.TextField(unique=True)
    email = models.EmailField(unique=True)
    full_name = models.TextField()
    location = models.OneToOneField(Location, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

class customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

class Phone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name
    
class Feedback(models.Model):
    Gadget_id = models.ForeignKey(Gadget_Data, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Feedback = models.TextField()
    rating = models.SmallIntegerField()

    def __unicode__(self):
        return self.name

class Website_Source(models.Model):
    web_id = models.AutoField(primary_key=True)
    name = models.TextField()
    url = models.URLField()
    GadgetID = models.ForeignKey(Gadget_Data, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.name

class WishList(models.Model):
    list_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    Description = models.TextField()
    customer_id = models.ForeignKey(customer, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

class Outlet(models.Model):
    web_id = models.ForeignKey(Website_Source, on_delete=models.CASCADE)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return self.name