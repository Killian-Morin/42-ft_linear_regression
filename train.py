import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
from typing import Tuple
from print_color import print


plt.rcParams["axes.grid"] = True # enable grid by default


def data_extraction() -> Tuple[pd.DataFrame, list]:
    """ Extract data from data.csv using pandas.read_csv() and the python csv module

    * Use pandas.read_csv() to take the data from the file 'data.csv'
    * Print the head (five first entries) and the shape of the data
    * Plot the data in a scatter plot
    * Use the python csv module to take the data from the file 'data.csv'
    * Remove the first entry line that corresponds to the labels 'km,price'
    * Print the head (five first entries) and the shape of the data
    * Plot the data in a scatter plot

    * data_array[:, x] -> the ':' takes all elements (rows) of the first dimension
        and only the elements at index 0, then 1 in each row

    Return
    -----
        data_pandas (pandas.DataFrame): the data extracted using pandas
        data_vanilla (list): the data extracted using csv
    """

    print("====================================", color='yellow')
    print("===========DATA EXTRACTION==========", color='yellow')
    print("====================================", color='yellow')

    print("Reading data from data.csv (using pandas.read_csv())", tag='information', tag_color='g', color='w')

    data_frame = pd.read_csv("data/data.csv")
    print(data_frame[:5], tag='data', tag_color='m', color='w')

    print("Shape of km:", data_frame["km"].shape, tag='information', tag_color='g', color='w')
    print("Shape of price:", data_frame["price"].shape, tag='information', tag_color='g', color='w')
    print("Global shape:", data_frame.shape, tag='information', tag_color='g', color='w')

    data_frame.plot.scatter(x="km", y="price", c='b')
    plt.title("Dataset: Mileage vs Price (pandas)")
    plt.xlabel("Mileage (km)")
    plt.ylabel("Price ($)")
    plt.xlim(0, 250000)
    plt.ylim(0, 10000)
    plt.savefig('dataframe_scatter.png', dpi=300)

    print()
    print("Reading data from data.csv (using python csv module)", tag='information', tag_color='g', color='w')

    with open("data/data.csv", 'r') as data_file:
        reader = csv.reader(data_file)
        data_vanilla = list(reader)

    del(data_vanilla[0])
    data_array = np.array(data_vanilla, dtype='i')

    print(tag='data', tag_color='m')
    print(data_array[:5], color='w')

    print("Shape of km:", data_array[:, 0].shape, tag='information', tag_color='g', color='w')
    print("Shape of price:", data_array[:, 1].shape, tag='information', tag_color='g', color='w')
    print("Global shape:", data_array.shape, tag='information', tag_color='g', color='w')

    plt.scatter(x=data_array[:, 0], y=data_array[:, 1], c='b')
    plt.title("Dataset: Mileage vs Price (csv module)")
    plt.xlabel("Mileage (km)")
    plt.ylabel("Price ($)")
    plt.xlim(0, 250000)
    plt.ylim(0, 10000)
    plt.savefig('list_scatter.png', dpi=300)

    return data_frame, data_array


def visualize_linear_scatter(theta: np.ndarray, X: pd.Series, y: pd.Series):
    """ Plot the dataset with the function taken from theta

    Params
    -----
        theta (numpy.ndarray): the linear function: theta[0]x + theta[1]
        X (pandas.Series): the mileage data
        y (pandas.Series): the price data (what we aim to predict)
    """

    plt.axline(xy1=(0, theta[0]), slope=theta[1], color='r')
    plt.scatter(x=X, y=y, color='b')
    plt.title("Dataset with linear function")
    plt.savefig('dataset_linear_function.png', dpi=300)


def main():

    data_frame, data_array = data_extraction()

    X = data_frame["km"]
    y = data_frame["price"]

    result = X == data_array[:, 0]
    if result.all() == True:
        print("X and data_array[:, 0] are equal", tag='information', tag_color='g', color='b')
    else:
        print("X and data_array[:, 0] are not equal", tag='information', tag_color='g', color='r')
    result = y == data_array[:, 1]
    if result.all() == True:
        print("y and data_array[:, 1] are equal", tag='information', tag_color='g', color='b')
    else:
        print("y and data_array[:, 1] are not equal", tag='information', tag_color='g', color='r')

    theta = np.zeros(2)

    visualize_linear_scatter(theta, X, y)


if __name__ == "__main__":
    main()
