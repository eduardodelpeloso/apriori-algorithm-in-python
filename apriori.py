#!/bin/python3

import math
import os
import random
import re
import sys
import pandas as pd
from pandas.core.common import flatten as pdflat
from itertools import product


#@profile
def attributesSet(numberOfAttributes, supportThreshold):

    # Load data into a Pandas DataFrame, without a header row.
    data = pd.read_csv("census.csv", header=None)

    # Rename columns using the data attributes
    attributes = list(map(lambda x: x.split("=")[0], data.iloc[0]))
    data.columns = attributes

    # Remove the attributes from the data, keeping only the values
    # Example: If data was originally capital-gain=None, now we
    # have a None value in the capital-gain column.
    for attribute in attributes:
        data[attribute] = data[attribute].map(lambda x: x.lstrip(attribute + "="))

    values = list(map(lambda x: data[x].unique(), attributes))

    data2 = data.to_numpy()

    finalResults = []

    listaParesBad = []
    badValuesTuple = ()

    for attribNum in range(numberOfAttributes):

        if (attribNum == 0):
            combs = [i for i in range(12)]  # list([range(12)])
        else:
            combs = product(leftPart, rightPart)
            combs = [sorted(pdflat(item)) for item in combs]
            tempCombs = []
            for i in combs:
                if i not in tempCombs and list(sorted(set(i))) == i:
                    tempCombs.append(i)
            combs = tempCombs

        leftPart = []
        if attribNum == 0:
            rightPart = []

        badAttribList = []
        for comb in combs:
            badAttribList.append(True)
            if attribNum == 0:
                prods = values[comb]
            else:
                prods = values[comb[0]]
                for i in range(1, attribNum + 1):
                    prods = list(product(values[comb[i]], list(prods)))
            for prod in prods:
                prod = list(pdflat(prod))
                if attribNum == 0:
                    prod = "".join(prod)
                else:
                    prod.reverse()

                badValue = False
                #testParam = (data[attributes[comb if attribNum == 0 else comb[0]]] == (prod if attribNum == 0 else prod[0]))
                testParam = (data[attributes[comb if attribNum == 0 else comb[0]]].values == (prod if attribNum == 0 else prod[0]))
                
                for i in range(1, attribNum + 1):
                    if prod[i] in badValuesTuple:
                        badValue = True
                        break
                    #testParam = testParam & (data[attributes[comb if attribNum == 0 else comb[i]]] == (prod if attribNum == 0 else prod[i]))
                    testParam = testParam & (data[attributes[comb if attribNum == 0 else comb[i]]].values == (prod if attribNum == 0 else prod[i]))
    
                if badValue == True:
                    continue

                support = testParam.sum() / 30162
                if support >= supportThreshold:
                    if attribNum == numberOfAttributes - 1:
                        strResult = ""
                        for i in range(numberOfAttributes):
                            if attribNum == 0:
                                testVar = prod
                                strResult += cnames[comb] + "=" + testVar + ","
                            else:
                                testVar = prod[i]
                                strResult += attributes[comb[i]] + "=" + testVar + ","
                        finalResults.append(strResult[:-1])
                elif attribNum == 0:
                    badValuesTuple += (prod,)

                badAttribList[-1] = badAttribList[-1] and support < supportThreshold

        for i in range(len(badAttribList)):
            if badAttribList[i] == False:
                leftPart.append(combs[i])

        if (attribNum == 0):
            rightPart = leftPart

    return finalResults


if __name__ == '__main__':
    result = attributesSet(4, 0.6)

    print('\n'.join(result))
    print('\n')
