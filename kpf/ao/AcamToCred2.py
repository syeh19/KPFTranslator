import ktl

from ddoitranslatormodule.KPFTranslatorFunction import KPFTranslatorFunction


class AcamToCred2(KPFTranslatorFunction):
    """
    AcamToCred2  
        Switch CRED2 to ACAM

    SYNOPSIS
        AcamToCred2.execute({})
    DESCRIPTION
        1. Set AO roator in Manual
        2. Leave AO rotator to 45 deg
        3. Move PCU to KPF <-- to be implemented
        

    ARGUMENTS
    OPTIONS
    EXAMPLES
    
    """

    @classmethod
    def pre_condition(args, logger, cfg):
        return True

    @classmethod
    def perform(cls, args, logger, cfg):
        
        print('Set AO rotator in Manual')
        SetAoRotatorManual.execute({})

        print('Set AO rotator to 45 deg')
        ParkAoRotator.execute({})

        print('Move PCU to KPF')



    @classmethod
    def post_condition(cls, args, logger, cfg):
        return True