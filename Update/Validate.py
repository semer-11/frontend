from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Validate:
    def validateProfileUpdate(request):
        return Validate.emailExists(request)
        # try:
        #     if request.POST['email'] == None:
        #         return HttpResponse("We are good")
        #     else:
        #         raise ValidationError(
        #             request.user,
        #             params={'value': "sfdfd"},
        #         )
        # except ValidationError as e:
        #     return HttpResponse(e.message)

    def emailExists(request):
        user = User.objects.get(email=request.user.email)
        return user
