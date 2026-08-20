from django.db import models

#Book model
class Book(models.Model):
    book_title = models.CharField(
        max_length=255,
        unique=True,
        help_text="Book title"
    )
    book_isbn = models.CharField(
        max_length=17,
        unique=True,
        help_text="17 character International Standard Book Number"
    )

class Church(models.Model):
    church_name = models.CharField(
        max_length=255,
        help_text="Church Name"
    )
    church_times = models.CharField(
        max_length=255
    )

class MortgagePool(models.Model):
    pool_name = models.CharField(
        max_length=200,
    )
    pool_number = models.CharField(
        max_length=200,
    )
    # Stores values up to (2 total digits minus 2 decimal places)
    expected_yield = models.DecimalField(
    max_digits=5,
    decimal_places=2,
    )
    def __str__(self):
        return f"{self.pool_number} - {self.pool_name} - {self.expected_yield}"


class SIRRScenario(models.Model):
    product_name = models.CharField(max_length=100)
    coupon_rate = models.DecimalField(max_digits=5,decimal_places=2)
    funding_cost = models.DecimalField(max_digits=5,decimal_places=2)
    credit_loss = models.DecimalField(max_digits=5, decimal_places=2)
    servicing_cost = models.DecimalField(max_digits=5, decimal_places=2)
    target_margin = models.DecimalField(max_digits=5, decimal_places=2)


class Library(models.Model):
    state = models.CharField
