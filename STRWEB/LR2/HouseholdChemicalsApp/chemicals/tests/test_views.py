from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.timezone import make_aware
from ..models import Profile, Employee, Customer, Product, Order, News, CompanyInfo, Manufacturer, ProductType

class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser('admin', 'admin@example.com', 'password')
        self.employee_user = User.objects.create_user(username='employee', password='password')
        self.customer_user = User.objects.create_user(username='customer', password='password')
        Profile.objects.create(user=self.employee_user, role='employee')
        Profile.objects.create(user=self.customer_user, role='customer')
        Employee.objects.create(user=self.employee_user, age=30)
        Customer.objects.create(user=self.customer_user, age=30)

        self.manufacturer = Manufacturer.objects.create(name="Test Manufacturer")
        self.producttype = ProductType.objects.create(name="Test ProductType")
        
        self.product = Product.objects.create(
            name="Product1",
            price=10.0,
            description="Description",
            unit="unit",
            manufacturer=self.manufacturer ,
            product_type=self.producttype,
        )
        
        self.order = Order.objects.create(
            customer=Customer.objects.get(user=self.customer_user),
            delivery_date=timezone.now() + timezone.timedelta(days=7),
        )
        self.order.products.add(self.product)

    def test_base_view(self):
        response = self.client.get(reverse('base'))
        self.assertEqual(response.status_code, 200)

    def test_admin_dashboard(self):
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('admin_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        response = self.client.get(reverse('admin_dashboard'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_employee_dashboard(self):
        self.client.login(username='employee', password='password')
        response = self.client.get(reverse('employee_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        response = self.client.get(reverse('employee_dashboard'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password': 'password',
            'role': 'customer',
            'age': 25,
        })
        self.assertEqual(response.status_code, 200)  # Redirect to base after successful registration

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('login'), {
            'username': 'customer',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 302)  # Redirect to base after successful login

    def test_logout_view(self):
        self.client.login(username='customer', password='password')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect to base after successful logout

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_company_info_view(self):
        CompanyInfo.objects.create(about_text="About us")
        response = self.client.get(reverse('company_info'))
        self.assertEqual(response.status_code, 200)

    def test_news_list_view(self):
        response = self.client.get(reverse('news_list'))
        self.assertEqual(response.status_code, 200)

    def test_create_news_view(self):
        response = self.client.get(reverse('create_news'))
        self.assertEqual(response.status_code, 200)

    def test_faq_list_view(self):
        response = self.client.get(reverse('faq_list'))
        self.assertEqual(response.status_code, 200)

    def test_contacts_list_view(self):
        response = self.client.get(reverse('contacts_list'))
        self.assertEqual(response.status_code, 200)

    def test_privacy_policy_view(self):
        response = self.client.get(reverse('privacy_policy'))
        self.assertEqual(response.status_code, 200)

    def test_vacancies_list_view(self):
        response = self.client.get(reverse('vacancies_list'))
        self.assertEqual(response.status_code, 200)

    def test_reviews_list_view(self):
        response = self.client.get(reverse('reviews_list'))
        self.assertEqual(response.status_code, 200)

    def test_add_review_view(self):
        response = self.client.get(reverse('add_review'))
        self.assertEqual(response.status_code, 200)

    def test_promotions_list_view(self):
        response = self.client.get(reverse('promotions_list'))
        self.assertEqual(response.status_code, 200)

    def test_product_list_view(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)

    def test_profile_view(self):
        self.client.login(username='customer', password='password')
        response = self.client.get(reverse('profile_view'))
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        response = self.client.get(reverse('profile_view'))
        self.assertEqual(response.status_code, 200)  # Redirect to auth_options if not authenticated

    def test_profile_edit_view(self):
        self.client.login(username='customer', password='password')
        response = self.client.get(reverse('profile_edit'))
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        response = self.client.get(reverse('profile_edit'))
        self.assertEqual(response.status_code, 200)  # Redirect to auth_options if not authenticated

    def test_add_to_cart_view(self):
        self.client.login(username='customer', password='password')
        response = self.client.post(reverse('add_to_cart'), {'product_ids': [self.product.id]})
        self.assertEqual(response.status_code, 302)  # Redirect to cart after adding to cart

    def test_place_order_view(self):
        self.client.login(username='customer', password='password')
        response = self.client.post(reverse('place_order'))
        self.assertEqual(response.status_code, 302)  # Redirect to profile_view after placing order

    def test_pickup_points_view(self):
        response = self.client.get(reverse('pickup_points'))
        self.assertEqual(response.status_code, 200)

    def test_check_zip_code_view(self):
        response = self.client.get(reverse('check_zip_code'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('check_zip_code'), {'zip_code': '90210'})
        self.assertEqual(response.status_code, 200)
