""" Setting break point when the wx event loop is running doesn't cause 
any problems. Under QT it does and throws 
QCoreApplication::exec: The event loop is already running

Use the function below to put a break point 
from qt_break import debug_trace ; debug_trace()
and have the namespace of the location of that function call inside 
ipython. 

In PDB, that namespace is stored in 2 dictionaries l (for locals) and g 
(for globals)
"""

def debug_trace(break_to = "ipy", use_globals = True):
  """ Set a tracepoint in the Python debugger that works with Qt (tested
  on pyqt and pyside 1.0.7)
  """
  from PyQt4.QtCore import pyqtRemoveInputHook
  from IPython import embed
  from pdb import set_trace

  # Get the locals and globals dict from the location where this function
  # was called.
  import sys
  previous_frame = sys._getframe(1)
  l = previous_frame.f_locals
  if use_globals:
      g = previous_frame.f_globals
      namespace = g
  else:
      namespace = {}
  namespace.update(l)
  # Stop the QT check for gui event loop and put the break point
  pyqtRemoveInputHook()
  if break_to == "ipy":
      embed(user_ns=namespace)
  else:
      set_trace()
