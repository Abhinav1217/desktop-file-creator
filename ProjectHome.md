# Desktop File Creator #

I find creating appropriate .desktop files for the linux desktop a bit tricky to do by hand: cinnamon doesn't show them at all in the menu bar if there's any typos, and there didn't seem to be an appropriate tool to create them automatically that include file selection boxes and similar to help with creation.

This short programme creates proforma entry boxes for all of the valid keys, saving having to remember them all.  Shows file / directory chooser for the keys that are appropriate, saving typing errors.

Written in python / Tk.

Uses the following as a source for the legal values:

http://standards.freedesktop.org/desktop-entry-spec/latest/