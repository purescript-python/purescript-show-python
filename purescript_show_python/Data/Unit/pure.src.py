from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "$foreign"
                        , call( var('import_module')
                              , "purescript_show_python.ffi.Data.Unit" ) )
           , assign_star( "ps_Data_Show"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Show.pure" ) )
           , assign_star( "ps_showUnit"
                        , new( get_item(var("ps_Data_Show"), "Show")
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( metadata( 17
                                                           , 12
                                                           , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Unit.purs"
                                                           , "unit" ) ) ) ) ) )
           , assign( "exports"
                   , record( ("showUnit", var("ps_showUnit"))
                           , ("unit", get_item(var("$foreign"), "unit")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Unit.purs", name="purescript_show_python.Data.Unit.pure")
