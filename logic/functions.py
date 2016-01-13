import json  # import function unused for now, until we have a sample JSON file.

class Processing:
    """Contains logic for processing json from wrapper.

    :meanprice: defines mean price of input prices.
    :location: defines average lat and long for input.
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

    def location(self, *args1, **args2):
        """Creates an average location for all houses analysed, in longitude and latitude.

        Uses output from Processing.average() to determine average latitude and longitude.

        I think there would be an issue the Processing.processeddata.update({'meanprice': mean})
        because it would record this average as the meanprice, so I created a seperate mean function
        that will call the average function
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