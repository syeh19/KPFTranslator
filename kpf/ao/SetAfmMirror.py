import ktl

from ddoitranslatormodule.KPFTranslatorFunction import KPFTranslatorFunction


class SetAfmMirror(KPFTranslatorFunction):
    """
    SetAfmMirror -- set AFM to Mirror so ACAM sees light
    SYNOPSIS
        SetAfmMirror.execute()
    DESCRIPTION
        AO rotator needs to be in the Manual mode before observing.

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
        ao['OBAMNAME'].write('Mirror')
        ao['OBAMSLEW'].write('1')

    @classmethod
    def post_condition(cls, args, logger, cfg):
        ao = ktl.cache('ao')
        aoamstst_success = ktl.waitfor('($ao.OBAMSTST == INPOS)' and '($ao.OBAMNAME == Mirror)', timeout=60)
        if not aoamstst_success:
            print(f'Failed to set AFM to Mirror')
        return aoamstst_success   