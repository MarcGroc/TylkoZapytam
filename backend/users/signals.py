# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from users.client.client_models import Client
# from users.expert.expert_models import Expert

# TODO: Uncomment after api tests
# @receiver(post_save, sender=User)
# def create_client_profile(sender, instance, created, **kwargs):
#     user = instance
#     if created:
#         profile = Client(client_id=user)
#         profile.save()
#
#
# @receiver(post_save, sender=User)
# def create_expert_profile(sender, instance, created, **kwargs):
#     user = instance
#     if created:
#         profile = Expert(expert_id=user)
#         profile.save()
