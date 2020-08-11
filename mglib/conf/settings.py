import importlib

try:
    from django.conf import settings as django_settings
except ImportError:
    # Operating outside django, use own settings module
    django_settings = None


class DefaultSettings:

    def __init__(
        self,
        settings_module="mglib.conf.default_settings"
    ):
        self.SETTINGS_MODULE = settings_module

        mod = importlib.import_module(
            self.SETTINGS_MODULE
        )

        for setting in dir(mod):
            if setting.isupper():
                setting_value = getattr(mod, setting)
                setattr(self, setting, setting_value)

    def configure(self, **options):
        for name, value in options.items():
            setattr(self, name, value)


class MgLibSettings:

    def __init__(
        self, default_settings
    ):
        self.default_settings = default_settings

    def __getattr__(self, name):
        # When operating withing django,
        # get configuration from django settings
        if not name.isupper():
            raise AttributeError

        if django_settings:
            val = getattr(django_settings, name)
            return val

        val = getattr(self.default_settings, name)
        return val

    def configure(self, **options):
        self.default_settings.configure(
            **options
        )
