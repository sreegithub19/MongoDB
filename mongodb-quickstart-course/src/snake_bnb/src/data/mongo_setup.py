import mongoengine

# this file is to make mongoengine communicate with mongodb


def global_init():
    mongoengine.register_connection(alias='core', name='snake_bnb')
