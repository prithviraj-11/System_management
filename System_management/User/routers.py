class UserRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'User':
            return 'userdb'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'User':
            return 'userdb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'User' and obj2._meta.app_label == 'User':
            return True
        elif 'User' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'User':
            return db == 'userdb'
        elif db == 'userdb':
            return False
        return None