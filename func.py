import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc

def getSubject(sub):
    rc('font', family=font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name())

    df = pd.read_csv("Data/scores.csv")
    df.index = df['name']
    del df['name']
    try:
        score = df['kor'].values
        names = df.index.values
        soc = df.loc[:, sub]
        print(soc)
        plt.bar(range(len(names)), soc)
        plt.xticks(range(len(names)), names, rotation="40")
        fname = 'static/' + sub + '.png'
        print(fname)
        plt.savefig(fname)
        plt.close()
    except KeyError:
        fname = 'no'
    return fname





