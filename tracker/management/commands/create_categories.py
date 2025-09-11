from django.core.management.base import BaseCommand
from tracker.models import Category


class Command(BaseCommand):
    help = 'Create default categories for the finance tracker'

    def handle(self, *args, **options):
        categories = [
            # Income Categories
            'Salary',
            'Freelance',
            'Investment Returns',
            'Business Income',
            'Gift/Bonus',
            'Other Income',
            
            # Expense Categories
            'Food & Dining',
            'Transportation',
            'Shopping',
            'Entertainment',
            'Bills & Utilities',
            'Healthcare',
            'Education',
            'Travel',
            'Insurance',
            'Groceries',
            'Rent/Mortgage',
            'Personal Care',
            'Other Expenses',
        ]
        
        created_count = 0
        for category_name in categories:
            category, created = Category.objects.get_or_create(name=category_name)
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created category: {category_name}')
                )
            else:
                self.stdout.write(f'Category already exists: {category_name}')
        
        self.stdout.write(
            self.style.SUCCESS(f'\nSummary: Created {created_count} new categories')
        )
