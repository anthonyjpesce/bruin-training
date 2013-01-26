from django.core.management.base import BaseCommand, CommandError
from admissions.models import Year
import csv

class Command(BaseCommand):
    help = 'Loads our CSV into the database'

    def clean(self, string):
        """
        Takes an integer or float as a string, then returns the
        appropriate type.
        """
        if string == '':
            return None
        try:
            return int(string)
        except ValueError:
            return float(string)

    def handle(self, *args, **options):
        # open up our CSV
        data_file = open('admissions/data/ucla_data.csv', 'rU')
        # parse it with the Python CSV module
        rdr = csv.DictReader(data_file)
        for i in rdr:
            year = Year.objects.create(
                year = self.clean(i.get('year')),
                african_american_applicants = self.clean(i.get('african_american_applicants')),
                african_american_admits = self.clean(i.get('african_american_admits')),
                african_american_enrollees = self.clean(i.get('african_american_enrollees')),
                african_american_admit_rate = self.clean(i.get('african_american_admit_rate')),
                african_american_yield = self.clean(i.get('african_american_yield')),
                american_indian_applicants = self.clean(i.get('american_indian_applicants')),
                american_indian_admits = self.clean(i.get('american_indian_admits')),
                american_indian_enrollees = self.clean(i.get('american_indian_enrollees')),
                american_indian_admit_rate = self.clean(i.get('american_indian_admit_rate')),
                american_indian_yield = self.clean(i.get('american_indian_yield')),
                asian_american_applicants = self.clean(i.get('asian_american_applicants')),
                asian_american_admits = self.clean(i.get('asian_american_admits')),
                asian_american_enrollees = self.clean(i.get('asian_american_enrollees')),
                asian_american_admit_rate = self.clean(i.get('asian_american_admit_rate')),
                asian_american_yield = self.clean(i.get('asian_american_yield')),
                chicano_latino_applicants = self.clean(i.get('chicano_latino_applicants')),
                chicano_latino_admits = self.clean(i.get('chicano_latino_admits')),
                chicano_latino_enrollees = self.clean(i.get('chicano_latino_enrollees')),
                chicano_latino_admit_rate = self.clean(i.get('chicano_latino_admit_rate')),
                chicano_latino_yield = self.clean(i.get('chicano_latino_yield')),
                white_applicants = self.clean(i.get('white_applicants')),
                white_admits = self.clean(i.get('white_admits')),
                white_enrollees = self.clean(i.get('white_enrollees')),
                white_admit_rate = self.clean(i.get('white_admit_rate')),
                white_yield = self.clean(i.get('white_yield')),
                other_applicants = self.clean(i.get('other_applicants')),
                other_admits = self.clean(i.get('other_admits')),
                other_enrollees = self.clean(i.get('other_enrollees')),
                other_admit_rate = self.clean(i.get('other_admit_rate')),
                other_yield = self.clean(i.get('other_yield')),
                unknown_applicants = self.clean(i.get('unknown_applicants')),
                unknown_admits = self.clean(i.get('unknown_admits')),
                unknown_enrollees = self.clean(i.get('unknown_enrollees')),
                unknown_admit_rate = self.clean(i.get('unknown_admit_rate')),
                unknown_yield = self.clean(i.get('unknown_yield')),
                international_applicants = self.clean(i.get('international_applicants')),
                international_admits = self.clean(i.get('international_admits')),
                international_enrollees = self.clean(i.get('international_enrollees')),
                international_admit_rate = self.clean(i.get('international_admit_rate')),
                international_yield = self.clean(i.get('international_yield')),
                total_applicants = self.clean(i.get('total_applicants')),
                total_admits = self.clean(i.get('total_admits')),
                total_enrollees = self.clean(i.get('total_enrollees')),
                total_admit_rate = self.clean(i.get('total_admit_rate')),
                total_yield = self.clean(i.get('total_yield')),
            )
            print "loaded %s" % year.year
        print "Done!"
