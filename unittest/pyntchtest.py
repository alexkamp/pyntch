import unittest, os

import pyntch
from pyntch.typenode import TypeNode, CompoundTypeNode, TypeChecker
from pyntch.frame import ExecutionFrame, ExceptionCatcher
from pyntch.expression import MustBeDefinedNode
from pyntch.namespace import Namespace
from pyntch.module import Interpreter, IndentedStream, ModuleNotFound
from pyntch.config import ErrorConfig

class OldTest(unittest.TestCase):
    
    def setUp(self):
        """This method performs the setup for pyntch. You should call it once before you use pyntch for the first time. """
        TypeNode.debug = False
        TypeNode.verbose = False
        Interpreter.debug = False
        Interpreter.verbose = False
        stubdir = os.path.join(os.path.dirname(pyntch.__file__), 'stub')
        Interpreter.initialize(stubdir)
        TypeChecker.reset()
        MustBeDefinedNode.reset()
        ExceptionCatcher.reset()

    def analyzeFile(self, pyFile):
        (name,_) = os.path.splitext(os.path.basename(pyFile))
        module = Interpreter.load_file(name, pyFile, [])
        TypeNode.run()
        TypeChecker.check()
        MustBeDefinedNode.check()
        ExceptionCatcher.check()
        TypeNode.run()
        return module
    
    def test_all(self):
        for f in os.listdir('test'):
            self.analyzeFile(os.path.join('test', f))
    