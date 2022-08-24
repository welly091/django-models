from django.urls import path
from .views import ShowListView, ShowDetailListView, ShowDrinkView, ShowDetailDrinkView

urlpatterns = [
    path("", ShowListView.as_view(), name="showList"),
    path("<int:pk>/", ShowDetailListView.as_view(), name="showDetailList"),
    path("drink/", ShowDrinkView.as_view(), name="showDrink"),
    path("drink/<int:pk>/", ShowDetailDrinkView.as_view(), name="showDetailDrink")
]