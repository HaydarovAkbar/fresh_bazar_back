from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from .discount import Discount
from .category import ProductCategory
from api.models.info import State


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
    sku = models.CharField(_("Product SKU"), max_length=50)
    date_of_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    image_url = models.ImageField(_("Product Image URL"), upload_to="product", null=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_inventory = models.ForeignKey(ProductInventory, on_delete=models.CASCADE, null=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)

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
            return '%s%s' % (settings.HOST, self.image_url.url)
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
    name = models.CharField(_("Best Offer Name"), max_length=50)
    image = models.ImageField(_("Best Offer Image"), upload_to="best_offer", null=True)
    description = models.TextField(_("Best Offer Description"), null=True, blank=True)
    date_of_created = models.DateTimeField(auto_now_add=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Best Offer")
        verbose_name_plural = _("Best Offers")
        ordering = ("id",)
        db_table = "best_offer"
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name

    def update_best_offer(self, product):
        self.product = product
        self.save()
        return True

    @property
    def get_image_url(self):
        # "Returns the image url."
        try:
            return '%s%s' % (settings.HOST, self.image.url)
        except ValueError:
            return ''
