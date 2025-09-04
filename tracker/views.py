from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .filters import TransactionFilter

# Create your views here.
def index(request):
    return render(request, 'tracker/index.html')


@login_required
def transactions_list(request):
    transaction_filter = TransactionFilter(
        request.GET,
        queryset=Transaction.objects.filter(user=request.user).select_related('category')
    )

    total_income = transaction_filter.qs.get_total_income()
    total_expense = transaction_filter.qs.get_total_expenses()

    context = {
        'filter': transaction_filter,
        'total_income': total_income,
        'total_expense': total_expense,
        'net_total': total_income - total_expense,
    }

    if request.htmx:
        return render(request, 'tracker/partials/transactions-container.html', context)
    
    return render(request, 'tracker/transactions-list.html', context)
