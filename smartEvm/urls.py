from django.conf.urls import url
from . import views

urlpatterns = [
	url( r'^$', views.index , name = 'index'),#home page url
	url( r'^ $', views.index , name = 'index'),
	url( r'^contact$', views.contact , name = 'contact'),#contact tab
	url( r'^about$', views.about , name = 'about'),#about tab
	url( r'^authentication$', views.authentication , name = 'authentication'),#authentication tab
	url( r'^auth$', views.auth , name = 'auth'),#initiate sensor for authentication
	url( r'^vote$', views.vote , name = 'vote'),#storing the vote
	url( r'^enroll$', views.enroll , name = 'enroll'),#enroll the user
	url( r'^enrollment$', views.enrollment , name = 'enrollment'),#enrollment tab
	url( r'^pre_enroll$', views.pre_enroll , name = 'pre_enroll'),#initiate sensor for enrollment
]
