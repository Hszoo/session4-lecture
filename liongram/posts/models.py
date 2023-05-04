from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() # 이 함수 커스텀해서 사용한다. 위에 import해줘야됨 , 여기서 모델 생성하고 사용자와 연결한다고 생각  ㄴ
# Create your models here.

class Post(models.Model):
    image = models.ImageField(verbose_name='이미지', null=True, blank=True) # 필드에 대한 이름 지정 
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True) # 작성시 날짜 생성 
    view_count = models.IntegerField(verbose_name='조회수', default=True)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)

class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    content_at = models.DateTimeField(verbose_name='작성일')
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE) # FK Post에 대한 FK, 게시글 삭제시 연결된 댓글도 삭제 되도록 CASCADE
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)