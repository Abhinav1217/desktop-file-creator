# Introduction #

I can't remember all of the .desktop file keys, and it usually takes me ages of frustration of finding typing mistakes before my shortcuts actually work, so have written a little app to help me along with that.


The first thing I did with this program was make it self hosting:

  * get Tk if it's not already installed
    * sudo apt-get install python-tk
  * start the script from the command line:
    * git clone https://code.google.com/p/desktop-file-creator/
    * cd desktop-file-creator
    * chmod +x desktop-file-creator.py
    * ./desktop-file-creator.py
  * Beside "Name", enter "Desktop File Creator"
  * Beside "Exec", enter "python" in the left-hand box.  Click the middle button, and choose "desktop-file-creator.py"
  * Choose "Utility" from "Categories"
  * Press "Generate".  The default path to save is in your .local/share/applications/ folder, which will cause this entry to appear in your menu bar.  Press "Save"
  * Now you can run the script by choosing "Accessories->Desktop File Creator" from the menu bar.

Repeat for all of the other apps that you want shortcuts for.
# Details #

Most of the fields should be fairly self-explanatory; they're exactly the same as the freedesktop.org specification.  The Exec box has entry fields before and after: creating a shortcut for Steam on wine, for instance, requires "wine", "path/to/steam", and "-no-dwrite" on my machine.