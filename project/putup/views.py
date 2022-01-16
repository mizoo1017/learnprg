from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.views import generic
from .forms import PutupForm
from .models import Item


def item(request):
    items = Item.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'putup/item.html/', {'items': items})

    # https://office54.net/python/django/views-render-how-to
    # render => request=セッション情報+requestの種類(get/post), template_name=表示するhtml, context=htmlに渡したいデータの集合

def detail(request, putup_id):
    detail = get_object_or_404(Item ,pk=putup_id)
    return render(request, 'putup/detail.html', {'detail': detail})

def new(request):
    if request.method == "POST":
        form = PutupForm(request.POST, request.FILES)
        if form.is_valid():
        # formに入力された値にエラーがないかバリデートする
        # https://teratail.com/questions/116711
            putup = form.save(commit=False)
            putup.seller = request.user
            putup.created_date = timezone.now()
            putup.save()
            return redirect('putup:item')
            # https://qiita.com/taole33/items/9a09b7bce0ee455d266f
    else:
        form = PutupForm()
    return render(request, 'putup/edit.html', {'form':form})
    フォームを保存
