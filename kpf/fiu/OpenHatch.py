

import ktl
from ddoitranslatormodule.BaseFunction import TranslatorModuleFunction
from ddoitranslatormodule.DDOIExceptions import *

from ..utils import *


class OpenHatch(TranslatorModuleFunction):
    '''Open the FIU hatch
    '''
    def __init__(self):
        super().__init__()

    @classmethod
    def pre_condition(cls, args, logger, cfg):
        return True

    @classmethod
    def perform(cls, args, logger, cfg):
        kpffiu = ktl.cache('kpffiu')
        kpffiu['HATCH'].write('Open')

    @classmethod
    def post_condition(cls, args, logger, cfg):
        return check_fiu_hatch_is_open()
