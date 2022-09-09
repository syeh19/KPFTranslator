import ktl

from ddoitranslatormodule.KPFTranslatorFunction import KPFTranslatorFunction


class InitWfc(KPFTranslatorFunction):
    """
    InitWfc -- Init WFC 
    SYNOPSIS
        InitWfc.execute()
    DESCRIPTION
        init WFS so ACAM can see light

    ARGUMENTS
    OPTIONS
    EXAMPLES
    
    """

    @classmethod
    def pre_condition(args, logger, cfg):
        return True

    @classmethod
    def perform(cls, args, logger, cfg):
        ao = ktl.cache('ao')
        ao['WCINIT'].write('1')

    @classmethod
    def post_condition(cls, args, logger, cfg):
        ao = ktl.cache('ao')
        aowcinit_success = ktl.waitfor('($ao.WCSTAT == normal)', timeout=3)
        if not aowcinit_success:
            print(f'Failed to init WFC')
        return aowcinit_success        