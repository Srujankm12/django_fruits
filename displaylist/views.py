from django.shortcuts import render
from django.http import HttpResponse
def lists_view(request):
    fruits = ['Apple', 'Date', 'Cherry','Banana']
    students = ['Alice', 'Diana', 'Charlie','Bob']
    context = {
        'fruits': fruits,


        'students': students,
}
    return render(request, 'lists.html', context)