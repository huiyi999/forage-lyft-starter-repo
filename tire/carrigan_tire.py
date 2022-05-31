"""
Created on 2022-05-30
@author: chy
"""
from tire.tire import Tire


class CarriganTire(Tire):
    '''A Carrigan tire'''

    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        '''
        Carrigan tires should be serviced only when one or more of the values
        in the tire wear array is greater than or equal to 0.9.
        '''
        return any([value >= 0.9 for value in self.tire_wear])
