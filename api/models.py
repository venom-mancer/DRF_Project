from django.db import models


class TblProduct(models.Model):

    title = models.CharField(max_length=120)
    content = models.TextField(blank=True , null=True)
    price = models.DecimalField(max_digits=15,decimal_places=2,default=99.99)

    @property
    def sell_price(self):
        return "{}".format(float(self.price)*0.8)
    
    def get_discount(self):
        return "120"

