from django.shortcuts import render
from django.http import HttpResponseRedirect
from phonebook.models import Phonebook


def phones_table(request):
    if request.method == "GET":
        data = Phonebook.objects.all()

        return render(
            request,
            'phones_table.html',
            context={
                'entries': data,
            },
        )

    if request.method == "POST":
        data = {
            "phone_number": request.POST["phone_number"],
            "fullname": request.POST["fullname"],
            "position": request.POST["position"],
        }

        Phonebook.objects.create(**data)

        return HttpResponseRedirect("/")


def update_entry(request, entry_id):
    if request.method == "GET":
        data = Phonebook.objects.get(pk=entry_id)

        return render(
            request,
            'update_form.html',
            context={
                'phone_number': data.phone_number,
                'fullname': data.fullname,
                'position': data.position,
            },
        )

    if request.method == "POST":
        instance = Phonebook.objects.get(pk=entry_id)

        instance.phone_number = request.POST["phone_number"]
        instance.fullname = request.POST["fullname"]
        instance.position = request.POST["position"]

        instance.save()

        return HttpResponseRedirect("/")


def delete_entry(request, entry_id):
    if request.method == "POST":
        instance = Phonebook.objects.get(pk=entry_id)

        instance.delete()

        return HttpResponseRedirect("/")
