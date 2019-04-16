# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod

class Base(object):
    '''
    The way of using Abstract differs between Python 2.x and 3.x
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def sample_method(self):
        raise NotImplementedError()
