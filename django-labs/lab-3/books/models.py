import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver

# Custom validators for model-level validation (works in Admin & ModelForms)
def validate_book_title(value):
    if len(value) < 10 or len(value) > 50:
        raise ValidationError("The length of a book title must be between 10 & 50 characters.")

def validate_category_name(value):
    if len(value) < 2:
        raise ValidationError("The minimum length of a category name is 2 characters.")


class Category(models.Model):
    name = models.CharField(max_length=100, validators=[validate_category_name])

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Book(models.Model):
    # 1. Related to an existing user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")
    # 7.1 Title validation (10 to 50 chars)
    title = models.CharField(max_length=50, validators=[validate_book_title])
    desc = models.TextField(verbose_name="Description")
    rate = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    # 2. Related to one or more categories
    categories = models.ManyToManyField(Category, related_name="books")

    def __str__(self):
        return self.title


class ISBN(models.Model):
    # 3. One-to-one relationship with Book
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name="isbn")
    # 4. Fields: author title, book title, and auto-generated ISBN string
    author_title = models.CharField(max_length=100, blank=True)
    book_title = models.CharField(max_length=255, blank=True)
    isbn_number = models.CharField(max_length=50, unique=True, blank=True)

    def __str__(self):
        return self.isbn_number


# Bonus: Signal to auto-create and assign an ISBN object when a Book is created
@receiver(post_save, sender=Book)
def create_book_isbn(sender, instance, created, **kwargs):
    if created:
        # Generate a unique pseudo-ISBN using UUID if a real generator isn't provided
        generated_isbn = f"ISBN-{uuid.uuid4().hex[:10].upper()}"
        
        ISBN.objects.create(
            book=instance,
            book_title=instance.title,
            author_title=instance.user.get_full_name() or instance.user.username,
            isbn_number=generated_isbn
        )