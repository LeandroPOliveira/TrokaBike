import uuid
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse


class Product(models.Model):

    class Meta:
        verbose_name_plural = "Products"
        ordering = ["-created_at"]

    CATEGORY_CHOICES = [
        ("MOUNTAIN", "Mountain"),
        ("ROAD", "Road"),
        ("GRAVEL", "Gravel"),
        ("APPAREL", "Apparel"),
    ]

    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="MOUNTAIN",
    )

    color = models.CharField(max_length=40)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    year = models.PositiveIntegerField()

    description = models.TextField()

    image = models.ImageField(
        upload_to="products/%Y/%m/%d/",
        blank=True,
        null=True,
    )

    is_published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="products",
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug

            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{uuid.uuid4().hex[:5]}"

            self.slug = slug

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("products:my_products")

    def __str__(self):
        return self.name