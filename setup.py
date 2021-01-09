from distutils.core import setup
import py2exe

setup(console = ['simple_server.py'], options = {'py2exe' : { 
	"bundle_files" : 1, "optimize" : 2, "excludes" : ['_ssl', 'pdb', 'doctest', 'unittest', 'difflib', 'inspect'] }})
