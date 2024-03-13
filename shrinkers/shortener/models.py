from django.db import models

# Create your models here.
# 1. 프로젝트 시작 시에 python manage.py migrate
# 2. 커스텀 모델 작성 후 python manage.py makemigrations
# 3. 다시 python manage.py


class PayPlan(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
