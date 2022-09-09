import ktl
from ddoitranslatormodule.KPFTranslatorFunction import KPFTranslatorFunction


class AoHatchClose(KPFTranslatorFunction):
    """
    AoHatchClose -- Close AO hatch
    SYNOPSIS
        AoHatchClose.execute()
    DESCRIPTION
        Close AO hatch after KPF observing

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
        ao['aohatchcmd'].write('close')

    @classmethod
    def post_condition(cls, args, logger, cfg):
        ao = ktl.cache('ao')
        aohatchsts_success = ktl.waitfor('($ao.AOHATCHSTS == closed)', timeout=30)
        if not aohatchsts_success:
            print(f'Failed to close AO hatch')
        return aohatchsts_success   