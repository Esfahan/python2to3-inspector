# -*- coding:utf-8 -*-
'''
# It means 
- `import PRJ_ROOT/base.py` with Python2.x
- `import PRJ_ROOT/libs/base.py` with Python3.x
'''
import base
'''
It should be `configparser` with Python3.x
'''
import ConfigParser


class SampleClass(base.Base):

    def sample_method(self):
        '''
        It should be `print()` with Python3.x
        '''
        print '[division]'
        '''
        # Results
        - `0` with Python 2.x
        - `0.5` with Python 3.x
        '''
        print '1/2 = {}'.format(1/2)
        print '1//2 = {}'.format(1//2)
