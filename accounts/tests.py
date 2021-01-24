from django.test import TestCase
from django.test.runner import DiscoverRunner
from account.conf import AccountAppConf

class MyTestDiscoverRunner(DiscoverRunner):
    def setup_test_environment(self, **kwargs):
        super(MyTestDiscoverRunner, self).setup_test_environment(**kwargs)
        aac = AccountAppConf()
        aac.CREATE_ON_SAVE = False