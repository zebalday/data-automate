import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn as skl

from pandas import (
    DataFrame,
)

from sklearn.preprocessing import (
    MinMaxScaler,
)


""" 
This is a collection of popular data science methods used in the data
visualization stage.
"""


# --------------------------------------------------------------------

def getDataframeLayout(
        df : DataFrame,
        cols : int = 3
    ) -> tuple:
   
    """
    Support Method
    --------------
    Returns dataframe layout for plot visualization. Takes an initial
    column value of 3.

    Parameters
    ----------
    df : pandas.DataFrame object.
    cols : int.
        Number of desired columns for the layout. Default value = 3.

    Returns
    -------
    Tuple (rows, cols).
    """
    rows = round((len(df.columns) / cols), 0) + 1
    layout = (int(rows), cols)

    return layout


# --------------------------------------------------------------------

def getScaledDataframe(
        df : DataFrame,
    ) -> DataFrame:

    """
    Support Method
    --------------
    Returns provided dataframe with scaled values between range (0, 1).

    Parameters
    ----------
    df : pandas.DataFrame object.

    Returns
    -------
    pandas.DataFrame object.
    """

    scaler = MinMaxScaler(feature_range = (0,1))
    scaled_data = scaler.fit_transform(df)
    scaled_df = DataFrame(scaled_data, df.columns.to_list())

    return scaled_df


# --------------------------------------------------------------------

def pltScaledData(
        df : DataFrame,
    ) -> None:

    """ 
    Visualization Method
    --------------------
    Displays histrogram plots of provided dataframe columns with scaled
    data. Used library: Matplotlib.

    Parameters
    ----------
    df : pandas.DataFrame object.
    """

    scaled_df = getScaledDataframe(df)

    figure = plt.figure(figsize = (14, 14))
    ax = figure.gca()
    df_layout = getDataframeLayout(scaled_df)

    scaled_df.plot(
        ax = ax,
        kind = 'hist',
        subplots = True,
        layout = df_layout,
        sharex = True
    )

    plt.show()


# --------------------------------------------------------------------

def snsScaledData(
        df : DataFrame,
    ) -> None:
   
    """ 
    Visualization Method
    --------------------
    Displays histrogram plots of provided dataframe columns with scaled
    data. Used library: Seaborn.

    Parameters
    ----------
    df : pandas.DataFrame object.
    """

    scaled_df = getScaledDataframe(df)

    df_len = len(scaled_df.columns)  
    df_layout = getDataframeLayout(scaled_df)

    f, ax =plt.subplots(df_layout[0], df_layout[1], figsize = (12,12))

    count = 0

    for row in range(df_layout[0]):
        for col in range(df_layout[1]):
            data = scaled_df[scaled_df.columns[count]]
            sns.histplot(data, ax = ax[row, col], kde = True, stat = "density").set(ylabel="")
            
            if count == (df_len - 1):
                break
            count += 1


# --------------------------------------------------------------------


# --------------------------------------------------------------------