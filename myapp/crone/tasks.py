from myapp.models import ProductTypes


def my_crone_task():
    data = {
        "name": "Sarfraz Saleem Rajpoot ",
        "price": "Muhammad Sheraz",
        "discount": "Muhammad Imtiaz"
    }
    ProductTypes.objects.update_or_create(data)
    return data
