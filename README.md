# 🏦 Personal Finance Tracker

A comprehensive web application built with Django that helps users track their income and expenses, visualize financial data through interactive charts, and manage their personal finances effectively.

## 🚀 **Live Demo**

**🌐 [View Live Application](https://muneeb01500.pythonanywhere.com/)**

_Experience the full-featured finance tracker in action! The deployed application showcases all features including real-time charts, transaction management, and responsive design._

---

## 🌟 Features

### 💰 Transaction Management

- **Create, Read, Update, Delete (CRUD)** operations for financial transactions
- **Real-time form validation** with custom business logic (e.g., amount must be positive)
- **Categorized transactions** with predefined categories (Bills, Food, Housing, Salary, etc.)
- **Income vs Expense tracking** with automatic totals calculation
- **Date-based transaction recording** with intuitive date picker

### 📊 Data Visualization & Analytics

- **Interactive Charts** powered by Plotly.js:
  - Bar charts comparing total income vs expenses
  - Pie charts showing income distribution by category
  - Pie charts showing expense distribution by category
- **Real-time financial summary** displaying:
  - Total income
  - Total expenses
  - Net income (profit/loss)
  - Transaction count

### 🔍 Advanced Filtering & Search

- **Multi-criteria filtering**:
  - Filter by transaction type (Income/Expense)
  - Date range filtering (start date to end date)
  - Category-based filtering with multi-select
- **Real-time filtering** without page refresh using HTMX

### 📈 Data Import/Export

- **CSV Export** functionality for financial data backup
- **Django Import-Export** integration for data management
- **Bulk data generation** with management commands for testing

### 🚀 Modern UI/UX

- **Responsive design** with Tailwind CSS and DaisyUI components
- **HTMX integration** for seamless, SPA-like user experience
- **Infinite scrolling** with pagination for large datasets
- **Loading indicators** and smooth transitions
- **Real-time form validation** with error display

### 🔐 User Authentication & Security

- **Django Allauth integration** for comprehensive auth system
- **User registration, login, logout** functionality
- **User-specific data isolation** - users only see their own transactions
- **Session-based authentication** with proper security measures

### 🧪 Testing & Quality Assurance

- **Comprehensive test suite** with pytest
- **Factory-based test data generation** using Factory Boy
- **View testing** with authentication and database interactions
- **Form validation testing** ensuring business rules are enforced
- **Filter functionality testing** for data integrity

## 🛠 Technical Stack

### Backend

- **Django 5.2** - Web framework
- **Python 3.12** - Programming language
- **SQLite** - Database (development)
- **Django ORM** - Database abstraction layer

### Frontend

- **HTML5/CSS3** - Markup and styling
- **Tailwind CSS** - Utility-first CSS framework
- **DaisyUI** - Component library for Tailwind
- **HTMX** - Modern web interactions without JavaScript frameworks
- **Plotly.js** - Interactive data visualization

### Key Django Packages

- **django-allauth** - Authentication system
- **django-filter** - Advanced filtering capabilities
- **django-htmx** - HTMX integration for Django
- **widget-tweaks** - Enhanced form rendering
- **django-extensions** - Additional Django management commands
- **import-export** - Data import/export functionality
- **template-partials** - Partial template rendering
- **factory-boy** - Test data generation
- **pytest-django** - Testing framework

## 🏗 Architecture & Design Patterns

### Model Design

```python
# Custom User model extending AbstractUser
class User(AbstractUser):
    pass

# Transaction model with business logic
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
```

### Custom QuerySet Managers

- **TransactionQuerySet** with custom methods:
  - `get_total_income()` - Calculate total income
  - `get_total_expenses()` - Calculate total expenses
  - `get_income()` - Filter income transactions
  - `get_expenses()` - Filter expense transactions

### Advanced Filtering System

```python
class TransactionFilter(django_filters.FilterSet):
    transaction_type = django_filters.ChoiceFilter(...)
    start_date = django_filters.DateFilter(...)
    end_date = django_filters.DateFilter(...)
    category = django_filters.ModelMultipleChoiceFilter(...)
```

### Chart Generation System

- **Modular charting functions** using Plotly
- **Dynamic chart titles** based on data context
- **Server-side chart generation** with client-side rendering

## 📱 User Interface Features

### Dashboard Overview

- Clean, modern interface with dark theme
- Financial summary cards showing key metrics
- Quick action buttons for common tasks

### Transaction Management

- **Modal-style forms** for creating/editing transactions
- **Inline editing** capabilities
- **Confirmation dialogs** for destructive actions
- **Success notifications** for user feedback

### Responsive Design

- **Mobile-first approach** with responsive breakpoints
- **Touch-friendly interface** elements
- **Optimized for various screen sizes**

## 🔧 Installation & Setup

### Prerequisites

- Python 3.12+
- pip (Python package manager)
- Git

### Installation Steps

1. **Clone the repository**

```bash
git clone https://github.com/M-MuneebAlam/django-finance-tracker.git
cd django-finance-tracker
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Database setup**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser**

```bash
python manage.py createsuperuser
```

6. **Create default categories**

```bash
python manage.py create_categories
```

7. **Generate sample data (optional)**

```bash
python manage.py generate_sample_data --count 30
```

8. **Run development server**

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the application.

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=tracker

# Run specific test file
pytest tracker/tests/test_views.py

# Run with verbose output
pytest -v
```

## 📊 Usage Examples

### Creating Transactions

1. Navigate to the transactions page
2. Click the "+" button to add a new transaction
3. Fill in amount, category, type, and date
4. Submit the form for real-time validation

### Filtering Data

- Use the sidebar filters to narrow down transactions
- Apply date ranges for specific periods
- Filter by categories or transaction types
- Filters update results in real-time

### Viewing Analytics

- Visit the charts page for visual insights
- Interactive charts show income vs expense trends
- Category-wise breakdowns help identify spending patterns

## 🚀 Production Deployment

### Production Environment Features

- ✅ **Optimized Dependencies** - Production-ready requirements.txt with dev dependencies commented out
- ✅ **Security Hardened** - `DEBUG = False`, proper SECRET_KEY configuration
- ✅ **Database Management** - Production database with management commands
- ✅ **Static File Serving** - Properly configured static files
- ✅ **Sample Data Generation** - Management commands for demo data creation

### Deployment Architecture

**Platform:** PythonAnywhere  
**Database:** SQLite (Production-optimized)  
**Static Files:** Properly configured and served  
**Environment:** Production-grade Django settings

### Management Commands

```bash
# Create default categories
python manage.py create_categories

# Generate sample transactions (production-safe, no external dependencies)
python manage.py generate_sample_data --count 50

# Create superuser for admin access
python manage.py createsuperuser
```

### Security Features

- CSRF protection enabled
- User authentication required for all financial data
- SQL injection protection via Django ORM
- XSS protection with template escaping
- Production-grade user management system

## 🎯 Key Learning Outcomes

This project demonstrates proficiency in:

### Django Framework

- **Model relationships** and custom managers
- **Form handling** with validation
- **Authentication** and user management
- **Template system** with inheritance
- **URL routing** and view design

### Modern Web Development

- **HTMX integration** for dynamic interfaces
- **Responsive design** principles
- **AJAX-like interactions** without JavaScript
- **Component-based UI** development

### Data Management

- **Database design** and optimization
- **Query optimization** with select_related
- **Data filtering** and pagination
- **Import/export** functionality

### Testing & Quality

- **Test-driven development** practices
- **Factory pattern** for test data
- **Mock objects** and fixtures
- **Code coverage** analysis

## 📝 Future Enhancements

- **Budget planning** and goal setting
- **Recurring transactions** automation
- **Multi-currency** support
- **Email notifications** for financial milestones
- **Advanced reporting** with PDF generation
- **Mobile app** development
- **API development** for third-party integrations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Muneeb Alam**

- 📂 **GitHub:** [@M-MuneebAlam](https://github.com/M-MuneebAlam)
- 📧 **Email:** [mmuneeb.alam09@gmail.com]

## 🎖️ Project Highlights

### 🏆 **Production-Ready Application**

This isn't just a demo - it's a **fully deployed, production-grade application** showcasing:

- ✨ **Modern UI/UX** with glassmorphism design and responsive layouts
- 📊 **Interactive Data Visualization** using Plotly.js with real-time updates
- 🔐 **Complete Authentication System** with user registration and secure login
- 💾 **Robust Data Management** with advanced filtering and CSV export
- 🚀 **HTMX Integration** for smooth, SPA-like interactions without JavaScript frameworks
- 📱 **Mobile-First Design** optimized for all devices and screen sizes

### 💡 **Technical Excellence**

- **Clean Architecture** following Django best practices
- **Comprehensive Testing** with pytest and factory-boy
- **Production Optimization** with dependency management and security hardening
- **Scalable Design** with custom QuerySets and efficient database queries

---

_This project demonstrates enterprise-level Django development skills with modern web technologies, showcasing the ability to build, test, and deploy production-ready applications._
