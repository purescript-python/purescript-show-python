from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "$foreign"
                        , call( var('import_module')
                              , "purescript_show_python.ffi.Data.Symbol" ) )
           , assign_star( "ps_SProxy"
                        , block( define( "ps_SProxy"
                                       , [".this"]
                                       , block(var(".this")) )
                               , set_attr( var("ps_SProxy")
                                         , "value"
                                         , new(var("ps_SProxy")) )
                               , var("ps_SProxy") ) )
           , assign_star( "ps_IsSymbol"
                        , define( None
                                , ["ps_reflectSymbol", ".this"]
                                , block( set_item( var(".this")
                                                 , "reflectSymbol"
                                                 , var("ps_reflectSymbol") )
                                       , var(".this") ) ) )
           , assign_star( "ps_reifySymbol"
                        , define( None
                                , ["ps_s"]
                                , block( ret( define( None
                                                    , ["ps_f"]
                                                    , block( ret( call( call( call( get_item( var( "$foreign" )
                                                                                            , "unsafeCoerce" )
                                                                                  , define( None
                                                                                          , [ "ps_dictIsSymbol" ]
                                                                                          , block( ret( call( var( "ps_f" )
                                                                                                            , var( "ps_dictIsSymbol" ) ) ) ) ) )
                                                                            , metadata( 20
                                                                                      , 28
                                                                                      , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Symbol.purs"
                                                                                      , record( ( "reflectSymbol"
                                                                                                , define( None
                                                                                                        , [ "ps_v" ]
                                                                                                        , block( ret( var( "ps_s" ) ) ) ) ) ) ) )
                                                                      , get_attr( var( "ps_SProxy" )
                                                                                , "value" ) ) ) ) ) ) ) ) )
           , assign_star( "ps_reflectSymbol"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "reflectSymbol" ) ) ) ) )
           , assign( "exports"
                   , record( ("IsSymbol", var("ps_IsSymbol"))
                           , ("reflectSymbol", var("ps_reflectSymbol"))
                           , ("reifySymbol", var("ps_reifySymbol"))
                           , ("SProxy", var("ps_SProxy")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Symbol.purs", name="purescript_show_python.Data.Symbol.pure")
