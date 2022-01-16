from django.conf import settings
from django.db import models
from django.utils import timezone

class Item(models.Model):
    ITEM_CONDITION = (
        ('新品','新品'),
        ('新古品','新古品'),
        ('良中古品','良中古品'),
        ('悪中古品','悪中古品'),
        ('ジャンク品','ジャンク品'),
    )
    
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="出品者名")
    title = models.CharField(max_length=200, blank=False, verbose_name="商品名")
    description = models.TextField(max_length=2000, verbose_name="商品説明")
    image = models.ImageField(upload_to='images/',blank=True, null=True, verbose_name="商品画像")
    # MEDIA_URLで指定したパスとuploads_toで指定したパスが連結してパスが生成される(/media/images)
    start_price = models.PositiveIntegerField(default=0, verbose_name="開始価格")
    condition = models.CharField(max_length=20, choices=ITEM_CONDITION, verbose_name="商品状態")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="出品日")
    # https://office54.net/python/django/model-field-options

    class Meta:
        # https://note.com/saito_pythonista/n/n2d02442ea1bf#jPuMt
        verbose_name = "商品"
        verbose_name_plural = verbose_name
        
    def created(self):
        self.created_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
    # 管理画面上のタイトルの判別が可能となる
    # https://office54.net/python/django/model-str-self