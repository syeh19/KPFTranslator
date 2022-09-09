import ktl

from ddoitranslatormodule.KPFTranslatorFunction import KPFTranslatorFunction


class AoHatchOpen(KPFTranslatorFunction):
    """
    AoHatchOpen -- open AO hatch
    SYNOPSIS
        AoHatchOpen.execute()
    DESCRIPTION
        open AO hatch for KPF observing

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
        ao['aohatchcmd'].write('open')

    @classmethod
    def post_condition(cls, args, logger, cfg):
        ao = ktl.cache('ao')
        aohatchsts_success = ktl.waitfor('($ao.AOHATCHSTS == open)', timeout=30)
        if not aohatchsts_success:
            print(f'Failed to open AO hatch')
        return aohatchsts_success   
        