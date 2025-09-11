import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from tracker.models import User, Transaction, Category


class Command(BaseCommand):
    help = "Generates sample transactions without external dependencies"

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=20, help='Number of transactions to create')

    def handle(self, *args, **options):
        count = options['count']
        
        # Get the first superuser
        user = User.objects.filter(is_superuser=True).first()
        if not user:
            self.stdout.write(
                self.style.ERROR("No superuser found. Please create one first using: python manage.py createsuperuser")
            )
            return

        # Ensure we have categories
        if not Category.objects.exists():
            self.stdout.write(
                self.style.ERROR("No categories found. Please run: python manage.py create_categories")
            )
            return

        categories = Category.objects.all()
        types = [x[0] for x in Transaction.TRANSACTION_TYPE_CHOICES]
        
        # Generate random dates within the last year
        today = date.today()
        start_date = today - timedelta(days=365)
        
        created_count = 0
        for i in range(count):
            # Random date between start_date and today
            random_days = random.randint(0, 365)
            transaction_date = start_date + timedelta(days=random_days)
            
            # Random amount between $1 and $2500
            amount = round(random.uniform(1, 2500), 2)
            
            Transaction.objects.create(
                category=random.choice(categories),
                user=user,
                amount=amount,
                date=transaction_date,
                type=random.choice(types)
            )
            created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} sample transactions for user: {user.username}')
        )
