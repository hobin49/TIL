from django import forms
from .models import Article

# forms 정의
class ArticleForm(forms.ModelForm):
    class meta:
        model = Article
        # 모든 데이터 사용
        field = "__all__"
