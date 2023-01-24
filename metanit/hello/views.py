from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import students


# получение данных из бд
def index(request):
    people = students.objects.order_by("LastName")
    return render(request, "index.html", {"people": people})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        person = students()
        person.LastName = request.POST.get("LastName")
        person.FirstName = request.POST.get("FirstName")
        person.MiddleName = request.POST.get("MiddleName")
        person.Arrd1 = request.POST.get("Arrd1")
        person.Arrd2 = request.POST.get("Arrd2")
        person.City = request.POST.get("City")
        person.StateProvince = request.POST.get("StateProvince")
        person.Country = request.POST.get("Country")
        person.PostalCode = request.POST.get("PostalCode")
        person.Email = request.POST.get("Email")

        person.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        person = students.objects.get(id=id)

        if request.method == "POST":
            person.LastName = request.POST.get("LastName")
            person.FirstName = request.POST.get("FirstName")
            person.MiddleName = request.POST.get("MiddleName")
            person.Arrd1 = request.POST.get("Arrd1")
            person.Arrd2 = request.POST.get("Arrd2")
            person.City = request.POST.get("City")
            person.StateProvince = request.POST.get("StateProvince")
            person.Country = request.POST.get("Country")
            person.PostalCode = request.POST.get("PostalCode")
            person.Email = request.POST.get("Email")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except students.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        person = students.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except students.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")