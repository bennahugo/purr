# -*- coding: utf-8 -*-
Version = "1.1.beta";

import os.path

# init debug printing
import Kittens.utils
verbosity = Kittens.utils.verbosity(name="purr");
dprint = verbosity.dprint;
dprintf = verbosity.dprintf;

import Kittens.pixmaps 
pixmaps = Kittens.pixmaps.PixmapCache("purr");

import Kittens.config
ConfigFile = Kittens.config.DualConfigParser("purr.conf");
Config = Kittens.config.SectionParser(ConfigFile,"Purr");

from LogEntry import DataProduct,LogEntry
from Purrer import Purrer
import Parsers

# if GUI is enabled, this will be overwritten by an object that
# sets a busy cursor on instantiation, and restores the cursor when killed
class BusyIndicator (object):
  pass;


def canonizePath (path):
  """Returns the absolute, normalized, real path  of something.
  This takes care of symbolic links, redundant separators, etc.""";
  return os.path.abspath(os.path.normpath(os.path.realpath(path)));


def progressMessage (msg,sub=False):
  """shows a progress message. If a GUI is available, this will be redefined by the GUI.
  If sub is true, message is a sub-message of previous one.""";
  pass;