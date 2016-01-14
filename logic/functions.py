import json  # import function unused for now, until we have a sample JSON file.
from math import pow, sqrt

class Processing:
    """Contains logic for processing json from wrapper.

    :mean: defines mean price of input prices from mean
    :location: defines average lat and long for input.
    :average: defines average.
    :median: defines median for input data.
    :iqr: defines iqr for input data.
    :standardDeviation: defines standard deviation for inout data.

    Note: JSON imports INCOMPLETE
    """
    processeddata = {}

    def average(self, *args):
        """Simple average calculator"""
        total = sum(args)
        totalinstances = len(args)
        average = total / totalinstances
        return average

    def mean(self, *args):
        """fixes potential issue with calling average in location method"""
        mean = self.average(args)
        Processing.processeddata.update({'meanprice': mean})
        return mean

    def location(self, *args1, *args2):
        """Creates an average location for all houses analysed, in longitude and latitude.

        Uses output from Processing.average() to determine average latitude and longitude.
        """
        averagelat = self.average(args1)
        averagelong = self.average(args2)
        Processing.processeddata.update({'averagelat': averagelat, 'averagelong': averagelong})

    def median(self, *args):
        """Simple median calculator"""
        prices = sorted(args)
        totalInstances = len(args)
        if totalInstances%2 == 0:
            median = (prices[int(totalInstances/2)]+prices[int((totalInstances/2)-1)])/2
        else:
            median = prices[int((totalInstances-1)/2)]
        Processing.processeddata.update({'median':median})
        return prices[int((totalInstances-1)/2)]

    def standardDeviation(self, *args):
        """
        finds the standard deviation using the formula for samples(hence the len(args) -1) which is sqrt((sum((x - mean)^2)/n-1)
        """

        #makes sure that the sample size is graeter than one
        if len(args) <= 1:
            return -1

        mean = self.average(args)
        sum = 0
        for a in args:
            sum += pow((a - mean),2)
        standardDeviation = sum/(len(args)-1)
        standardDeviation = sqrt(standardDeviation)
        return standardDeviation

    def iqr(self, *args):
        """simple iqr calculator"""

        q1=0;q3=0
        prices = sorted(args)
        length = len(prices)
        if length%4 == 0:
            q1 = (prices[int(length/4)]+prices[int(length/4)-1])/2
            q3 = (prices[length-int(length/4)]+prices[length-1-(length/4)])/2
        elif length%2 == 0:
            q1 = prices[int(((length/2)-1)/2)]
            q3 = prices[length-1-int(((length/2)-1)/2)]
        elif (length-1)%4 == 0:
            q1 = (prices[int((length-1)/4)] + prices[int((length-1)/4)-1])/2
            q3 = (prices[length-int((length-1)/4)]+prices[length-int((length-1)/4)-1])/2
        else:
            q1 = prices[int((((length-1)/2)-1)/2)]
            q3 = prices[length-int((((length-1)/2)-1)/2)-1]
        return q3 - q1