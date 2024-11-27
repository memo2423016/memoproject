from django.urls import path
from . import views

#URLパターン逆引き用空間名
app_name = 'memo'

#URLパターン登録
urlpatterns = [
    #memoアプリへのアクセス
    path('', views.LogoutpageView.as_view(), name='logout_page'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('create_memo/', views.CreateMemoView.as_view(), name='create_memo'),

    #メモ作成完了ページへのアクセス
    path('preserve_done/', views.PreserveSuccessView.as_view(), name='preserve_done'),
    
    #カテゴリ一覧ページ
    path('memo/<int:category>/', views.CategoryView.as_view(), name = 'memo_cat'),
    
    # 詳細ページ
    path('memo-detail/<int:pk>/', views.DetailView.as_view(), name = 'memo_detail'),

    # 投稿写真の削除
    path('memo/<int:pk>/delete/', views.MemoDeleteView.as_view(), name = 'memo_delete'),

    #メモ削除完了ページへのアクセス
    path('delete_done/', views.DeleteSuccessView.as_view(), name='delete_done'),

    #メモの編集ページ
    path('update_memo/<int:pk>/', views.UpdateMemoView.as_view(), name='update_memo'),
]