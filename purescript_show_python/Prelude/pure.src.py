from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block("No document", assign("exports", record()))
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Prelude.purs", name="purescript_show_python.Prelude.pure")
