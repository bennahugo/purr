#!/usr/bin/python
# -*- coding: utf-8 -*-

# loading file into karma:
#   ksend -add_connection unix 9975 multi_array kvis -load ARRAY:FILE0 img4096.fits
# ls /tmp/.KARMA-connections for port number

# runs Purr standalone
if __name__ == "__main__":
  print "Welcome to PURR!"

  # parse options is the first thing we should do
  from optparse import OptionParser
  usage = "usage: %prog [options] <directories to watch>"
  parser = OptionParser(usage=usage)
  parser.add_option("-d", "--debug",dest="verbose",type="string",action="append",metavar="Context=Level",
                    help="(for debugging Python code) sets verbosity level of the named Python context. May be used multiple times.");
  parser.add_option("-n", "--no-cwd",dest="no_cwd",action="store_true",
                    help="Do not include '.' in directories to watch.");
  (options, rem_args) = parser.parse_args();

  print "Please wait a second while the GUI starts up."

  import sys
  import signal
  import os.path

  from PyQt4.Qt import *

  import Purr
  import Purr.MainWindow
  import Purr.Render


  app = QApplication(sys.argv);
  app.setDesktopSettingsAware(True);

  dirnames = list(rem_args);
  if not options.no_cwd and '.' not in dirnames:
    dirnames.append('.');

  if not os.path.isdir(dirnames[0]):
    print "Argument must be an existing directory name";
    sys.exit(1);

  purrwin = Purr.MainWindow.MainWindow(None);
  if purrwin.attachDirectory(dirnames[0],dirnames):
    # app.setMainWidget(purrwin);
    purrwin.show();
    QObject.connect(app,SIGNAL("lastWindowClosed()"),app,SLOT("quit()"));

    # handle SIGINT
    def sigint_handler (sig,stackframe):
      print "Caught Ctrl+C"
      purrwin.detachDirectory();
      app.quit();
    signal.signal(signal.SIGINT,sigint_handler);


    app.exec_();
    print "PURR exiting, goodbye!";
