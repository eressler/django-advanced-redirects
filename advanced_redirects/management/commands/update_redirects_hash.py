import hashlib

from django.core.management import BaseCommand

from advanced_redirects.models import Redirect, Referral


class Command(BaseCommand):

    def handle(self, *args, **options):
        for item in Redirect.objects.all().iterator():
            item.url_hash = hashlib.sha256(item.originating_url.encode('utf-8')).hexdigest()
            item.save()
            print 'id:', item.id, '(', item.url_hash, ')'


        # string_val = "x" * 300
        # r1 = Redirect(originating_url=string_val + '1')
        # r1.save()
        #
        # r2 = Redirect(originating_url=string_val + '2')
        # r2.save()
