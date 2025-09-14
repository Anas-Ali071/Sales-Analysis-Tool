"""
utils.py

This module contains helper functions for data validation, error handling, and common utilities.
"""

def validate_dataframe(df, required_columns):
    """
    Validate that the DataFrame contains the required columns.
    
    Args:
        df (pd.DataFrame): DataFrame to validate.
        required_columns (list): List of required column names.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        print(f"DataFrame is missing required columns: {missing_cols}")
        return False
    return True

def handle_missing_values(df, strategy='median', columns=None):
    """
    Handle missing values in the DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame to process.
        strategy (str): Strategy to fill missing values ('median', 'mean', 'mode', 'drop').
        columns (list): List of columns to apply the strategy on. If None, apply to all.
        
    Returns:
        pd.DataFrame: DataFrame with missing values handled.
    """
    if columns is None:
        columns = df.columns
    for col in columns:
        if strategy == 'median':
            median_val = df[col].median()
            df[col].fillna(median_val, inplace=True)
        elif strategy == 'mean':
            mean_val = df[col].mean()
            df[col].fillna(mean_val, inplace=True)
        elif strategy == 'mode':
            mode_val = df[col].mode()[0]
            df[col].fillna(mode_val, inplace=True)
        elif strategy == 'drop':
            df.dropna(subset=[col], inplace=True)
        else:
            print(f"Unknown strategy: {strategy} for column: {col}")
    return df
