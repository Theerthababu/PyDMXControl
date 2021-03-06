"""
 *  PyDMXControl: A Python 3 module to control DMX via Python. Featuring fixture profiles and working with uDMX.
 *  <https://github.com/MattIPv4/PyDMXControl/>
 *  Copyright (C) 2018 Matt Cowley (MattIPv4) (me@mattcowley.co.uk)
"""

from ..defaults import Fixture


class Custom(Fixture):

    def __init__(self, *args, **kwargs):
        chans = args[0]
        args = args[1:]
        super().__init__(*args, **kwargs)

        for _ in range(chans):
            self._register_channel(str(_ + 1))
