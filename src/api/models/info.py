from django.db import models
from django.utils.translation import gettext_lazy as _


class State(models.Model):
    name = models.CharField(max_length=50, help_text=_("State Name"))
    abbreviation = models.CharField(max_length=2, help_text=_("State Abbreviation"))
    date_of_created = models.DateTimeField(auto_now_add=True, help_text=_("Date of Created"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")
        db_table = "states"


class Language(models.Model):
    name = models.CharField(max_length=50, help_text=_("Language Name"))
    abbreviation = models.CharField(max_length=2, help_text=_("Language Abbreviation"))
    date_of_created = models.DateTimeField(auto_now_add=True, help_text=_("Date of Created"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")
        db_table = "languages"


class Country(models.Model):
    shortname = models.CharField(max_length=20, help_text=_("Country Short Name"))
    fullname = models.CharField(max_length=50, help_text=_("Country Full Name"))
    code = models.CharField(max_length=10, help_text=_("Country Code"))
    postal_code = models.CharField(max_length=10, help_text=_("Country Postal Code"))
    date_of_created = models.DateTimeField(auto_now_add=True, help_text=_("Date of Created"))
    state = models.ForeignKey(State, on_delete=models.CASCADE, help_text=_("State"))

    def __str__(self):
        return self.shortname

    class Meta:
        verbose_name = _("Countrie")
        verbose_name_plural = _("Countries")
        db_table = "countries"


class Region(models.Model):
    shortname = models.CharField(max_length=50, help_text=_("Region Short Name"))
    fullname = models.CharField(max_length=50, help_text=_("Region Full Name"))
    code = models.CharField(max_length=10, help_text=_("Region Code"))
    date_of_created = models.DateTimeField(auto_now_add=True, help_text=_("Date of Created"))
    country = models.ForeignKey(Country, on_delete=models.CASCADE, help_text=_("Country"))
    state = models.ForeignKey(State, on_delete=models.CASCADE, help_text=_("State"))

    def __str__(self):
        return self.shortname

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")
        db_table = "regions"


class District(models.Model):
    shortname = models.CharField(max_length=50, help_text=_("District Short Name"))
    fullname = models.CharField(max_length=50, help_text=_("District Full Name"))
    code = models.CharField(max_length=10, help_text=_("District Code"))
    date_of_created = models.DateTimeField(auto_now_add=True, help_text=_("Date of Created"))
    region = models.ForeignKey(Region, on_delete=models.CASCADE, help_text=_("Region"))
    state = models.ForeignKey(State, on_delete=models.CASCADE, help_text=_("State"))

    def __str__(self):
        return self.shortname

    class Meta:
        verbose_name = _("District")
        verbose_name_plural = _("Districts")
        db_table = "districts"


class PaymentType(models.Model):
    name = models.CharField(max_length=50, help_text=_("Payment Type Name"))
    date_of_created = models.DateTimeField(auto_now_add=True, help_text=_("Date of Created"))
    state = models.ForeignKey(State, on_delete=models.CASCADE, help_text=_("State"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Payment Types")
        verbose_name_plural = _("Payment Types")
        db_table = "payment_types"


class UnitOfMeasure(models.Model):
    name = models.CharField(max_length=50, help_text=_("Unit of Measure Name"))
    abbreviation = models.CharField(max_length=2, help_text=_("Unit of Measure Abbreviation"))
    date_of_created = models.DateTimeField(auto_now_add=True, help_text=_("Date of Created"))
    state = models.ForeignKey(State, on_delete=models.CASCADE, help_text=_("State"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Unit of Measure")
        verbose_name_plural = _("Units of Measure")
        db_table = "units_of_measure"
