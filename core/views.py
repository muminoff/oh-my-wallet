from django.shortcuts import render
from django import http
from core.models import Category, Expense


def get_this_month_expenses(request):
    context = {
        'expenses': Expense.objects.all()
    }
    # return render(request, 'this_month_expenses.html', context)
    return http.HttpResponse(context)
