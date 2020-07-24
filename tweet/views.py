from django.views.generic import ListView
from .models import Post
# Create your views here.

class PostListView(ListView):
    model = Post #対象モデル
    template_name = "tweet/index.html" #テンプレの場所
    context_object_name = 'posts' #
    ordering = ['-date_posted'] #表示順位 -> '-date_posted'とすると昇順となる。
    paginate_by = 5 #ページネ-ション