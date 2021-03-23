from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Poll


# Create your views here.
class PollDetailView(View):
    template_name = "polls/poll_detail.html"

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Poll, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     return render(request, 'about.html', {})


def my_fbv(request, *args, **kwargs):
    print(request.method)
    return render(request, 'about.html', {})
