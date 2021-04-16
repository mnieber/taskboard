from django.utils.text import slugify


def generate_unique_slug(klass, field):
    origin_slug = slugify(field)
    unique_slug = origin_slug
    num = 1
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = "{}-{}".format(origin_slug, num)
        num += 1
    return unique_slug
