import matplotlib as mpl
import pandas as pd
import csv
from typing import Tuple
from print_color import print


def data_extraction() -> Tuple[pd.DataFrame, list]:
    """ Extract data from data.csv using pandas.read_csv() and the python csv module

    * Use pandas.read_csv() to take the data from the file 'data.csv'
    * Print the head (five first entries) of the data
    * Use the python csv module to take the data from the file 'data.csv'
    * Remove the first entry line that corresponds to the labels 'km,price'
    * Print the head (five first entries) of the data

    Return
    -----
        data_pandas (pandas.DataFrame): the data extracted using pandas
        data_vanilla (list): the data extracted using csv
    """

    print("Reading data from data.csv (using pandas.read_csv())", tag='information', tag_color='green', color='white')

    data_pandas = pd.read_csv("data/data.csv")
    print(data_pandas[:5], tag='data', tag_color='magenta', color='white')

    print("\n")
    print("Reading data from data.csv (using python csv module)", tag='information', tag_color='green', color='white')

    with open("data/data.csv", 'r') as data_file:
        reader = csv.reader(data_file)
        data_vanilla = list(reader)

    del data_vanilla[0]
    print(data_vanilla[:5], tag='data', tag_color='magenta', color='white')


    return data_pandas, data_vanilla


def main():

    data_pandas, data_vanilla = data_extraction()


if __name__ == "__main__":
    main()
