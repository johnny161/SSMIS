from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade_college_major=models.CharField(max_length=60, blank=True, null=True)
    realname = models.CharField(max_length=20, blank=True, null=True)

    def __unicode__(self):
        return self.user.username

    class Meta:
        db_table = 'Account'

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                p = Account.objects.get(user=self.user)
                self.pk = p.pk
            except Account.DoesNotExist:
                pass

        super(Account, self).save(*args, **kwargs)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Account()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)

class Tenant(models.Model):

    TYPE_CHOICES = {
        1: '公益类',
        2: '体育类',
        3: '公共传媒类',
        4: '艺术类',
        5: '科技类',
        6: '兴趣爱好类',
        7: '职业拓展类',
    }
    tenantid = models.AutoField( primary_key=True)  # Field name made lowercase.
    tenantcategory = models.SmallIntegerField(default=1, choices=TYPE_CHOICES.items())
    tenantname = models.CharField(u'社团名称',max_length=45)  # Field name made lowercase.
    tenantbelong = models.CharField(u'所属单位',max_length=20,)
    tenantcampus = models.CharField(u'所属校区',max_length=20,)
    tenantintroduction = models.TextField( u'社团简介',max_length=200)  # Field name made lowercase.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.tenantname


