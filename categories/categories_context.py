from categories.models import Categories


def categories_context(request):
    return {
        'categories': Categories.objects.all()
    }
