from django.test import TestCase
from core.models import Category, Expense


class TestCategory(TestCase):

    def test_category(self):
        category = Category()
        category.name = 'Test category'
        assert(category.name == 'Test category')



class TestExpense(TestCase):
    
    def test_expense(self):
        food_category = Category.objects.create(name='Food')
        expense = Expense()
        expense.name = 'Toast bread'
        expense.category = food_category
        expense.amount = 9
        expense.price = 2400
        expense.save()
        print expense.name, expense.get_sum, expense.paid
        assert(expense.get_sum == 21600)
