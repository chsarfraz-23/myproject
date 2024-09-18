from myapp.models import ProductTypes


def my_crone_task():
    data = {
        "name": "mmmmmmm",
        "price": "Muhammad Sheraz",
        "discount": "Muhammad Imtiaz"
    }
    try:
        ProductTypes.objects.update_or_create(name=data['name'], defaults=data)
        return data
    except Exception as e:
        print(e)

