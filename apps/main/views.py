# Python
from typing import Any

#Django
from django.shortcuts import render
from django.views.generic import (
    View
)
from django.shortcuts import render
from django.http import (
    HttpRequest,
    HttpResponse,
    QueryDict,
)

#Local
from main.models import (
    Pen,
    Stock
)
from main.forms import PenForm


class PenView(View):

    form = PenForm
    
    def get(
        self, 
        request: HttpRequest, 
        *args: tuple, 
        **kwargs: dict
    ) -> HttpResponse:
        return render(
            request = request,
            template_name = 'main/index.html',
            context={
                'ctx_form': self.form()
            }
        )
        
    def post(
        self, 
        request: HttpRequest, 
        *args: tuple, 
        **kwargs: dict
    ) -> HttpResponse:

        data: PenForm = self.form(
            request.POST
        )
        if not data.is_valid():
            return HttpResponse('bad')
        
        data.save()
        
        return HttpResponse("ok")