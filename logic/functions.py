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
        sumprice = sum(args)
        totalinstances = len(args)
        average = sumprice / totalinstances
        Processing.processeddata.update({'meanprice': average})
        return average

    def location(self, *args1, *args2):
        """Creates an average location for all houses analysed, in longitude and latitude.

        Uses output from Processing.average() to determine average latitude and longitude.
        """
        averagelat = self.average(args1)
        averagelong = self.average(args2)
        Processing.processeddata.update({'averagelat': averagelat, 'averagelong': averagelong})
