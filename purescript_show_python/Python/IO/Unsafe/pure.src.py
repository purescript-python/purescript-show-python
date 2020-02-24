from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "$foreign"
                        , call( var('import_module')
                              , "purescript_show_python.ffi.Python.IO.Unsafe" ) )
           , assign_star("ps_assert", get_item(var("$foreign"), "assert_"))
           , assign( "exports"
                   , record( ("assert", var("ps_assert"))
                           , ("show", get_item(var("$foreign"), "show"))
                           , ("printLn", get_item(var("$foreign"), "printLn"))
                           , ("repr", get_item(var("$foreign"), "repr"))
                           , ( "assertMsg"
                             , get_item(var("$foreign"), "assertMsg") ) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\src\\Python\\IO\\Unsafe.purs", name="purescript_show_python.Python.IO.Unsafe.pure")
