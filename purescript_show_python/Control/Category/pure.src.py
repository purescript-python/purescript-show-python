from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_Control_Semigroupoid"
                        , call( var('import_module')
                              , "purescript_show_python.Control.Semigroupoid.pure" ) )
           , assign_star( "ps_Category"
                        , define( None
                                , ["ps_Semigroupoid0", "ps_identity", ".this"]
                                , block( set_item( var(".this")
                                                 , "Semigroupoid0"
                                                 , var("ps_Semigroupoid0") )
                                       , set_item( var(".this")
                                                 , "identity"
                                                 , var("ps_identity") )
                                       , var(".this") ) ) )
           , assign_star( "ps_identity"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "identity" ) ) ) ) )
           , assign_star( "ps_categoryFn"
                        , new( var("ps_Category")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Control_Semigroupoid" )
                                                           , "semigroupoidFn" ) ) ) )
                             , define( None
                                     , ["ps_x"]
                                     , block(ret(var("ps_x"))) ) ) )
           , assign( "exports"
                   , record( ("Category", var("ps_Category"))
                           , ("identity", var("ps_identity"))
                           , ("categoryFn", var("ps_categoryFn")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Control\\Category.purs", name="purescript_show_python.Control.Category.pure")
