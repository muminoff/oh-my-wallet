from django.shortcuts import render
from django import http
from core.models import Category, Expense


def all_expenses(request):
    context = {
        'all_expenses': Expense.objects.all(),
        'all_categories': Category.objects.all()
    }
    return render(request, 'all_expenses.html', context)
