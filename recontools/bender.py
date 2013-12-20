import base


class Bender(base.ReconPlugin):
    def __init__(self):
        base.ReconPlugin.__init__(self)
        self.name = 'bender'

    def get_info(self, path):
        benderism = "I would have won, except we ran out of olives."
        if path == self.name:
            return {self.name: benderism}
        else:
            return None
