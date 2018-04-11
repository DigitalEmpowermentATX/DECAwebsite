from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from flagging.forms import FlagForm

# Create your views here.
def flag(request: HttpRequest):
    if request.method == "POST":
        flag_form = FlagForm(request.POST)
        if flag_form.is_valid():
            # print(flag_form)
            flag_form.save()
        else:
            print(flag_form)
            print(flag_form.org_id)
            print(flag_form.other)
            print(flag_form.issue)
            print(flag_form.errors)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return Http404()
