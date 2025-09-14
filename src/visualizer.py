"""
visualizer.py

This module contains functions for creating visualizations for sales data analysis.
"""

import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_matrix(df, figsize=(10,8), cmap='coolwarm'):
    """
    Plot a correlation matrix heatmap.
    
    Args:
        df (pd.DataFrame): DataFrame with numerical data.
        figsize (tuple): Figure size.
        cmap (str): Colormap.
    """
    corr = df.corr()
    plt.figure(figsize=figsize)
    sns.heatmap(corr, annot=True, cmap=cmap)
    plt.title('Correlation Matrix')
    plt.show()

def plot_monthly_sales_trend(df, date_col='Order Date', sales_col='Sales', figsize=(12,6)):
    """
    Plot monthly sales trend as a time series.
    
    Args:
        df (pd.DataFrame): DataFrame with sales data.
        date_col (str): Name of the date column.
        sales_col (str): Name of the sales column.
        figsize (tuple): Figure size.
    """
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df.set_index(date_col, inplace=True)
    monthly_sales = df[sales_col].resample('M').sum()
    plt.figure(figsize=figsize)
    monthly_sales.plot()
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.show()

def plot_sales_by_category(df, category_col='Category', sales_col='Sales', ax=None):
    """
    Plot sales by category as a bar plot.
    
    Args:
        df (pd.DataFrame): DataFrame with sales data.
        category_col (str): Name of the category column.
        sales_col (str): Name of the sales column.
        ax (matplotlib.axes.Axes): Axes to plot on.
    """
    if ax is None:
        plt.figure(figsize=(8,6))
        ax = plt.gca()
    sns.barplot(x=category_col, y=sales_col, data=df, ax=ax)
    ax.set_title('Sales by Category')

def plot_profit_by_region(df, region_col='Region', profit_col='Profit', ax=None):
    """
    Plot profit by region as a bar plot.
    
    Args:
        df (pd.DataFrame): DataFrame with sales data.
        region_col (str): Name of the region column.
        profit_col (str): Name of the profit column.
        ax (matplotlib.axes.Axes): Axes to plot on.
    """
    if ax is None:
        plt.figure(figsize=(8,6))
        ax = plt.gca()
    sns.barplot(x=region_col, y=profit_col, data=df, ax=ax)
    ax.set_title('Profit by Region')

def plot_profit_margin_distribution(df, profit_margin_col='Profit Margin', ax=None, bins=30):
    """
    Plot distribution of profit margin.
    
    Args:
        df (pd.DataFrame): DataFrame with sales data.
        profit_margin_col (str): Name of the profit margin column.
        ax (matplotlib.axes.Axes): Axes to plot on.
        bins (int): Number of bins.
    """
    if ax is None:
        plt.figure(figsize=(8,6))
        ax = plt.gca()
    sns.histplot(df[profit_margin_col], bins=bins, ax=ax)
    ax.set_title('Profit Margin Distribution')
