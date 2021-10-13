from django.shortcuts import render
from . forms import KakeiboForm  #forms .pyからKakeiboFormをインポート
from django.urls import reverse_lazy # url遷移
# Create your views here.
# ここから下を追加

# CRUDに対応するDjango標準の汎用ビュー
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
# models.pyで定義されているCategory,KakeiboテーブルクラスをImport
from .models import Category, Kakeibo

# 一覧表示用のDjango標準ビュー(ListView)を承継して一覧表示用のクラスを定義


class KakeiboListView(ListView):
    # 利用するモデルを指定 import
    model = Kakeibo
    # データを渡すテンプレートファイルを指定
    # C:\django\tutorial\kakeibo\templates\kakeibo\kakeibo_list.html
    template_name = 'kakeibo/kakeibo_list.html'

    # 家計簿テーブルの全データを取得するメソッドを定義
    def queryset(self):
        return Kakeibo.objects.all()

    # 特定条件に一致する複数レコードを取得したい場合は[modelクラス名].objects.filter([カラム名]= ‘値’)

class KakeiboCreateView(CreateView):

    #利用するモデルを指定
    model = Kakeibo
    #利用するフォームクラス名を指定 forms.py
    form_class = KakeiboForm
    #登録処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('kakeibo:create_done')

def create_done(request):
   #登録処理が正常終了した場合に呼ばれるテンプレートを指定
   return render(request, 'kakeibo/create_done.html')

class KakeiboUpdateView(UpdateView):
    #利用するモデルを指定
    model = Kakeibo
    #利用するフォームクラス名を指定
    form_class = KakeiboForm
    #登録処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('kakeibo:update_done')


def update_done(request):
    #更新処理が正常終了した場合に呼ばれるテンプレートを指定
    return render(request, 'kakeibo/update_done.html')

class KakeiboDeleteView(DeleteView):

    #利用するモデルを指定
    model = Kakeibo
    #削除処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('kakeibo:delete_done')

def delete_done(request):

    return render(request, 'kakeibo/delete_done.html')