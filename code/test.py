import pandas as pd
import numpy as np

if __name__ == '__main__':
    chip = pd.read_csv('../data/fundemental/chip.csv')
    chip = np.array(chip)[:, :4]
    chip = chip[::-1]

    price = pd.read_csv('../data/fundemental/STOCK_DAY_2330_202001.csv', encoding='unicode_escape')
    price = price[1:16]

    print(price)
