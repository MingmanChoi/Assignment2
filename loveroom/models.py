from django.db import models
from datetime import datetime

#datetime.now()
# Create your models here.

Sex_Choice = (
    (1, "남성"),
    (2, "여성")
)

Num_Choice = (
    (1, "2:2"),
    (2, "3:3"),
    (3, "4:4"),
    (4, "5:5"),
    (5, "기타"),
)

Cam_Choice = (
    (1, "명륜"),
    (2, "율전"),
    (3, "기타")
)
class Room(models.Model):
    sex = models.IntegerField(choices=Sex_Choice, default=1)
    num_people = models.IntegerField(choices=Num_Choice, default=1)
    campus = models.IntegerField(choices=Cam_Choice, default=1)
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:40]

class Comment(models.Model):
    content = models.CharField(max_length=200)
    userid = models.CharField(max_length=50)
    write_date = models.DateTimeField('date published')

    def __str__(self):
        return self.userid