from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# slugify transform a string into a slug.
# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.street}, {self.postal_code}, {self.city}"

    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        "Address", on_delete=models.CASCADE, null=True)

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self) -> str:
        return self.full_name()


class Book(models.Model):

    # define the structure of an item.
    # define the type of data that can be stored in db
    title = models.CharField(max_length=50)  # string
    rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)])  # numbers
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True)
    published_countries = models.ManyToManyField(Country, null=False)

    def get_absolute_path(self):
        return reverse("book_detail", args=[self.slug])

    # # we override the save method and format the slug field before saving to the db.
    # def save(self, *args, **kwargs):  # add *args and **kwargs to make sure that additional
    #     self.slug = slugify(f"{self.title} {self.id}")
    #     # parameters are passed to the super() method
    #     super().save(*args, **kwargs)  # to import the built-in django save method

    def __str__(self):
        return f"{self.title} ({self.rating})"
