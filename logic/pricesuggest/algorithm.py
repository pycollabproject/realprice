class pricesuggest:
    """

    ok so over here im just going to suggest the variables and try to classify them

    Primary variable(variabels which affect each other):
        -square feet
        -amount of rooms
        -amount of bathrooms


    Secondary Variables(variables whose effect is constent):
        -Pool
        -Location
        -age(not sure about this one)


    Now how I think that the rest of the algorithm should be like is as follows:

    price = primaryPrice()+secondaryPrice()

    primaryPrice would be a function that takes into account all of the primary variables and tries to combine them into a price
    this will be the harder part to implement

    secondaryPrice will be alot easier to implement it will be something like this

    float secondaryPrice():
        secondaryprice = 0;
        if(pool):
            secondaryprice += poolaverage]

        ...
        return secondary price
    """

    def primaryPrice(self):
        pass

    def secondaryPrice(self):
        pass

    def estimatePrice(self):
        return self.primaryPrice() + self.secondaryPrice()