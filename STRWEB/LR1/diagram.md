```mermaid
classDiagram
    class User {
        +id: AutoField
        +password: CharField
        +last_login: DateTimeField
        +is_superuser: BooleanField
        +username: CharField
        +first_name: CharField
        +last_name: CharField
        +email: CharField
        +is_staff: BooleanField
        +is_active: BooleanField
        +date_joined: DateTimeField
    }

    class Employee {
        +user: OneToOneField
        +first_name: CharField
        +last_name: CharField
        +position: CharField
        +contact_info: CharField
        +age: PositiveIntegerField
        +photo: URLField
    }

    class ProductType {
        +name: CharField
    }

    class Manufacturer {
        +name: CharField
    }

    class Product {
        +name: CharField
        +price: DecimalField
        +description: TextField
        +unit: CharField
        +product_type: ForeignKey
        +manufacturer: ForeignKey
    }

    class Customer {
        +user: OneToOneField
        +first_name: CharField
        +last_name: CharField
        +email: EmailField
        +phone: CharField
        +address: TextField
        +city: CharField
        +age: PositiveIntegerField
    }

    class Order {
        +customer: ForeignKey
        +order_date: DateTimeField
        +delivery_date: DateTimeField
    }

    class OrderItem {
        +order: ForeignKey
        +product: ForeignKey
        +quantity: PositiveIntegerField
    }

    class CompanyInfo {
        +about_text: TextField
    }

    class News {
        +title: CharField
        +content: TextField
        +image: URLField
        +date_added: DateTimeField
    }

    class FAQ {
        +question: CharField
        +answer: TextField
        +date_added: DateTimeField
    }

    class Contacts {
        +employee_name: CharField
        +description: TextField
        +phone: CharField
        +email: EmailField
        +photo: ImageField
    }

    class Vacancies {
        +title: CharField
        +description: TextField
    }

    class Review {
        +name: CharField
        +rating: IntegerField
        +text: TextField
        +date_added: DateTimeField
    }

    class Promotion {
        +code: CharField
        +is_active: BooleanField
    }

    class Profile {
        +user: OneToOneField
        +role: CharField
    }

    class PickupPoint {
        +name: CharField
        +address: CharField
        +phone: CharField
        +hours: CharField
    }

    User --o Employee
    User --o Customer
    ProductType --o Product
    Manufacturer --o Product
    Customer --o Order
    Order --o OrderItem
    Product --o OrderItem
    User --o Profile
    ```
