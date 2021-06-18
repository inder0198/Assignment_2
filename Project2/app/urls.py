from django.urls import path

from . import views     # it means - 'from all import views'

urlpatterns = [
    path('',views.index, name='index'),
    path('type1',views.vowel, name='type1'),
    path('type2',views.reverse, name='type2'),
    path('type3',views.alpha_numeric_order, name='type3'),
    path('type4',views.traverse, name='type4'),
    path('type5',views.ascii, name='type5'),
]