

import pandas as pd
import numpy as np

def clean_data():
    df = pd.read_csv('data/raw_data.csv')
    
    # Clean columns
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    
    # Create synthetic 'quantity_sold' and 'order_value'
    df['quantity_sold'] = np.random.randint(1, 10, size=len(df))
    df['order_value'] = df['price'] * df['quantity_sold']
    
    df.to_csv('data/cleaned_data.csv', index=False)
    print("Cleaned data saved successfully!")

if __name__ == "__main__":
    clean_data()
