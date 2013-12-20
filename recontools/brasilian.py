import base
from random import choice


class Brasilian(base.ReconPlugin):
    def __init__(self):
        base.ReconPlugin.__init__(self)
        self.name = 'brasilian'
        self.brasilians = ['Ardriana Lima',
                           'Ayrton Senna',
                           'Gisele Bundchen',
                           'Marcelo Martins',
                           'Alessandra Ambrosio',
                           'Seu George',
                           'Pele',
                           'Jorge Stolfi',
                           ]

    def get_info(self, path):
        if path == self.name:
            brasilian = choice(self.brasilians)
            return {self.name: brasilian}
        else:
            return None
