from distutils.core import setup
import py2exe

setup(
	windows=["picmerger.pyw",],
	options={"py2exe":{"includes":["sip","PyQt4","elixir"]}})