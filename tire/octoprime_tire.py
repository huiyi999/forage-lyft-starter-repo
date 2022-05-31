"""
Created on 2022-05-30
@author: chy
"""
from tire.tire import Tire


class OctoprimeTire(Tire):
    '''A Octoprime Tire'''

    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        '''
        Octoprime tires should be serviced only when the sum of all values
        in the tire wear array is greater than or equal to 3.
        '''

        return sum(self.tire_wear) >= 3
