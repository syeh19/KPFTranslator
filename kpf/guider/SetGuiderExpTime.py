from pathlib import Path

import ktl

from ddoitranslatormodule.KPFTranslatorFunction import KPFTranslatorFunction


class SetGuiderExpTime(KPFTranslatorFunction):
    '''Set the guider exposure time (in seconds) via the kpfguide.EXPTIME
    keyword.
    
    The guider exposure time is governed by several factors.  The exposure time
    controlled here is generated by stacking (averaging) multiple frames as
    needed to obtain the specified exposure time.  Those individual frames are
    controlled by the FPS, AVERAGE, STACK, and EXPTIME keywords.


    From Kyle:

    If you want to tweak an exposure setting, I recommend MAGIQ use the
    EXPTIME keyword as its preferred knob. This will translate to changing
    the number of frames averaged together. You can also choose to stack
    frames, but I doubt that will be necessary.

    Notice how EXPTIME remains unchanged when I change the STACK keyword:

    [klanclos@kpffiuserver ~]$ gshow -s kpfguide fps average stack exptime
             FPS =  100.0000 frames/second
         AVERAGE =  100 frames
           STACK =  1 averaged frames
         EXPTIME =  1.000000 seconds

    [klanclos@kpffiuserver ~]$ modify -s kpfguide stack=2
    setting stack = 2 (wait)
    [klanclos@kpffiuserver ~]$ gshow -s kpfguide fps average stack exptime
             FPS =  100.0000 frames/second
         AVERAGE =  50 frames
           STACK =  2 averaged frames
         EXPTIME =  1.000000 seconds

    ...but if I change AVERAGE, EXPTIME reflects the change:

    [klanclos@kpffiuserver ~]$ modify -s kpfguide average=20
    setting average = 20 (wait)
    [klanclos@kpffiuserver ~]$ gshow -s kpfguide fps average stack exptime
             FPS =  100.0000 frames/second
         AVERAGE =  20 frames
           STACK =  1 averaged frames
         EXPTIME =  0.200000 seconds

    Stick to changing EXPTIME and you won't have to worry about it.
    Changing the frames per second is not recommended, because the tip/tilt
    system will be consuming this image stream, and it needs to retain full
    control of what an individual frame looks like.
    '''
    @classmethod
    def pre_condition(cls, args, logger, cfg):
        return True

    @classmethod
    def perform(cls, args, logger, cfg):
        exptimekw = ktl.cache('kpfguide', 'EXPTIME')
        exptime = args.get('exptime', None)
        if exptime is not None:
            exptimekw.write(exptime)

    @classmethod
    def post_condition(cls, args, logger, cfg):
        exptimekw = ktl.cache('kpfguide', 'EXPTIME')
        exptime = args.get('exptime', None)

        exptol = 0.01
        timeshim = 0.25
        if exptime is not None:
            exptime_check = exptimekw.read(binary=True)
            # First try sleeping briefly
            if abs(exptime_check - exptime) > exptol:
                sleep(timeshim)
            # Now check again
            exptime_check = exptimekw.read(binary=True)
            if abs(exptime_check - exptime) > exptol:
                print(f"Failed to set exposure time.")
                print(f"Requested {exptime:.3f} s, found {exptime_check:.3f} s")
                return False

        return True
