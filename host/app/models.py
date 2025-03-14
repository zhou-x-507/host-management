from django.db import models

# Create your models here.


class City(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment="id", verbose_name="id")
    name = models.CharField(max_length=200, null=True, blank=True, db_comment="城市名", verbose_name="城市名")

    class Meta:
        db_table_comment = "城市表"
        db_table = "app_city"
        verbose_name = "City"
        verbose_name_plural = verbose_name


class Datacenter(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment="id", verbose_name="id")
    name = models.CharField(max_length=200, null=True, blank=True, db_comment="机房名", verbose_name="机房名")
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.DO_NOTHING, db_comment="关联城市", db_constraint=False)

    class Meta:
        db_table_comment = "机房表"
        db_table = "app_datacenter"
        verbose_name = "Datacenter"
        verbose_name_plural = verbose_name


class Host(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment="id", verbose_name="id")
    ip_address = models.CharField(max_length=200, null=True, blank=True, db_comment="ip地址", verbose_name="ip地址")
    status = models.BigIntegerField(db_comment="状态", verbose_name="状态")
    datacenter = models.ForeignKey(Datacenter, null=True, blank=True, on_delete=models.DO_NOTHING, db_comment="关联机房", db_constraint=False)

    class Meta:
        db_table_comment = "主机表"
        db_table = "app_host"
        verbose_name = "Host"
        verbose_name_plural = verbose_name


class HostCount(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment="id", verbose_name="id")
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.DO_NOTHING, db_comment="关联城市", db_constraint=False)
    datacenter = models.ForeignKey(Datacenter, null=True, blank=True, on_delete=models.DO_NOTHING, db_comment="关联机房", db_constraint=False)
    count = models.IntegerField(null=True, blank=True, db_comment="主机数量", verbose_name="主机数量")
    create_datetime = models.DateTimeField(null=True, blank=True, verbose_name="创建时间", db_comment="创建时间")

    class Meta:
        db_table_comment = "主机数量表"
        db_table = "app_host_count"
        verbose_name = "Host Count"
        verbose_name_plural = verbose_name
