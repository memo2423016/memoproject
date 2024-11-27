from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Category(models.Model):
    '''カテゴリ管理モデル
    '''
    title = models.CharField(verbose_name='カテゴリ', max_length=20)
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す{Returns(str):カテゴリ名}
        '''
        return self.title

class MemoPreserve(models.Model):
    '''メモデータ管理モデル
    '''
    #CustomUserモデル(のuser_id)と1対多の関係で結び付ける
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    #Categoryモデル(のtitle)と1対多の関係で結び付ける
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
    #タイトル用のフィールド
    title = models.CharField(verbose_name='タイトル', max_length=200)
    #メモ用のフィールド
    note = models.TextField(verbose_name='メモ')
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(verbose_name='投稿日時', auto_now_add=True)
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す{Returns(str):投稿記事のタイトル}
        '''
        return self.title
