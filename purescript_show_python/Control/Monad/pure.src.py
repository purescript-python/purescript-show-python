from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_Control_Applicative"
                        , call( var('import_module')
                              , "purescript_show_python.Control.Applicative.pure" ) )
           , assign_star( "ps_Control_Bind"
                        , call( var('import_module')
                              , "purescript_show_python.Control.Bind.pure" ) )
           , assign_star( "ps_Monad"
                        , define( None
                                , ["ps_Applicative0", "ps_Bind1", ".this"]
                                , block( set_item( var(".this")
                                                 , "Applicative0"
                                                 , var("ps_Applicative0") )
                                       , set_item( var(".this")
                                                 , "Bind1"
                                                 , var("ps_Bind1") )
                                       , var(".this") ) ) )
           , assign_star( "ps_whenM"
                        , define( None
                                , ["ps_dictMonad"]
                                , block( ret( define( None
                                                    , ["ps_mb"]
                                                    , block( ret( define( None
                                                                        , [ "ps_m" ]
                                                                        , block( ret( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                                , "bind" )
                                                                                                      , call( get_item( var( "ps_dictMonad" )
                                                                                                                      , "Bind1" ) ) )
                                                                                                , var( "ps_mb" ) )
                                                                                          , define( None
                                                                                                  , [ "ps_b" ]
                                                                                                  , block( ret( call( call( call( get_item( var( "ps_Control_Applicative" )
                                                                                                                                          , "when" )
                                                                                                                                , call( get_item( var( "ps_dictMonad" )
                                                                                                                                                , "Applicative0" ) ) )
                                                                                                                          , var( "ps_b" ) )
                                                                                                                    , var( "ps_m" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_unlessM"
                        , define( None
                                , ["ps_dictMonad"]
                                , block( ret( define( None
                                                    , ["ps_mb"]
                                                    , block( ret( define( None
                                                                        , [ "ps_m" ]
                                                                        , block( ret( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                                , "bind" )
                                                                                                      , call( get_item( var( "ps_dictMonad" )
                                                                                                                      , "Bind1" ) ) )
                                                                                                , var( "ps_mb" ) )
                                                                                          , define( None
                                                                                                  , [ "ps_b" ]
                                                                                                  , block( ret( call( call( call( get_item( var( "ps_Control_Applicative" )
                                                                                                                                          , "unless" )
                                                                                                                                , call( get_item( var( "ps_dictMonad" )
                                                                                                                                                , "Applicative0" ) ) )
                                                                                                                          , var( "ps_b" ) )
                                                                                                                    , var( "ps_m" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_monadFn"
                        , new( var("ps_Monad")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Control_Applicative" )
                                                           , "applicativeFn" ) ) ) )
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Control_Bind" )
                                                           , "bindFn" ) ) ) ) ) )
           , assign_star( "ps_monadArray"
                        , new( var("ps_Monad")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Control_Applicative" )
                                                           , "applicativeArray" ) ) ) )
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Control_Bind" )
                                                           , "bindArray" ) ) ) ) ) )
           , assign_star( "ps_liftM1"
                        , define( None
                                , ["ps_dictMonad"]
                                , block( ret( define( None
                                                    , ["ps_f"]
                                                    , block( ret( define( None
                                                                        , [ "ps_a" ]
                                                                        , block( ret( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                                , "bind" )
                                                                                                      , call( get_item( var( "ps_dictMonad" )
                                                                                                                      , "Bind1" ) ) )
                                                                                                , var( "ps_a" ) )
                                                                                          , define( None
                                                                                                  , [ "ps_a'" ]
                                                                                                  , block( ret( call( call( get_item( var( "ps_Control_Applicative" )
                                                                                                                                    , "pure" )
                                                                                                                          , call( get_item( var( "ps_dictMonad" )
                                                                                                                                          , "Applicative0" ) ) )
                                                                                                                    , call( var( "ps_f" )
                                                                                                                          , var( "ps_a'" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_ap"
                        , define( None
                                , ["ps_dictMonad"]
                                , block( ret( define( None
                                                    , ["ps_f"]
                                                    , block( ret( define( None
                                                                        , [ "ps_a" ]
                                                                        , block( ret( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                                , "bind" )
                                                                                                      , call( get_item( var( "ps_dictMonad" )
                                                                                                                      , "Bind1" ) ) )
                                                                                                , var( "ps_f" ) )
                                                                                          , define( None
                                                                                                  , [ "ps_f'" ]
                                                                                                  , block( ret( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                                                          , "bind" )
                                                                                                                                , call( get_item( var( "ps_dictMonad" )
                                                                                                                                                , "Bind1" ) ) )
                                                                                                                          , var( "ps_a" ) )
                                                                                                                    , define( None
                                                                                                                            , [ "ps_a'" ]
                                                                                                                            , block( ret( call( call( get_item( var( "ps_Control_Applicative" )
                                                                                                                                                              , "pure" )
                                                                                                                                                    , call( get_item( var( "ps_dictMonad" )
                                                                                                                                                                    , "Applicative0" ) ) )
                                                                                                                                              , call( var( "ps_f'" )
                                                                                                                                                    , var( "ps_a'" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("Monad", var("ps_Monad"))
                           , ("liftM1", var("ps_liftM1"))
                           , ("ap", var("ps_ap"))
                           , ("whenM", var("ps_whenM"))
                           , ("unlessM", var("ps_unlessM"))
                           , ("monadFn", var("ps_monadFn"))
                           , ("monadArray", var("ps_monadArray")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Control\\Monad.purs", name="purescript_show_python.Control.Monad.pure")
