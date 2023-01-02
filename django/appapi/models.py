from django.db import models
import uuid

# Create your models here.
class RasPi(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    individual_id = models.CharField(max_length=5, unique=True)
    mac_address = models.SlugField(max_length=17)
    in_use = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return str(self.individual_id)
    
    class Meta:
        verbose_name_plural = "RaspberryPi識別"


class User(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=10, verbose_name="ユーザー名")
    email_address = models.EmailField(unique=True, verbose_name="メールアドレス")
    # TODO: パスワードをハッシュ化する
    hash_password = models.CharField(max_length=254, verbose_name="パスワード")
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "ユーザー管理"


class UserBottle(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=50, verbose_name="ボトル名")
    product_name = models.CharField(max_length=50, verbose_name="商品名")
    user_id = models.ForeignKey('User', on_delete=models.PROTECT, verbose_name="ユーザーID")
    raspi_id = models.ForeignKey('RasPi', on_delete=models.PROTECT, verbose_name="ラズパイID")
    bottle_type_id = models.ForeignKey('BottleType', on_delete=models.PROTECT, verbose_name="種類ID", null=True)
    container_id = models.ForeignKey('Container', on_delete=models.PROTECT, verbose_name ="容器ID")
    bottle_volume = models.PositiveSmallIntegerField()
    remaining_quantity = models.PositiveSmallIntegerField()
    is_favorite = models.BooleanField(default=False, verbose_name='お気に入り')
    memo = models.TextField(null=True, blank=True,verbose_name='メモ')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return str(self.user_id) + "：" + self.name

    class Meta:
        verbose_name_plural = "ボトル情報"


class BottleType(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=10, unique=True, verbose_name="ボトルの種類")
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural = "ボトルの種類"



class Container(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=10, unique=True, verbose_name="容器の種類")
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "容器"


class ContainerImage(models.Model):
    container_id = models.ForeignKey('Container',  on_delete = models.PROTECT, verbose_name ="容器ID")
    quantity = models.PositiveSmallIntegerField()
    container_image = models.CharField(max_length=30, verbose_name="画像のファイル名")
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return str(self.container_id) + "：" +  str(self.quantity)
    
    class Meta:
        verbose_name_plural = "容器画像"