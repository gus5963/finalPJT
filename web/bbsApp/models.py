from django.db import models

# Create your models here.

class BbsUser(models.Model):
    userId = models.CharField(max_length=50, primary_key=True)
    userPwd = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)

    def __str__(self):
        return self.userId+"\t" +self.userPwd+"\t"+self.userName




class BbsList(models.Model):
    id = models.BigAutoField(primary_key = True)
    title = models.CharField(max_length=50)
    writer=models.CharField(max_length=50)
    content=models.TextField(max_length=500)
    regdate=models.DateTimeField(auto_now=True)
    viewcnt=models.IntegerField(default=0)
