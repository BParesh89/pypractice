class X1:
    def __init__(self, name, price, color='black', variant='diesel'):
        self.name = name
        self.price = price
        self.color = color
        self.variant = variant

    def module_features(self):
        print("Name :{}".format(self.name))
        print("Price :{}".format(self.price))
        print("Color :{}".format(self.color))
        print("Variant :{}".format(self.variant))