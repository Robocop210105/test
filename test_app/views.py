from django.http import HttpResponse
from test_app.models import CreditApplication


def get_manufacturer_id(request, id):
    id_contract = id
    response_id = CreditApplication.objects.get(credit_contract__id=id_contract)\
        .products.all()\
        .values_list("manufacturer_name_id", flat=True).distinct()

    return HttpResponse(response_id)
