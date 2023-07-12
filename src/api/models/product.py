from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from .discount import Discount
from .category import ProductCategory
from api.models.info import State, UnitOfMeasure


class ProductInventory(models.Model):
    quantity = models.IntegerField(_("Product Inventory Quantity"), default=0)
    date_of_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = _("Product Inventory")
        verbose_name_plural = _("Product Inventories")
        ordering = ("id",)
        db_table = "product_inventory"

    def delete(self, *args):
        self.deleted_at = timezone.now()
        self.save()
        return True

    def update_product_inventory(self, quantity):
        self.quantity = quantity
        self.save()
        return True


class Product(models.Model):
    name = models.CharField(_("Product Name"), max_length=50)
    description = models.TextField(_("Product Description"), null=True, blank=True)
    price = models.DecimalField(_("Product Price"), max_digits=10, decimal_places=2)
    uuid = models.UUIDField(_("Product UUID"), unique=True, editable=False, auto_created=True, null=True)
    sku = models.CharField(_("Product SKU"), max_length=50, null=True, blank=True)
    date_of_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(_("Product Image URL"), upload_to="product", null=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_inventory = models.ForeignKey(ProductInventory, on_delete=models.CASCADE, null=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    unit_of_measure = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE, null=True)
    views = models.IntegerField(_("Product Views"), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ("id",)
        db_table = "product"
        indexes = [
            models.Index(fields=["sku"]),
            models.Index(fields=["name"]),
            models.Index(fields=["price"]),
        ]

    def delete(self, *args):
        self.deleted_at = timezone.now()
        self.save()
        return True

    @property
    def get_image_url(self):
        # "Returns the image url."
        try:
            return '%s%s' % (settings.HOST, self.image.url)
        except ValueError:
            return ''


class TopProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_of_created = models.DateTimeField(auto_now_add=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Top Product")
        verbose_name_plural = _("Top Products")
        ordering = ("id",)
        db_table = "top_product"
        indexes = [
            models.Index(fields=["product"]),
        ]

    def __str__(self):
        return self.product.name

    def update_top_product(self, product):
        self.product = product
        self.save()
        return True


class BestOffer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Best Offer")
        verbose_name_plural = _("Best Offers")
        ordering = ("id",)
        db_table = "best_offer"

    def __str__(self):
        return self.product.name

    @property
    def get_image_url(self):
        # "Returns the image url."
        try:
            return '%s%s' % (settings.HOST, self.product.image.url)
        except ValueError:
            return ''


class RatingProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(_("Rating Product"), default=0)
    date_of_created = models.DateTimeField(auto_now_add=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Rating Product")
        verbose_name_plural = _("Rating Products")
        ordering = ("id",)
        db_table = "rating_product"
        indexes = [
            models.Index(fields=["product"]),
        ]

    def __str__(self):
        return self.product.name

    def update_rating_product(self, rating):
        self.rating = rating
        self.save()
        return True
