import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from django.db.models import Sum
from .models import Category

def plot_income_expense_bar_chart(qs):
    """Create a modern bar chart comparing income vs expenses with professional styling"""
    x_vals = ['Income', 'Expenses']

    # sum up the total income and expenditure
    total_income = qs.filter(type='income').aggregate(
        total=Sum('amount')
    )['total'] or 0
    
    total_expense = qs.filter(type='expense').aggregate(
        total=Sum('amount')
    )['total'] or 0
    
    # Create modern bar chart with custom colors
    fig = go.Figure(data=[
        go.Bar(
            x=x_vals,
            y=[total_income, total_expense],
            marker_color=['#10b981', '#ef4444'],  # Green for income, red for expenses
            text=[f'${total_income:,.2f}', f'${total_expense:,.2f}'],
            textposition='auto',
            textfont=dict(color='white', size=14, family='Arial Black'),
            hovertemplate='<b>%{x}</b><br>' +
                         'Amount: $%{y:,.2f}<br>' +
                         '<extra></extra>',
        )
    ])
    
    # Update layout for modern appearance
    fig.update_layout(
        title={
            'text': 'Income vs Expenses Overview',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': 'white', 'family': 'Arial Black'}
        },
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(
            title='Transaction Type',
            title_font=dict(size=14, color='white'),
            tickfont=dict(size=12, color='white'),
            gridcolor='rgba(255,255,255,0.1)'
        ),
        yaxis=dict(
            title='Amount ($)',
            title_font=dict(size=14, color='white'),
            tickfont=dict(size=12, color='white'),
            gridcolor='rgba(255,255,255,0.1)'
        ),
        margin=dict(l=40, r=40, t=60, b=40),
        height=400,
    )

    return fig


def plot_category_pie_chart(qs, title="Total Amount per Category"):
    """Create a modern pie chart with professional styling and better colors"""
    count_per_category = (
        qs.order_by('category').values('category')
        .annotate(total=Sum('amount'))
    )

    category_pks = count_per_category.values_list('category', flat=True).order_by('category')
    categories = Category.objects.filter(pk__in=category_pks).order_by('pk').values_list('name', flat=True)
    total_amounts = count_per_category.order_by('category').values_list('total', flat=True)

    # Modern color palette
    colors = [
        '#10b981', '#3b82f6', '#8b5cf6', '#f59e0b', 
        '#ef4444', '#06b6d4', '#84cc16', '#f97316',
        '#ec4899', '#6366f1', '#14b8a6', '#eab308'
    ]

    if not total_amounts:
        # Create empty chart with message
        fig = go.Figure()
        fig.add_annotation(
            text="No data available for the selected filters",
            xref="paper", yref="paper",
            x=0.5, y=0.5, xanchor='center', yanchor='middle',
            showarrow=False,
            font=dict(size=16, color='white'),
            bgcolor='rgba(255,255,255,0.1)',
            bordercolor='rgba(255,255,255,0.2)',
            borderwidth=1
        )
    else:
        fig = go.Figure(data=[
            go.Pie(
                labels=list(categories),
                values=list(total_amounts),
                hole=0.4,  # Donut chart style
                marker_colors=colors[:len(categories)],
                textinfo='label+percent+value',
                texttemplate='<b>%{label}</b><br>%{percent}<br>$%{value:,.0f}',
                textfont=dict(size=11, color='white'),
                hovertemplate='<b>%{label}</b><br>' +
                             'Amount: $%{value:,.2f}<br>' +
                             'Percentage: %{percent}<br>' +
                             '<extra></extra>',
            )
        ])

    # Update layout for modern appearance
    fig.update_layout(
        title={
            'text': title,
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16, 'color': 'white', 'family': 'Arial Black'}
        },
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        margin=dict(l=20, r=20, t=60, b=20),
        height=350,
        showlegend=False,  # Remove legend to save space
    )

    return fig