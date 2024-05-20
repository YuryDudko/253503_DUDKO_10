from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from ..models import (
    Employee, ProductType, Manufacturer, Product, Customer, Order, OrderItem,
    CompanyInfo, News, FAQ, Contacts, Vacancies, Review, Promotion, Profile, PickupPoint
)

class EmployeeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')

    def test_employee_creation(self):
        employee = Employee.objects.create(
            user=self.user,
            first_name="John",
            last_name="Doe",
            position="Manager",
            contact_info="+375 (29) 123-45-67",
            age=30
        )
        self.assertEqual(employee.__str__(), "John Doe")
        self.assertEqual(employee.contact_info, "+375 (29) 123-45-67")

    def test_employee_age_validation(self):
        employee = Employee(
            user=self.user,
            first_name="John",
            last_name="Doe",
            position="Manager",
            contact_info="+375 (29) 123-45-67",
            age=17
        )
        with self.assertRaises(ValidationError):
            employee.full_clean()

class ProductModelTest(TestCase):
    def setUp(self):
        self.product_type = ProductType.objects.create(name="Type1")
        self.manufacturer = Manufacturer.objects.create(name="Manufacturer1")

    def test_product_creation(self):
        product = Product.objects.create(
            name="Product1",
            price=10.0,
            description="Description",
            unit="unit",
            product_type=self.product_type,
            manufacturer=self.manufacturer
        )
        self.assertEqual(product.__str__(), "Product1")
        self.assertEqual(product.price, 10.0)

class CustomerModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testcustomer')

    def test_customer_creation(self):
        customer = Customer.objects.create(
            user=self.user,
            first_name="Alice",
            last_name="Smith",
            email="alice@example.com",
            phone="+375 (29) 123-45-67",
            address="Address",
            city="City",
            age=25
        )
        self.assertEqual(customer.__str__(), "Alice Smith")
        self.assertEqual(customer.email, "alice@example.com")

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testcustomer')
        self.customer = Customer.objects.create(
            user=self.user,
            first_name="Alice",
            last_name="Smith",
            email="alice@example.com",
            phone="+375 (29) 123-45-67",
            address="Address",
            city="City",
            age=25
        )
        self.product_type = ProductType.objects.create(name="Type1")
        self.manufacturer = Manufacturer.objects.create(name="Manufacturer1")
        self.product = Product.objects.create(
            name="Product1",
            price=10.0,
            description="Description",
            unit="unit",
            product_type=self.product_type,
            manufacturer=self.manufacturer
        )

    def test_order_creation(self):
        order = Order.objects.create(
            customer=self.customer,
            delivery_date="2024-12-31"
        )
        order.products.add(self.product)
        self.assertEqual(order.__str__(), f"Order {order.id} by {self.customer}")

    def test_order_item_creation(self):
        order = Order.objects.create(
            customer=self.customer,
            delivery_date="2024-12-31"
        )
        order_item = OrderItem.objects.create(
            order=order,
            product=self.product,
            quantity=2
        )
        self.assertEqual(order_item.__str__(), f"{order_item.quantity} x {order_item.product.name} in order {order_item.order.id}")
        self.assertEqual(order_item.quantity, 2)

class CompanyInfoModelTest(TestCase):
    def test_company_info_creation(self):
        company_info = CompanyInfo.objects.create(
            about_text="This is a company."
        )
        self.assertEqual(company_info.about_text, "This is a company.")

class NewsModelTest(TestCase):
    def test_news_creation(self):
        news = News.objects.create(
            title="News Title",
            content="This is news content.",
            image="http://example.com/image.jpg"
        )
        self.assertEqual(news.__str__(), "News Title")
        self.assertEqual(news.content, "This is news content.")

class FAQModelTest(TestCase):
    def test_faq_creation(self):
        faq = FAQ.objects.create(
            question="What is your return policy?",
            answer="You can return items within 30 days."
        )
        self.assertEqual(faq.__str__(), "What is your return policy?")
        self.assertEqual(faq.answer, "You can return items within 30 days.")

class ContactsModelTest(TestCase):
    def test_contacts_creation(self):
        contact = Contacts.objects.create(
            employee_name="John Doe",
            description="Manager",
            phone="+375 (29) 123-45-67",
            email="john@example.com",
            photo="http://example.com/photo.jpg"
        )
        self.assertEqual(contact.__str__(), "John Doe")
        self.assertEqual(contact.phone, "+375 (29) 123-45-67")

class VacanciesModelTest(TestCase):
    def test_vacancies_creation(self):
        vacancy = Vacancies.objects.create(
            title="Software Engineer",
            description="Develop and maintain software applications."
        )
        self.assertEqual(vacancy.__str__(), "Software Engineer")
        self.assertEqual(vacancy.description, "Develop and maintain software applications.")

class ReviewModelTest(TestCase):
    def test_review_creation(self):
        review = Review.objects.create(
            name="Alice",
            rating=5,
            text="Great product!"
        )
        self.assertEqual(review.__str__(), "Alice")
        self.assertEqual(review.rating, 5)

class PromotionModelTest(TestCase):
    def test_promotion_creation(self):
        promotion = Promotion.objects.create(
            code="DISCOUNT2024",
            is_active=True
        )
        self.assertEqual(promotion.__str__(), "DISCOUNT2024")
        self.assertTrue(promotion.is_active)

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='profileuser')

    def test_profile_creation(self):
        profile = Profile.objects.create(
            user=self.user,
            role='customer'
        )
        self.assertEqual(profile.__str__(), "profileuser")
        self.assertEqual(profile.role, 'customer')

class PickupPointModelTest(TestCase):
    def test_pickup_point_creation(self):
        pickup_point = PickupPoint.objects.create(
            name="Main Office",
            address="123 Main St",
            phone="+375 (29) 123-45-67",
            hours="9 AM - 5 PM"
        )
        self.assertEqual(pickup_point.__str__(), "Main Office")
        self.assertEqual(pickup_point.address, "123 Main St")

