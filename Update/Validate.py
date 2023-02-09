from django.http import HttpResponse
from django.core.exceptions import ValidationError


class Validate:
    def validate():
        try:
            raise ValidationError(
                "fddf",
                params={'value': "sfdfd"},
            )
        except ValidationError as e:
            return HttpResponse(e.message)
