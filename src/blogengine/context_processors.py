from django.conf import settings

def disqus(context):
  return {'DISQUS': settings.DISQUS}