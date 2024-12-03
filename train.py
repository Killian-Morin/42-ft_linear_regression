import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from print_color import print


plt.rcParams["axes.grid"] = True # enable grid by default


def data_extraction() -> pd.DataFrame:
    """ Extract data from data.csv using pandas.read_csv()

    * Use pandas.read_csv() to take the data from the file 'data.csv'
    * Print the head (five first entries) and the shape of the data
    * Plot the data in a scatter plot

    * data_array[:, x] -> the ':' takes all elements (rows) of the first dimension
        and only the elements at index 0, then 1 in each row

    Return
    -----
        data_pandas (pandas.DataFrame): the data extracted using pandas
    """

    print("====================================", color='yellow')
    print("===========DATA EXTRACTION==========", color='yellow')
    print("====================================", color='yellow')

    print("Reading data from data.csv", tag='information', tag_color='g', color='w')

    data_frame = pd.read_csv("data/data.csv")
    print(tag='data', tag_color='m', color='w')
    print(data_frame[:5])

    print("Shape of km:", data_frame["km"].shape, tag='data', tag_color='m', color='w')
    print("Shape of price:", data_frame["price"].shape, tag='data', tag_color='m', color='w')
    print("Global shape:", data_frame.shape, tag='data', tag_color='m', color='w')

    data_frame.plot.scatter(x="km", y="price", c='b')
    plt.title("Dataset: Mileage vs Price")
    plt.xlabel("Mileage (km)")
    plt.ylabel("Price ($)")
    plt.xlim(0, 250000)
    plt.ylim(0, 10000)
    plt.savefig('dataset_scatter.png', dpi=300)

    return data_frame


def visualize_linear_scatter(theta: np.ndarray, X: pd.Series, y: pd.Series):
    """ Plot the dataset with the function taken from theta

    Params
    -----
        theta (numpy.ndarray): the linear function: theta[0]x + theta[1]
        X (pandas.Series): the mileage data
        y (pandas.Series): the price data (what we aim to predict)
    """

    plt.plot(X, y, "ob")
    plt.axline(xy1=(0, theta[0]), slope=theta[1], color='r')
    plt.title(f"Dataset with linear function at {theta[0]:.2f} + {theta[1]:.2f}")
    plt.savefig(f'dataset_linear_function_{theta[0]:.2f}_{theta[1]:.2f}.png', dpi=300)


def predict(X, theta):
    predictions = []
    for i in range(len(X)):
        pred = X[i] * theta[1] + theta[0]
        predictions.append(pred)
    return predictions


def fit(X, y, theta, learning_rate, num_iters):
    # Loop over the number of iterations
    # Initialize some useful variables
    m = X.shape[0]

    theta = theta.copy()

    # Loop over the number of iterations
    for _ in range(num_iters):
        predictions = predict(X, theta)
        errors = predictions - y

        theta[0] = theta[0] - (learning_rate / m) * np.sum(errors)
        theta[1] = theta[1] - (learning_rate / m) * np.sum(errors * X)
    return theta


def main():

    data_frame = data_extraction()

    X = data_frame["km"]
    y = data_frame["price"]

    theta = np.random.randn(2)
    # # theta = np.zeros(2)
    # print(theta)

    # visualize_linear_scatter(theta, X, y)

    # theta = fit(X, y, theta, 0.01, 100)
    # print(theta)

    # visualize_linear_scatter(theta, X, y)


    # print("Save the theta to theta.txt", tag='information', tag_color='g', color='y')

    # with open("theta.txt", "w") as theta_file:
    #     theta_file.write(str(theta[0]) + "\n")
    #     theta_file.write(str(theta[1]))


if __name__ == "__main__":
    main()
