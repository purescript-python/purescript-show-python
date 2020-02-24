from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_Semigroupoid"
                        , define( None
                                , ["ps_compose", ".this"]
                                , block( set_item( var(".this")
                                                 , "compose"
                                                 , var("ps_compose") )
                                       , var(".this") ) ) )
           , assign_star( "ps_semigroupoidFn"
                        , new( var("ps_Semigroupoid")
                             , define( None
                                     , ["ps_f"]
                                     , block( ret( define( None
                                                         , ["ps_g"]
                                                         , block( ret( define( None
                                                                             , [ "ps_x" ]
                                                                             , block( ret( call( var( "ps_f" )
                                                                                               , call( var( "ps_g" )
                                                                                                     , var( "ps_x" ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_compose"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "compose" ) ) ) ) )
           , assign_star( "ps_composeFlipped"
                        , define( None
                                , ["ps_dictSemigroupoid"]
                                , block( ret( define( None
                                                    , ["ps_f"]
                                                    , block( ret( define( None
                                                                        , [ "ps_g" ]
                                                                        , block( ret( call( call( call( var( "ps_compose" )
                                                                                                      , var( "ps_dictSemigroupoid" ) )
                                                                                                , var( "ps_g" ) )
                                                                                          , var( "ps_f" ) ) ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("compose", var("ps_compose"))
                           , ("Semigroupoid", var("ps_Semigroupoid"))
                           , ("composeFlipped", var("ps_composeFlipped"))
                           , ("semigroupoidFn", var("ps_semigroupoidFn")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Control\\Semigroupoid.purs", name="purescript_show_python.Control.Semigroupoid.pure")
