from __future__ import print_function

"""

.. moduleauthor:: exploreropen developers and Stephen Raymond Ferg
.. default-domain:: py
.. highlight:: python

Version |release|
"""

import os

try:
    from . import utils as ut
    from . import fileboxsetup as fbs
except (SystemError, ValueError, ImportError):
    import utils as ut
    import fileboxsetup as fbs

tk = ut.tk


# -------------------------------------------------------------------
# fileopenbox
# -------------------------------------------------------------------


def fileopenbox(msg=None, title=None, default='*', filetypes='*.html', multiple=False):

    if filetypes is None:
        filetypes = ["*.htm", "*.html", "HTML for Django"]
    localRoot = tk.Tk()
    localRoot.wm_attributes("-topmost", 1)
    localRoot.withdraw()

    initialbase, initialfile, initialdir, filetypes = fbs.fileboxSetup(
        default, filetypes)

    # ------------------------------------------------------------
    # if initialfile contains no wildcards; we don't want an
    # initial file. It won't be used anyway.
    # Also: if initialbase is simply "*", we don't want an
    # initialfile; it is not doing any useful work.
    # ------------------------------------------------------------
    if (initialfile.find("*") < 0) and (initialfile.find("?") < 0):
        initialfile = None
    elif initialbase == "*":
        initialfile = None

    func = ut.tk_FileDialog.askopenfilenames if multiple else ut.tk_FileDialog.askopenfilename
    ret_val = func(parent=localRoot,
                   title=ut.getFileDialogTitle(msg, title),
                   initialdir=initialdir, initialfile=initialfile,
                   filetypes=filetypes
                   )
    if not ret_val or ret_val == '':
        return None
    if multiple:
        f = [os.path.normpath(x) for x in localRoot.tk.splitlist(ret_val)]
    else:
        try:
            f = os.path.normpath(ret_val)
        except AttributeError as e:
            print("ret_val is {}".format(ret_val))
            raise e
    localRoot.destroy()

    if not f:
        return None
    return f


if __name__ == '__main__':
    print("Hello from file open box")
    ret_val = fileopenbox("Please select a file", "My File Open dialog")
    print("Return value is:{}".format(ret_val))
