from django.urls import path


from app__foodie import views

urlpatterns = [path("", views.index, name="app__foodie_index")]
