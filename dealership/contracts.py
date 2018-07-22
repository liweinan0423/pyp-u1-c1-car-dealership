class Contract(object):
    def total_value(self):
        return self.before_discount() - self.before_discount() * self.customer.DISCOUNT_RATE

    def monthly_value(self):
        return self.total_value() / self.months()

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments

    def before_discount(self):
        return self.vehicle.sale_price() + self.vehicle.INTEREST_RATE * self.monthly_payments * self.vehicle.sale_price() / 100
    def months(self):
        return self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
    def before_discount(self):
        return self.vehicle.sale_price() + self.vehicle.sale_price() * self.vehicle.LEASE_MULTIPLIER / self.length_in_months
    def months(self):
        return self.length_in_months
