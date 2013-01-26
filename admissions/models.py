from django.db import models

# Create your models here.
class Year(models.Model):
    """
    A year of admissions data
    """
    year = models.IntegerField(null=True, blank=True)
    # African American
    african_american_applicants = models.IntegerField(null=True, blank=True)
    african_american_admits = models.IntegerField(null=True, blank=True)
    african_american_enrollees = models.IntegerField(null=True, blank=True)
    african_american_admit_rate = models.FloatField(null=True, blank=True)
    african_american_yield = models.FloatField(null=True, blank=True)
    # American Indian
    american_indian_applicants = models.IntegerField(null=True, blank=True)
    american_indian_admits = models.IntegerField(null=True, blank=True)
    american_indian_enrollees = models.IntegerField(null=True, blank=True)
    american_indian_admit_rate = models.FloatField(null=True, blank=True)
    american_indian_yield = models.FloatField(null=True, blank=True)
    # Asian American
    asian_american_applicants = models.IntegerField(null=True, blank=True)
    asian_american_admits = models.IntegerField(null=True, blank=True)
    asian_american_enrollees = models.IntegerField(null=True, blank=True)
    asian_american_admit_rate = models.FloatField(null=True, blank=True)
    asian_american_yield = models.FloatField(null=True, blank=True)
    # Chicano/Latino
    chicano_latino_applicants = models.IntegerField(null=True, blank=True)
    chicano_latino_admits = models.IntegerField(null=True, blank=True)
    chicano_latino_enrollees = models.IntegerField(null=True, blank=True)
    chicano_latino_admit_rate = models.FloatField(null=True, blank=True)
    chicano_latino_yield = models.FloatField(null=True, blank=True)
    # White
    white_applicants = models.IntegerField(null=True, blank=True)
    white_admits = models.IntegerField(null=True, blank=True)
    white_enrollees = models.IntegerField(null=True, blank=True)
    white_admit_rate = models.FloatField(null=True, blank=True)
    white_yield = models.FloatField(null=True, blank=True)
    # Other
    other_applicants = models.IntegerField(null=True, blank=True)
    other_admits = models.IntegerField(null=True, blank=True)
    other_enrollees = models.IntegerField(null=True, blank=True)
    other_admit_rate = models.FloatField(null=True, blank=True)
    other_yield = models.FloatField(null=True, blank=True)
    # Unknown
    unknown_applicants = models.IntegerField(null=True, blank=True)
    unknown_admits = models.IntegerField(null=True, blank=True)
    unknown_enrollees = models.IntegerField(null=True, blank=True)
    unknown_admit_rate = models.FloatField(null=True, blank=True)
    unknown_yield = models.FloatField(null=True, blank=True)
    # International
    international_applicants = models.IntegerField(null=True, blank=True)
    international_admits = models.IntegerField(null=True, blank=True)
    international_enrollees = models.IntegerField(null=True, blank=True)
    international_admit_rate = models.FloatField(null=True, blank=True)
    international_yield = models.FloatField(null=True, blank=True)
    # Total
    total_applicants = models.IntegerField(null=True, blank=True)
    total_admits = models.IntegerField(null=True, blank=True)
    total_enrollees = models.IntegerField(null=True, blank=True)
    total_admit_rate = models.FloatField(null=True, blank=True)
    total_yield = models.FloatField(null=True, blank=True)