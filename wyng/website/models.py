from django.db import models

class prod_mst(models.Model):
    Product_Code  = models.CharField(max_length=20)

    def __str__(self):
        return self.Product_Code

class whs_mst(models.Model):
    WH = models.CharField(max_length=20)

class stg_mst(models.Model):
    Store_Code = models.CharField(max_length=20)

class whs_stg(models.Model):
    WH = models.ManyToManyField('whs_mst', related_name="storage")
    Store_Code = models.ManyToManyField('stg_mst', related_name="storage")


class whs_inventory(models.Model):
    Product_Code = models.ManyToManyField('prod_mst', related_name="product")
    Store_Code = models.ManyToManyField('stg_mst', related_name="product")
    Date = models.DateField()

class stg_inventory(models.Model):
    Store_Code = models.ManyToManyField('stg_mst', related_name="warehouse")
    Product_Code = models.ManyToManyField('prod_mst', related_name="warehouse")
    Closing_Inventory = models.IntegerField()
    Date = models.DateField()

class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    birth_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)

class replenishment(models.Model):
    WH = models.ManyToManyField('whs_mst', related_name="replenishment")
    Store_Code = models.ManyToManyField('stg_mst', related_name="replenishment")
    Product_Code = models.ManyToManyField('prod_mst', related_name="replenishment")
    repl_qty = models.IntegerField()

class required_qty(models.Model):
    Product_Code = models.ManyToManyField('prod_mst', related_name="requiredqty")
    short_qty = models.IntegerField()



