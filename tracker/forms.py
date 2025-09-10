from django import forms
from .models import Transaction, Category


class TransactionForm(forms.ModelForm):
    
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), 
        widget=forms.Select(attrs={
            'class': 'select w-full bg-secondary-700 text-white border-white/20 focus:border-emerald-400 focus:ring-emerald-400/20 rounded-xl [&>option]:bg-secondary-700 [&>option]:text-white'
        }),
        empty_label="Select a category"
    )
    
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")
        return amount

    class Meta:
        model = Transaction
        fields = ['type', 'amount', 'date', 'category']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }