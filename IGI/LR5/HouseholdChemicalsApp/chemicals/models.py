from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinValueValidator

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    contact_info = models.CharField(
        max_length=20, 
        validators=[RegexValidator(regex=r'^\+375 \(29\) \d{3}-\d{2}-\d{2}$', message="Телефон должен быть в формате +375 (29) XXX-XX-XX")]
    )
    age = models.PositiveIntegerField(validators=[MinValueValidator(18, message="Возраст должен быть 18 лет и старше")])
    #photo = models.ImageField(upload_to='employee_photos/', blank=True, null=True)  # Поле для фото
    photo = models.URLField(null=True, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    unit = models.CharField(max_length=50)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(
        max_length=20, 
        validators=[RegexValidator(regex=r'^\+375 \(29\) \d{3}-\d{2}-\d{2}$', message="Телефон должен быть в формате +375 (29) XXX-XX-XX")]
    )
    address = models.TextField()
    city = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18, message="Возраст должен быть 18 лет и старше")])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()

    def __str__(self):
        return f"Order {self.id} by {self.customer}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in order {self.order.id}"

#Website info pages

class CompanyInfo(models.Model):
    about_text = models.TextField()

    def __str__(self):
        return self.about_text

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

class Contacts(models.Model):
    employee_name = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    photo = models.ImageField(upload_to='contact_photos/', blank=True, null=True)  # Поле для фото

    def __str__(self):
        return self.employee_name

class Vacancies(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.title

class Review(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Promotion(models.Model):
    code = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.code

class Profile(models.Model):
    ROLE_CHOICES = (
        ('employee', 'Employee'),
        ('customer', 'Customer'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')

    def __str__(self):
        return self.user.username

# class Cart(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product, through='CartItem')

#     def __str__(self):
#         return f"Cart for {self.user.username}"

# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return f"{self.quantity} x {self.product.name} in cart"

class PickupPoint(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    hours = models.CharField(max_length=100)

    def __str__(self):
        return self.name