#!/usr/bin/env python

import numpy as np
import pandas as pd

DATA_CSV_FILE = 'data/input.csv'

def main() -> None:
  df = pd.read_csv(DATA_CSV_FILE, lineterminator='\n')

  print("--- HEAD ---")
  print(df.head())
  print("--- INFO ---")
  print(df.info())
  print("--- DESCRIPTION ---")
  print(df.describe())
  print("--- NULL VALUES ---")
  print(df.isnull().sum())

  df.drop()
  df.drop_duplicates(inplace=True)
  df.dropna(inplace=True)
  df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
  df = df.fillna('')

if __name__ == '__main__':
  print("Hello World!")
