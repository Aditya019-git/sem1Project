from django.db import models


from django.db import models

# Customer Model
class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)  # Limit to 50 characters for names
    last_name = models.CharField(max_length=50)   # Limit to 50 characters for names
    phone = models.CharField(max_length=15)       # Standard phone number length
    address = models.TextField()                  # For full address, using TextField
    email = models.EmailField(unique=True)        # EmailField enforces email formatting
    password = models.CharField(max_length=128)   # Django recommends up to 128 characters for passwords

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Designer Model
class Designer(models.Model):
    designer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)       # Full name
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    address = models.TextField()                  # Detailed address
    pincode = models.CharField(max_length=6)      # Pincode/Zipcode is typically 5-6 digits
    locality = models.CharField(max_length=100)   # Locality name
    portfolio = models.URLField(null=True, blank=True)  # Optional URL for portfolio

    def __str__(self):
        return self.name

# Admin Model
class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)       # Full name
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name

# Interior Style Model
class InteriorStyle(models.Model):
    style_id = models.AutoField(primary_key=True)
    style_name = models.CharField(max_length=100) # Style name

    def __str__(self):
        return self.style_name

# Product Model
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)       # Product name
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price with up to 8 digits and 2 decimal places
    amazon_link = models.URLField()               # Amazon product link
    style = models.ForeignKey(InteriorStyle, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# 3D View Model
class ThreeDView(models.Model):
    id = models.AutoField(primary_key=True)
    style = models.ForeignKey(InteriorStyle, on_delete=models.CASCADE)
    front_view = models.ImageField(upload_to='3d_views/front/')  # Path for uploaded images
    side_view = models.ImageField(upload_to='3d_views/side/')    # Path for uploaded images
    bird_view = models.ImageField(upload_to='3d_views/bird/')    # Path for uploaded images

    def __str__(self):
        return f"3D View for Style {self.style.style_name}"

# Project Model
class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE)
    style = models.ForeignKey(InteriorStyle, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)      # Example: "Pending", "Completed", etc.
    start_date = models.DateField()               # Start date of the project
    end_date = models.DateField()                 # End date of the project
    budget = models.DecimalField(max_digits=12, decimal_places=2)  # Budget for the project

    def __str__(self):
        return f"Project {self.project_id} by {self.customer} with {self.designer}"

# Feedback Model
class Feedback(models.Model):
    feed_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE)
    comment = models.TextField()                 # Feedback comments

    def __str__(self):
        return f"Feedback for Project {self.project.project_id}"
