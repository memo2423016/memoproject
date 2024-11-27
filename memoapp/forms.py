from django.forms import ModelForm
from .models import MemoPreserve

class MemoPreserveForm(ModelForm):
    class Meta:
        '''        
        Attributes:
          model: モデルのクラス
          fields: フォームで使用するモデルのフィールドを指定
        '''
        model = MemoPreserve
        fields = ['category', 'title', 'note']
