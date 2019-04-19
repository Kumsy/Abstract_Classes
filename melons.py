"""Classes for melon orders."""


# class DomesticMelonOrder():
#     """A melon order within the USA."""

#     def __init__(self, species, qty):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.shipped = False
#         self.order_type = "domestic"
#         self.tax = 0.08

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True


# class InternationalMelonOrder():
#     """An international (non-US) melon order."""

#     def __init__(self, species, qty, country_code):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.country_code = country_code
#         self.shipped = False
#         self.order_type = "international"
#         self.tax = 0.17

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True

#     def get_country_code(self):
#         """Return the country code."""

#         return self.country_code


class AbstractMelonOrder():


    def __init__(self, species, qty, country_code = None ):

        self.species = species
        if self.species == 'christmas':
            self.base_price = 5 * 1.5
        else:
            self.base_price = 5    
        self.qty = qty 
        self.shipped = False

        if country_code:
            self.country_code = country_code


    def get_total(self):
        """Calculate price, including tax."""



        total = (1 + self.tax) * self.qty * self.base_price

        if self.country_code != "US" and self.qty < 10:
            total += 3

        return total    


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
        

class DomesticMelonOrder(AbstractMelonOrder):

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    
    order_type = "international"
    tax = 0.17

