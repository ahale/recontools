import abc


class ReconPlugin(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def get_info(self, path):
        pass
