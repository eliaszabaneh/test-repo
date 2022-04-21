import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # read csv
    df = pd.read_csv('spam.csv')
    print(df.head(10))
    print(df.describe(include='all'))
    print(df.info())
    print("Columns {}".format(df.columns[2]))
    print(df.shape)
    print(df.dtypes)
    print(df.index)
    # print(df.values)
    print(df.iloc[0])
    print(df.loc[0])

    # pi plot From frequency
    ax = df.plot.hist(column=["msgDate"])

    plt.show()


def othermain():
    teststr = "18045d189d4b9229, admin.qfr9aqrobf@twecu2jzkn.us, Mon, 20 Apr 2022 03:13:18 -0400"
    a = len(teststr.split(","))
    print(str(a))


if __name__ == "__main__":
    main()
