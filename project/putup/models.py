from django.conf import settings
from django.db import models
from django.utils import timezone

class Item(models.Model):
    ITEM_CONDITION = (
        ('new','新品'),
        ('like_new','新古品'),
        ('used_better','良中古品'),
        ('used_worse','悪中古品'),
        ('junk','ジャンク品'),
    )
    
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,verbose_name="出品者名")
    title = models.CharField(max_length=200, verbose_name="商品名")
    description = models.TextField(max_length=2000,verbose_name="商品説明")
    image = models.ImageField(upload_to='images',blank=True, null=True, verbose_name="商品画像")
    start_price = models.PositiveIntegerField(default=0,verbose_name="開始価格")
    condition = models.CharField(choices=ITEM_CONDITION, verbose_name="商品状態")
    created_date = models.DateTimeField(default=timezone.now,verbose_name="出品日")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title