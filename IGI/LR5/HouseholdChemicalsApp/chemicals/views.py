from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import login, authenticate , logout
from .forms import UserRegistrationForm , ReviewForm , ProfileForm , LoginForm , CustomerForm , EmployeeForm
from .models import Profile, Employee, Customer , CompanyInfo, News, FAQ, Contacts, Vacancies, Review, Promotion , Product , Order , OrderItem , PickupPoint, News
from django.http import HttpResponse , JsonResponse
from .decorators import superuser_required, role_required
from django.contrib.auth.decorators import login_required , user_passes_test
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count , Sum , Q
import requests
from django.db.models.functions import TruncMonth, TruncYear
import pandas as pd
import plotly.express as px
import logging

logger = logging.getLogger('chemicals')
  
def base(request):
    return render(request, "base.html")

def index(request):
    return render(request, "index.html")

@superuser_required
def superuser_view(request):
    return render(request, 'superuser_page.html')

@role_required('employee')
@login_required
def employee_view(request):
    return render(request, 'employee_page.html')

@role_required('customer')
@login_required
def customer_view(request):
    return render(request, 'customer_page.html')

@login_required
def registered_user_view(request):
    return render(request, 'registered_user_page.html')

def is_employee(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'employee'

def is_superadmin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superadmin)
def admin_dashboard(request):
    # Прайс-лист товаров
    products = Product.objects.all()

    # Список заказчиков, сгруппированных по городам
    customers_by_city = Customer.objects.values('city').annotate(count=Count('id'))

    # Товар с наибольшим спросом
    most_popular_product = Product.objects.annotate(num_sales=Count('order')).order_by('-num_sales').first()

    # Товар с наименьшим спросом
    least_popular_product = Product.objects.annotate(num_sales=Count('order')).order_by('num_sales').first()

    # Ежемесячный объем продаж товаров
    monthly_sales = Order.objects.annotate(month=TruncMonth('order_date')).values('month', 'products__name').annotate(total_sales=Count('products__name'))

    # Годовой отчет поступлений от продаж
    yearly_revenue = Order.objects.annotate(year=TruncYear('order_date')).values('year').annotate(total_revenue=Sum('products__price'))

    orders = Order.objects.annotate(month=TruncMonth('order_date')).values('month').annotate(total_sales=Count('id'))
    df = pd.DataFrame(list(orders))
    fig = px.line(df, x='month', y='total_sales', title='Ежемесячный объем продаж')
    sales_chart_html = fig.to_html()

    context = {
        'products': products,
        'customers_by_city': customers_by_city,
        'most_popular_product': most_popular_product,
        'least_popular_product': least_popular_product,
        'monthly_sales': monthly_sales,
        'yearly_revenue': yearly_revenue,
        'sales_chart_html': sales_chart_html,
    }

    return render(request, 'admin_dashboard.html', context)
    
@login_required
@user_passes_test(is_employee)
def employee_dashboard(request):
    orders = Order.objects.all().select_related('customer')
    customers = Customer.objects.all()

    # Подсчет количества проданных товаров
    sold_products = Order.objects.values('products__name').annotate(total_quantity=Count('products')).order_by('products__name')

    return render(request, 'employee_dashboard.html', {
        'orders': orders,
        'customers': customers,
        'sold_products': sold_products,
    })



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            #new_user.username(form.cleaned_data['username'])
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            
            # Создание профиля
            role = form.cleaned_data['role']
            age = form.cleaned_data['age']
            profile = Profile.objects.create(user=new_user, role=role)
            
            # Создание соответствующего профиля
            if role == 'employee':
                Employee.objects.create(user=new_user , age=age)
            elif role == 'customer':
                Customer.objects.create(user=new_user , age=age)
            logger.info(f"Created instance with role: {role}.")
            # Аутентификация и вход пользователя
            user = authenticate(username=new_user.username, password=form.cleaned_data['password'])
            login(request, user)
            logger.info(f"Registered user with name: {new_user.username}.")
            return redirect('base')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    logger.info(f"User logined")
                    return redirect('base')
                else:
                    logger.info(f"Try logging in disabled account")
                    return render(request, 'login.html', {'form': form, 'error': 'Disabled account'})
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid login'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('base')

def logout_view(request):
    logout(request)
    return redirect('base') 

#navigation
def home(request):
    latest_news = News.objects.latest('date_added') if News.objects.exists() else None
    return render(request, 'home.html', {'latest_news': latest_news})

def company_info(request):
    company_info = get_object_or_404(CompanyInfo)
    logger.info("Company info was asked")
    return render(request, 'company_info.html', {'company_info': company_info})

def company_info_create(request):
    if request.method == 'POST':
        form = CompanyInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_info_list')
    else:
        form = CompanyInfoForm()
    return render(request, 'company_info_form.html', {'form': form})

