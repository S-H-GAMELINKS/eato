from django import template

register = template.Library()

@register.filter(name='is_liked')
def is_liked(review, user):
    return review.is_liked(user)
