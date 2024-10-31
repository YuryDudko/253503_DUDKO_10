from django.test import TestCase
from ..forms import UserRegistrationForm, LoginForm, ReviewForm, ProfileForm, CustomerForm, EmployeeForm

class TestForms(TestCase):

    def test_user_registration_form_valid_data(self):
        form = UserRegistrationForm(data={
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password': 'testpassword',
            'password2': 'testpassword',
            'role': 'customer',
            'age': 25
        })
        self.assertTrue(form.is_valid())

    def test_user_registration_form_invalid_data(self):
        form = UserRegistrationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)  # 5 fields are required

    def test_login_form_valid_data(self):
        form = LoginForm(data={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertTrue(form.is_valid())

    def test_login_form_invalid_data(self):
        form = LoginForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)  # Both fields are required

    def test_review_form_valid_data(self):
        form = ReviewForm(data={
            'name': 'Test Reviewer',
            'rating': 5,
            'text': 'This is a test review.'
        })
        self.assertTrue(form.is_valid())

    def test_review_form_invalid_data(self):
        form = ReviewForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)  # All fields are required

    def test_profile_form_valid_data(self):
        form = ProfileForm(data={'role': 'customer'})
        self.assertTrue(form.is_valid())

    def test_profile_form_invalid_data(self):
        form = ProfileForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)  # role field is required

    def test_customer_form_valid_data(self):
        form = CustomerForm(data={
            'first_name': 'Test',
            'last_name': 'Customer',
            'email': 'test@example.com',
            'phone': '+375 (29) 123-45-67',
            'address': '123 Main St',
            'city': 'Test City',
            'age': 30
        })
        self.assertTrue(form.is_valid())

    def test_customer_form_invalid_data(self):
        form = CustomerForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 7)  # All fields are required

    def test_employee_form_valid_data(self):
        form = EmployeeForm(data={
            'first_name': 'Test',
            'last_name': 'Employee',
            'position': 'Manager',
            'contact_info': '+375 (29) 123-45-67',
            'age': 35
        })
        self.assertTrue(form.is_valid())

    def test_employee_form_invalid_data(self):
        form = EmployeeForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)  # All fields are required except photo
