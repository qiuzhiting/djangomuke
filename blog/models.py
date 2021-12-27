from django.db import models

# Create your models here.
class Article(models.Model):
    # 文章标题
    article_id = models.AutoField(primary_key=True);\
    # 文章标题
    title = models.TextField()
    # 文章摘要
    brief_content = models.TextField()
    #文章主要内容
    content = models.TextField()
    # 文章发布日期(未指定具体日期就使用当前日期作为发布日期)
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title