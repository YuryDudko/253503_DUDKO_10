from django.urls import path , re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.base , name='base'),

    path('superuser/', views.superuser_view, name='superuser_view'),
    path('employee/', views.employee_view, name='employee_view'),
    path('customer/', views.customer_view, name='customer_view'),
    path('registered/', views.registered_user_view, name='registered_user_view'),
    #path('public/', views.public_view, name='public_view'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    #path('logout/', views.user_logout, name='logout'),

    path('company_info/', views.company_info, name='company_info'),
    #path('news/', views.news_list, name='news_list'),
    path('faq/', views.faq_list, name='faq_list'),
    path('contacts/', views.contacts_list, name='contacts_list'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('vacancies/', views.vacancies_list, name='vacancies_list'),
    path('reviews/', views.reviews_list, name='reviews_list'),
    path('reviews/add/', views.add_review, name='add_review'),
    path('promotions/', views.promotions_list, name='promotions_list'),
    path('home/' , views.home , name='home'),

    path('products/', views.product_list, name='product_list'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),

    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('place_order/', views.place_order, name='place_order'),

    path('pickup_points/', views.pickup_points, name='pickup_points'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),

    re_path(r'^news/$', views.news_list, name='news_list'),
    path('news/create/', views.create_news, name='create_news'),
    path('check_zip_code/', views.check_zip_code, name='check_zip_code'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)