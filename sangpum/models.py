from django.db import models

# Create your models here.

class Maker(models.Model):
    mname = models.CharField(max_length=10)
    tel = models.CharField(max_length=30)
    addr = models.CharField(max_length=50)
    
    class Meta:
        ordering = ('-id',)
        
    def __str__(self):
        return self.mname # 이게 있어야 admin사이트에서 product 정보추가할때 maker_name에  mname이 나온다. 
                            # 안쓰면 이름대신 숫자로 나온다.
class Product(models.Model):
    pname = models.CharField(max_length=10)
    price = models.IntegerField()
    maker_name = models.ForeignKey(Maker, on_delete=models.CASCADE) # fk의 대상은 Maker의 pk
    
    
    