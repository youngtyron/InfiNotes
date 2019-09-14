class ModelMetaRouter(object):
    def db_for_read(self, model, **hints):

        db = getattr(model._meta, 'in_db', None)
        if db:
            return db
        else:
            return 'default'

    def db_for_write(self, model, **hints):
        db = getattr(model._meta, 'in_db', None)
        if db:
            return db
        else:
            return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if getattr(obj1._meta, 'in_db', None) == getattr(obj2._meta, 'in_db', None):
            return True
        return None

    def allow_syncdb(self, db, model):
        if db == getattr(model._meta, 'in_db', 'default'):
            return True
        return None
