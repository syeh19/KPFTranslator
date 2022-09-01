from pathlib import Path

import ktl

from ddoitranslatormodule.KPFTranslatorFunction import KPFTranslatorFunction

from .. import check_guider_is_active, check_guider_is_saving

class StopGuiderContinuous(KPFTranslatorFunction):
    '''Stop the guider's continuous exposure mode and stop saving images.
    '''
    @classmethod
    def pre_condition(cls, args, logger, cfg):
        return True

    @classmethod
    def perform(cls, args, logger, cfg):
        kpfguide = ktl.cache('kpfguide')
        kpfguide['CONTINUOUS'].write('inactive')
        kpfguide['SAVE'].write('inactive')

    @classmethod
    def post_condition(cls, args, logger, cfg):
        return check_guider_is_active() and check_guider_is_saving()