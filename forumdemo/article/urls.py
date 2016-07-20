from django.conf.urls import url
#from article import views as  article_views


# Create your views here.

#admin.autodiscover()

urlpatterns = [
      url(r'^lists/(?P<block_id>\d+)', "article.views.article_list", name="article_list"),
      url(r'^create/(?P<block_id>\d+)/$', "article.views.create_list", name="create_list"),
      url(r'^detail/(?P<block_id>\d+)', "article.views.article_detail", name="article_detail"),
]


