
# -*- coding: utf-8 -*-
"""
    MakeUrwidClient.urwid_text
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    DESCRIPTION

    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018-09-12 14:05:58
"""

import urwid

txt = urwid.Text("Hello World")
fill = urwid.Filler(txt, "top")
loop = urwid.MainLoop(fill)
loop.run()
