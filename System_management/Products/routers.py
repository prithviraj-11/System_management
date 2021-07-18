class ProductRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'Products':
            return 'productdb'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'Products':
            return 'productdb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'Products' and obj2._meta.app_label == 'Products':
            return True
        elif 'Products' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'Products':
            return db == 'productdb'
        elif db == 'productdb':
            return False
        return None