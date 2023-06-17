from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductCategory(models.Model):
    name = models.CharField(_("Product Category Name"), max_length=50)
    description = models.TextField(_("Product Category Description"))
    date_of_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    image_url = models.URLField(_("Product Category Image URL"), upload_to="static/images/product_category")
    deleted_at = models.DateTimeField(null=True, blank=True)
    state = models.ForeignKey("info.State", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product Category")
        verbose_name_plural = _("Product Categories")
        ordering = ("id",)
        db_table = "product_category"

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


class ProductInventory(models.Model):
    quantity = models.IntegerField(_("Product Inventory Quantity"), default=0)
    date_of_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.quantity

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


class Discount(models.Model):
    name = models.CharField(_("Discount Name"), max_length=50)
    description = models.TextField(_("Discount Description"))
    discount_percent = models.DecimalField(_("Discount Percent"), max_digits=5, decimal_places=2)
    date_of_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    state = models.ForeignKey("info.State", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Discount")
        verbose_name_plural = _("Discounts")
        ordering = ("id",)
        db_table = "discount"

    def delete(self, *args):
        self.deleted_at = timezone.now()
        self.save()
        return True


class Product(models.Model):
    name = models.CharField(_("Product Name"), max_length=50)
    description = models.TextField(_("Product Description"), null=True, blank=True)
    price = models.DecimalField(_("Product Price"), max_digits=10, decimal_places=2)
    sku = models.CharField(_("Product SKU"), max_length=50)
    date_of_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    image_url = models.URLField(_("Product Image URL"), upload_to="static/images/product", null=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_inventory = models.ForeignKey(ProductInventory, on_delete=models.CASCADE, null=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True)
    state = models.ForeignKey("info.State", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ("id",)
        db_table = "product"

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
