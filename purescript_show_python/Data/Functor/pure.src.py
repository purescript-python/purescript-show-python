from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "$foreign"
                        , call( var('import_module')
                              , "purescript_show_python.ffi.Data.Functor" ) )
           , assign_star( "ps_Control_Semigroupoid"
                        , call( var('import_module')
                              , "purescript_show_python.Control.Semigroupoid.pure" ) )
           , assign_star( "ps_Data_Function"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Function.pure" ) )
           , assign_star( "ps_Data_Unit"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Unit.pure" ) )
           , assign_star( "ps_Functor"
                        , define( None
                                , ["ps_map", ".this"]
                                , block( set_item( var(".this")
                                                 , "map"
                                                 , var("ps_map") )
                                       , var(".this") ) ) )
           , assign_star( "ps_map"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "map" ) ) ) ) )
           , assign_star( "ps_mapFlipped"
                        , define( None
                                , ["ps_dictFunctor"]
                                , block( ret( define( None
                                                    , ["ps_fa"]
                                                    , block( ret( define( None
                                                                        , [ "ps_f" ]
                                                                        , block( ret( call( call( call( var( "ps_map" )
                                                                                                      , var( "ps_dictFunctor" ) )
                                                                                                , var( "ps_f" ) )
                                                                                          , var( "ps_fa" ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_void"
                        , define( None
                                , ["ps_dictFunctor"]
                                , block( ret( call( call( var("ps_map")
                                                        , var( "ps_dictFunctor" ) )
                                                  , call( get_item( var( "ps_Data_Function" )
                                                                  , "const" )
                                                        , get_item( var( "ps_Data_Unit" )
                                                                  , "unit" ) ) ) ) ) ) )
           , assign_star( "ps_voidLeft"
                        , define( None
                                , ["ps_dictFunctor"]
                                , block( ret( define( None
                                                    , ["ps_f"]
                                                    , block( ret( define( None
                                                                        , [ "ps_x" ]
                                                                        , block( ret( call( call( call( var( "ps_map" )
                                                                                                      , var( "ps_dictFunctor" ) )
                                                                                                , call( get_item( var( "ps_Data_Function" )
                                                                                                                , "const" )
                                                                                                      , var( "ps_x" ) ) )
                                                                                          , var( "ps_f" ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_voidRight"
                        , define( None
                                , ["ps_dictFunctor"]
                                , block( ret( define( None
                                                    , ["ps_x"]
                                                    , block( ret( call( call( var( "ps_map" )
                                                                            , var( "ps_dictFunctor" ) )
                                                                      , call( get_item( var( "ps_Data_Function" )
                                                                                      , "const" )
                                                                            , var( "ps_x" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_functorFn"
                        , new( var("ps_Functor")
                             , call( get_item( var("ps_Control_Semigroupoid")
                                             , "compose" )
                                   , get_item( var("ps_Control_Semigroupoid")
                                             , "semigroupoidFn" ) ) ) )
           , assign_star( "ps_functorArray"
                        , new( var("ps_Functor")
                             , get_item(var("$foreign"), "arrayMap") ) )
           , assign_star( "ps_flap"
                        , define( None
                                , ["ps_dictFunctor"]
                                , block( ret( define( None
                                                    , ["ps_ff"]
                                                    , block( ret( define( None
                                                                        , [ "ps_x" ]
                                                                        , block( ret( call( call( call( var( "ps_map" )
                                                                                                      , var( "ps_dictFunctor" ) )
                                                                                                , define( None
                                                                                                        , [ "ps_f" ]
                                                                                                        , block( ret( call( var( "ps_f" )
                                                                                                                          , var( "ps_x" ) ) ) ) ) )
                                                                                          , var( "ps_ff" ) ) ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("Functor", var("ps_Functor"))
                           , ("map", var("ps_map"))
                           , ("mapFlipped", var("ps_mapFlipped"))
                           , ("void", var("ps_void"))
                           , ("voidRight", var("ps_voidRight"))
                           , ("voidLeft", var("ps_voidLeft"))
                           , ("flap", var("ps_flap"))
                           , ("functorFn", var("ps_functorFn"))
                           , ("functorArray", var("ps_functorArray")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Functor.purs", name="purescript_show_python.Data.Functor.pure")
