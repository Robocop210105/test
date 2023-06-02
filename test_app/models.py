from django.db import models


class CreditApplication(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField('Product', through='ProdMTM')


class ProdMTM(models.Model):
    credit = models.ForeignKey(CreditApplication, on_delete=models.CASCADE, related_name='cred_prod')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='prod_cred')


class Contract(models.Model):
    name = models.CharField(max_length=100)
    credit_app = models.OneToOneField('CreditApplication', on_delete=models.PROTECT, related_name='credit_contract')
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Продукт')
    manufacturer_name = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, related_name='owner')
    created_at = models.DateTimeField(auto_now_add=True)


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Производитель')
    created_at = models.DateTimeField(auto_now_add=True)



