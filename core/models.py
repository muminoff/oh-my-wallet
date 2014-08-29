from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=20,
        unique=True,
        db_index=True
    )

    created = models.DateField(
        auto_now_add=True
    )

    modified = models.DateField(
        auto_now=True
    )

    def __unicode__(self):
        return u'{0}'.format(self.name)

    class Meta:
        db_table = 'categories'


class Expense(models.Model):
    name = models.CharField(max_length=50)

    category = models.ForeignKey(
        Category,
        related_name='expense_category',
        db_index=True
    )

    amount = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=8,
        decimal_places=0
    )

    paid = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        editable=False
    )

    class Meta:
        db_table = 'expenses'

    @property
    def get_sum(self):
        return self.price * self.amount

    def __unicode__(self):
        return u'{0}'.format(self.name)
