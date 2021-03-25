from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Poll
from .forms import PollModelForm


# Create your views here.
class PollCreateView(View):
    template_name = "polls/poll_create.html"

    def get(self, request, *args, **kwargs):
        form = PollModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = PollModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = PollModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)


class PollListView(View):
    template_name = "polls/poll_list.html"
    queryset = Poll.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)


class MyListView(PollListView):
    queryset = Poll.objects.filter(id=1)


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
