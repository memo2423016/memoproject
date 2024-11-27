from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import MemoPreserveForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import MemoPreserve
from accounts.models import CustomUser

# Create your views here.
class LogoutpageView(TemplateView):
    template_name = 'base_logout.html'

class IndexView(ListView):
    template_name = 'index.html'
    paginate_by = 9

    def get_queryset(self):
        #ログインユーザーで絞り込み
        current_user = self.request.user.username
        user_data = CustomUser.objects.get(username=current_user)
        if user_data:
            queryset = MemoPreserve.objects.filter(user=user_data).all()
            queryset = queryset.order_by('-posted_at')
        return queryset

#アクセスをログインユーザーに限定　ログイン状態でなければsettings.pyのLOGIN_URLにリダイレクトされる
@method_decorator(login_required, name='dispatch')
class CreateMemoView(CreateView):
    '''メモ作成ページのビュー
    '''
    form_class = MemoPreserveForm
    template_name = "preserve_memo.html"
    success_url = reverse_lazy('memo:preserve_done')

    def form_valid(self, form):
        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class PreserveSuccessView(TemplateView):
    '''作成完了ページのビュー
    '''
    template_name ='preserve_success.html'

@method_decorator(login_required, name='dispatch')
class CategoryView(ListView):
    '''カテゴリページのビュー
    '''
    template_name ='index.html'
    paginate_by = 9

    def get_queryset(self):
        #ログインユーザーとカテゴリのidで絞り込み
        current_user = self.request.user.username
        user_data = CustomUser.objects.get(username=current_user)
        category_id = self.kwargs['category']
        categories = MemoPreserve.objects.filter(user=user_data, category=category_id)
        categories = categories.order_by('-posted_at')
        return categories

@method_decorator(login_required, name='dispatch')
class DetailView(DetailView):
    '''詳細ページのビュー
    '''
    template_name ='detail.html'
    model = MemoPreserve

@method_decorator(login_required, name='dispatch')
class MemoDeleteView(DeleteView):
    '''レコードの削除を行うビュー
    '''
    model = MemoPreserve
    template_name ='memo_delete.html'
    success_url = reverse_lazy('memo:delete_done')

    def delete(self, request, *args, **kwargs):
      # スーパークラスのdelete()を実行
      return super().delete(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class DeleteSuccessView(TemplateView):
    '''削除完了ページのビュー
    '''
    template_name ='delete_success.html'

@method_decorator(login_required, name='dispatch')
class UpdateMemoView(UpdateView):
    model = MemoPreserve
    template_name = 'update_memo.html'
    form_class = MemoPreserveForm

    def get_success_url(self):
        return reverse_lazy('memo:memo_detail', kwargs={'pk':self.kwargs['pk']})