from django.db import models
from django.contrib.admin.models import User


class Currency(models.Model):
    """
    Currency model represents the different currencies available in the sysmte
    """

    name = models.CharField(max_length=20)
    code = models.CharField(max_length=3)
    symbol = models.CharField(max_length=1, null=True)

    def __unicode__(self):
        return self.name + ' ' + (self.code)


class Rate(models.Model):
    """
    This model is responsible for keeping info about the latest rates given
    a sell and buy currencies
    """

    date = models.DateField()
    value = models.FloatField()
    sell_ccy = models.ForeignKey(Currency, related_name='fk_sell_ccy')
    buy_ccy = models.ForeignKey(Currency, related_name='fk_buy_ccy')

    class Meta:
        get_latest_by = ['date']

    def __unicode__(self):
        return "%s to %s -> %s" %(self.sell_ccy.code, self.buy_ccy.code, self.value)


class Log(models.Model):
    """
    Log model provides with a tracking of every exchange ever made in the system.
    It tracks the date, sell and buy currencies and amounts, as well as the user who
    requested the exchange and the rate value
    """

    date = models.DateField(auto_now_add=True)
    sell_amount = models.FloatField()
    sell_ccy = models.ForeignKey(Currency, related_name='fk_sell_ccy_log')
    buy_amount = models.FloatField()
    buy_ccy = models.ForeignKey(Currency, related_name='fk_buy_ccy_log')
    rate = models.ForeignKey(Rate, null=True)
    user = models.ForeignKey(User, null=True)

    class Meta:
        ordering = ['date']

    def __unicode__(self):
        return "%s: %s %s -> %s %s. Rate: %s. User: %s" % (self.date, self.sell_ccy.code, self.sell_amount, self.buy_ccy.code, self.buy_amount, self.rate.value, self.user)
