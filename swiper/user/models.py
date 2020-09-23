from django.db import models


# Create your models here.
class User(models.Model):
    '''User模型'''
    GENDER = (
        ('male', '男性'),
        ('female', '女性'),

    )
    LOCATION = (
        ('北京', '北京'),
        ('上海', '上海'),
        ('深圳', '深圳'),
        ('成都', '成都'),
        ('西安', '西安'),
        ('武汉', '武汉'),
        ('沈阳', '沈阳'),
    )
    nickname = models.CharField(max_length=16, unique=True, verbose_name='昵称')
    phonenum = models.CharField(max_length=32, unique=True, verbose_name='手机号')
    gender = models.CharField(max_length=10, choices=GENDER, verbose_name='性别')
    birthday = models.DateField(default='2002-01-01', verbose_name='出生日')
    avatar = models.ImageField(max_length=256, verbose_name='个人形象')
    location = models.CharField(max_length=64, choices=LOCATION, verbose_name='常居地')

    def to_dict(self):
        return {
            'id': self.id,
            'phonenum': self.phonenum,
            'nickname': self.nickname,
            'gender': self.gender,
            'birthday': str(self.birthday),
            'avatar': self.avatar,
            'location': self.location,
        }
