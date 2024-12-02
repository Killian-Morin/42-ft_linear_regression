import matplotlib.pyplot as plt
import pandas as pd
from print_color import print


def main():
    """ Predict the price for a car with a mileage passed as input

    * Prompt the user to put a price to estimate
    * Try to convert it to an int(), handle the possible exceptions
    * Read the theta.txt file for the theta values
    * Catch the possible exceptions (file not created, i.e. training not run) to set the theta at 0
    * Compute an estimated price with the theta values and the mileage
        * estimatePrice(mileage) = \theta_0 + (\theta_1 ∗ mileage)
    * Print the result and create a plot with the dataset, the theta function and the estimation
    """
    mileage = input("Mileage to get an estimated price for: ")

    try:
        mileage = int(mileage)
        print(f"Will estimate the price of a car that has a mileage of {mileage} km\n", tag='information', tag_color='g', color='b')
    except Exception as e:
        print(e, color='r')
        return

    print("Get the theta from theta.txt ...\n", tag='information', tag_color='g', color='w')

    try:
        with open("theta.txt", "r") as theta_file:
            print("theta.txt exist, the values of the theta are:", tag='information', tag_color='g', color='cyan')
            theta0 = float(theta_file.readline()[:-1])
            theta1 = float(theta_file.readline())
    except Exception as e:
        print("theta.txt does not exist, both theta are set to 0", tag='information', tag_color='g', color='cyan')
        theta0 = 0
        theta1 = 0

    print(f"theta0 == {theta0}", tag='information', tag_color='g', color='y')
    print(f"theta1 == {theta1}\n", tag='information', tag_color='g', color='y')

    estimated_price = theta0 + (theta1 * mileage)

    print(f"The estimated price of a car with a mileage of {mileage} is {estimated_price:.4f}", tag='result', tag_color='p', color='b')

    dataset = pd.read_csv("data/data.csv")
    dataset.plot.scatter(x="km", y="price", c="b", label="Dataset")
    plt.scatter(x=mileage, y=estimated_price, c="r", label="Estimation")
    plt.axline(xy1=(0, theta0), slope=theta1, color="g", label="Linear Regression function")
    plt.title(f"Dataset with the estimated price from the mileage {mileage} with function {theta0} + {theta1}x")
    plt.xlabel("Mileage (km)")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.grid()
    plt.savefig(f"estimation_{mileage}.png", dpi=300, bbox_inches='tight')


if __name__ == "__main__":
    main()
