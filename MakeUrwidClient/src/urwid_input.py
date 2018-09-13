
# -*- coding: utf-8 -*-
"""
    MakeUrwidClient.urwid_input
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    DESCRIPTION

    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018-09-12 14:09:45
"""

import urwid


message = ""


def show_or_exit(key):
    global message
    message += key
    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()
    txt.set_text(repr(message))


txt = urwid.Text("Hello World")
fill = urwid.Filler(txt, "top")
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
loop.run()