def company_info_update(request, pk):
    info = get_object_or_404(CompanyInfo, pk=pk)
    if request.method == 'POST':
        form = CompanyInfoForm(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return redirect('company_info_list')
    else:
        form = CompanyInfoForm(instance=info)
    return render(request, 'company_info_form.html', {'form': form})

def company_info_delete(request, pk):
    info = get_object_or_404(CompanyInfo, pk=pk)
    if request.method == 'POST':
        info.delete()
        return redirect('company_info_list')
    return render(request, 'company_info_confirm_delete.html', {'info': info})

def fetch_dog_image():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    if response.status_code == 200:
        return response.json()['message']
    return None

def news_list(request):
    news_list = News.objects.all()
    return render(request, 'news_list.html', {'news_list': news_list})

def create_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image_url = fetch_dog_image()
        if image_url:
            news = News(title=title, content=content, image=image_url)
            news.save()
            return redirect('news_list')
    return render(request, 'create_news.html')

def faq_list(request):
    faq_list = FAQ.objects.all()
    return render(request, 'faq_list.html', {'faq_list': faq_list})

def contacts_list(request):
    contacts_list = Employee.objects.all()
    return render(request, 'contacts.html', {'contacts_list': contacts_list})

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def vacancies_list(request):
    vacancies_list = Vacancies.objects.all()
    return render(request, 'vacancies_list.html', {'vacancies_list': vacancies_list})

def reviews_list(request):
    reviews_list = Review.objects.all()
    return render(request, 'reviews_list.html', {'reviews_list': reviews_list})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews_list')
    else:
        form = ReviewForm()
    return render(request, 'review_form.html', {'form': form})

def promotions_list(request):
    promotions_list = Promotion.objects.all()
    return render(request, 'promotions_list.html', {'promotions_list': promotions_list})

def product_list(request):
    query = request.GET.get('q')
    products = Product.objects.all()
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    sort_by = request.GET.get('sort_by')
    if sort_by:
        products = products.order_by(sort_by)
    return render(request, 'product_list.html', {'products': products})


def profile_view(request):
    if request.user.is_authenticated:
        user = request.user
        profile = request.user.profile
        orders = []

        if profile.role == 'customer':
            try:
                instance = user.customer
                orders = instance.order_set.all()
            except Customer.DoesNotExist:
                instance = None
            
        elif profile.role == 'employee':
            try:
                instance = user.employee
            except Employee.DoesNotExist:
                instance = None
        else:
            instance = None

        return render(request, 'profile_view.html', {'user': user, 'instance': instance, 'profile': profile, 'orders': orders})
    else:
        return render(request, 'auth_options.html')


def profile_edit(request):
    if request.user.is_authenticated:
        # profile = request.user.profile
        # if request.method == 'POST':
        #     form = ProfileForm(request.POST, instance=profile)
        #     if form.is_valid():
        #         form.save()
        #         return redirect('profile')
        # else:
        #     form = ProfileForm(instance=profile)
        # return render(request, 'profile.html', {'form': form})
        user = request.user
        profile = user.profile

        if profile.role == 'customer':
            if hasattr(user, 'customer'):
                instance = user.customer
            else:
                instance = Customer(user=user)
            if request.method == 'POST':
                form = CustomerForm(request.POST, instance=instance)
            else:
                form = CustomerForm(instance=instance)
        elif profile.role == 'employee':
            if hasattr(user, 'employee'):
                instance = user.employee
            else:
                instance = Employee(user=user)
            if request.method == 'POST':
                form = EmployeeForm(request.POST, instance=instance)
            else:
                form = EmployeeForm(instance=instance)
        else:
            form = ProfileForm(instance=profile)

        if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('profile_view')

        return render(request, 'profile_edit.html', {'form': form})
    else:
        return render(request, 'auth_options.html')

def add_to_cart(request):
    if request.method == 'POST':
        product_ids = request.POST.getlist('product_ids')
        cart = request.session.get('cart', {})

        for product_id in product_ids:
            if product_id in cart:
                cart[product_id] += 1
            else:
                cart[product_id] = 1

        request.session['cart'] = cart
        return redirect('cart')
    else:
        return redirect('product_list')

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []

    for product_id, quantity in cart.items():
        product = Product.objects.get(pk=product_id)
        cart_items.append({'product': product, 'quantity': quantity})

    return render(request, 'cart.html', {'cart_items': cart_items})

def place_order(request):
    if request.method == 'POST':
        customer = request.user.customer
        cart = request.session.get('cart', {})
        
        if cart:
            order = Order.objects.create(customer=customer, delivery_date=timezone.now() + timezone.timedelta(days=7))
            for product_id, quantity in cart.items():
                product = Product.objects.get(pk=product_id)
                for _ in range(quantity):
                    order.products.add(product)
            order.save()
            del request.session['cart']
            return redirect('profile_view')
        else:
            return redirect('cart')
    else:
        return redirect('cart')

def pickup_points(request):
    points = PickupPoint.objects.all()
    return render(request, 'pickup_points.html', {'points': points})

import requests
from django.shortcuts import render

import requests
from django.shortcuts import render

def check_zip_code(request):
    if request.method == 'POST':
        zip_code = request.POST.get('zip_code')
        response = requests.get(f'http://api.zippopotam.us/us/{zip_code}')
        if response.status_code == 200:
            data = response.json()
            places = data.get('places')
            if places:
                place_data = places[0]
                formatted_data = {
                    'post_code': data.get('post code'),
                    'country': data.get('country'),
                    'place_name': place_data.get('place name'),
                    'state': place_data.get('state')
                }
            else:
                formatted_data = None
        else:
            formatted_data = None
        return render(request, 'check_zip_code.html', {'data': formatted_data})
    return render(request, 'check_zip_code.html')



