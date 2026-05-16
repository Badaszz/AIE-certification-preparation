## Function to clean the netflix titles dataset
import os
import logging

import pandas as pd

## Logging config
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

## Acceptable ratings
rating_types = [ 'PG-13','TV-MA', 'PG', 'TV-14', 'TV-PG', 'TV-Y',
            'TV-Y7',  'R',  'TV-G', 'G', 'NC-17', 'NR', 
            'TV-Y7-FV', 'UR']
## Acceptable types
types = ['Movie', 'TV Show']
## Current date (date and release date should not be in the future)
date = pd.to_datetime("today")

## Load the dataset
path = "C:\\Users\\Yusuf Solomon\\.cache\\kagglehub\\datasets\\shivamb\\netflix-shows\\versions\\5"
path_to_dataset = os.path.join(path, "netflix_titles.csv") 

def load_data(path):
    logging.info(f"Loading data from {path}")
    return pd.read_csv(path)

## Inspecting the dataset
def inspect_data(df):
    logging.info("Inspecting the dataset")
    logging.info(f"Dataset shape: {df.shape}")
    logging.info(f"Dataset columns: {df.columns}")
    logging.info(f"Dataset info: {df.info()}")
    logging.info(f"Dataset description: {df.describe()}")

## Cleaning the dataset
def clean_data(df):
    logging.info("Cleaning the Dataset")
    df = df
    
    ## Handling missing values
    logging.info("Handling missing values, replacing them as follows:\n")
    logging.info(f"director: {df['director'].isnull().sum()} null values with 'Unknown'")
    logging.info(f"cast: {df['cast'].isnull().sum()} null values with 'Unknown'")
    logging.info(f"country: {df['country'].isnull().sum()} null values with 'Unknown'")
    logging.info(f"rating: {df['rating'].isnull().sum()} null values with 'Unknown'")
    df.fillna({"director": "Unknown", 
            "cast": "Unknown", 
            "country": "Unknown",
            "rating": "Unknown"}, inplace = True)
    
    ## Drop missing dates
    logging.info(f"Dropping {df['date_added'].isnull().sum()} rows with null values in date_added column")
    df.dropna(subset=["date_added"], inplace = True)
    
    ## Remove duplicate rows
    logging.info(f"Removing duplicate rows, found {df.duplicated().sum()} duplicates")
    df = df.drop_duplicates()
    
    ## Converting the date_added column to datetime format
    df["date_added"] = pd.to_datetime(df["date_added"].str.strip(), format='%B %d, %Y')
    
    logging.info(f"New Info {df.info()}")
    
    return df

def save_data(df, path):
    logging.info(f"Saving cleaned data to {path}")
    df.to_csv(path, index=False)
    
if __name__ == "__main__":
    df = load_data(path_to_dataset)
    inspect_data(df)
    cleaned_df = clean_data(df)
    save_data(cleaned_df, "netflix_titles_cleaned2.csv")