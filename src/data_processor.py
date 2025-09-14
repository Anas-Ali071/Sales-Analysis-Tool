"""
data_processor.py

This module contains functions for loading, inspecting, and processing sales data.
"""

import pandas as pd

def load_csv(filepath):
    """
    Load data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(filepath)
        print(f"CSV data loaded successfully from {filepath}")
        return data
    except Exception as e:
        print(f"Error loading CSV data: {e}")
        return None

def load_excel(filepath):
    """
    Load data from an Excel file.
    
    Args:
        filepath (str): Path to the Excel file.
        
    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_excel(filepath)
        print(f"Excel data loaded successfully from {filepath}")
        return data
    except Exception as e:
        print(f"Error loading Excel data: {e}")
        return None

def initial_exploration(df):
    """
    Perform initial data exploration: shape, info, describe.
    
    Args:
        df (pd.DataFrame): DataFrame to explore.
        
    Returns:
        dict: Summary statistics and info as strings.
    """
    try:
        shape = df.shape
        info_buf = []
        df.info(buf=info_buf)
        info_str = "\n".join(info_buf)
        description = df.describe(include='all').to_string()
        return {
            "shape": shape,
            "info": info_str,
            "description": description
        }
    except Exception as e:
        print(f"Error during initial exploration: {e}")
        return None

def missing_values_summary(df):
    """
    Summarize missing values per column.
    
    Args:
        df (pd.DataFrame): DataFrame to check.
        
    Returns:
        pd.Series: Count of missing values per column.
    """
    return df.isnull().sum()
