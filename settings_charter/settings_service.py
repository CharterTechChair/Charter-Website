'''
    Services to provide default settings for things
'''
from settings_charter.models import CharterClubSettings
class DynamicSettingsServices:
    @staticmethod

    def get(key):
        settings_o = get_settings_obj()
        check_if_concrete_field_exists_or_throw(key, settings_o)

        return getattr(settings_o, key)

    @staticmethod
    def get_valid_keys():
        settings_o = get_settings_obj()
        names = [f.get_attname() for f in settings_o._meta.concrete_fields]

        return names

def get_settings_obj():
        query = CharterClubSettings.objects.all()
        check_if_only_one_instance_exists_or_throw(query)
        settings_o = query[0]

        return settings_o

def check_if_only_one_instance_exists_or_throw(query):
    if len(query) != 1:
        raise Exception('Uh, oh. Past Quan set a constraint there there has to exactly one CharterClubSettings object. (there are %s). Either create a new object in django admin, or delete the extra ones.' % len(query))   
    return True

# Documentation: https://docs.djangoproject.com/en/1.9/ref/models/options/#
def check_if_concrete_field_exists_or_throw(key, model_obj):
    names = [f.get_attname() for f in model_obj._meta.concrete_fields]

    if key not in names:
        raise Exception('Looks like key=%s is not in the list of concrete names for this object. Names=%s' % (key, names))   
    return True