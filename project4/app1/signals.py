from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

from django.db.models.signals import pre_init, pre_save, pre_delete, pre_migrate, post_init, post_save, post_delete, post_migrate

from django.core.signals import request_started, request_finished, got_request_exception

@receiver(user_logged_in, sender=User)
def login_successs(sender, request, user, **kwargs):
    print("****login signal****")
    print('sender  :',sender)
    print('request :',request)
    print('User :',user)
    print('User :',user.password)
    print(f'Kwargs: {kwargs}')

# user_logged_in.connect(login_successs, sender=User)


def logout_successs(sender, request, user, **kwargs):
    print("****logout signal****")
    print('sender  :',sender)
    print('request :',request)
    print('User :',user)
    print(f'Kwargs: {kwargs}')

user_logged_out.connect(logout_successs, sender=User)

def login_failed(sender, credentials, request, **kwargs):
    print("****login failed****")
    print('sender  :',sender)
    print('request :',request)
    print('User :',credentials)
    print(f'Kwargs: {kwargs}')

user_login_failed.connect(login_failed)


@receiver(pre_save, sender=User)
def at_begin_save(sender, instance, **kwargs):
    print("**at_begin_save**")
    print('instance : ', instance)
    print('instance password : ', instance.password)



@receiver(request_started)
def at_request_started(sender, environ, **kwargs):
    print("**at_request_started**")
    # print('instance : ', environ)
    print(f'Kwargs: {kwargs}')


@receiver(request_finished)
def at_request_finished(sender, **kwargs):
    print("**at_request_finished**")
    print(f'Kwargs: {kwargs}')


@receiver(got_request_exception)
def at_request_exception(sender, request, **kwargs):
    print("**at_request_exception**")
    print(f'Kwargs: {kwargs}')

