import ktl

from ddoitranslatormodule.KPFTranslatorFunction import KPFTranslatorFunction

from . import AoHatchClose, AoHatchOpen

class AoHatchOpen(KPFTranslatorFunction):
    """
    AoHatchOpen -- turn off the HEPA filter in AO before observing
    SYNOPSIS
        AoHatchOpen.execute()
    DESCRIPTION
        Check if the HEPA filter inside the AO enclosure is turned off
        before observing. If not, turn it off.
        set ao.OBHPAON=0

    ARGUMENTS
    OPTIONS
    EXAMPLES
    
    """
    @classmethod
    def add_cmdline_args(cls, parser, cfg=None):
        """
        The arguments to add to the command line interface.
        """
        args_to_add = OrderedDict()
        args_to_add['destination'] = {'type': str,
                                'help': 'Desired hatch position: "open" or "closed"'}

        parser = cls._add_args(parser, args_to_add, print_only=False)
        return super().add_cmdline_args(parser, cfg)

    @classmethod
    def pre_condition(args, logger, cfg):
        destination = args.get('destination', '').strip()
        return destination.lower() in ['close', 'closed', 'open']

    @classmethod
    def perform(cls, args, logger, cfg):
        destination = args.get('destination', '').strip()
        if destination.lower() in ['close', 'closed']:
            AoHatchClose.AoHatchClose.execute({})
        elif destination.lower() in ['open']:
            AoHatchOpen.AoHatchOpen.execute({})

    @classmethod
    def post_condition(cls, args, logger, cfg):
        destination = args.get('destination', '').strip()
        ao = ktl.cache('ao')
        return ktl.waitfor(f'($ao.AOHATCHSTS == {destination})', timeout=30)
