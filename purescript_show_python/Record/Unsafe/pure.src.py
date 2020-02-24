from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( " | The functions in this module are highly unsafe as they treat records like | stringly-keyed maps and can coerce the row of labels that a record has. | | These function are intended for situations where there is some other way of | proving things about the structure of the record - for example, when using | `RowToList`. **They should never be used for general record manipulation.**"
           , assign_star( "$foreign"
                        , call( var('import_module')
                              , "purescript_show_python.ffi.Record.Unsafe" ) )
           , assign( "exports"
                   , record( ( "unsafeHas"
                             , get_item(var("$foreign"), "unsafeHas") )
                           , ( "unsafeGet"
                             , get_item(var("$foreign"), "unsafeGet") )
                           , ( "unsafeSet"
                             , get_item(var("$foreign"), "unsafeSet") )
                           , ( "unsafeDelete"
                             , get_item(var("$foreign"), "unsafeDelete") ) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Record\\Unsafe.purs", name="purescript_show_python.Record.Unsafe.pure")
