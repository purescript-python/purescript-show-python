from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "$foreign"
                        , call( var('import_module')
                              , "purescript_show_python.ffi.Control.Apply" ) )
           , assign_star( "ps_Control_Category"
                        , call( var('import_module')
                              , "purescript_show_python.Control.Category.pure" ) )
           , assign_star( "ps_Data_Function"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Function.pure" ) )
           , assign_star( "ps_Data_Functor"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Functor.pure" ) )
           , assign_star( "ps_Apply"
                        , define( None
                                , ["ps_Functor0", "ps_apply", ".this"]
                                , block( set_item( var(".this")
                                                 , "Functor0"
                                                 , var("ps_Functor0") )
                                       , set_item( var(".this")
                                                 , "apply"
                                                 , var("ps_apply") )
                                       , var(".this") ) ) )
           , assign_star( "ps_applyFn"
                        , new( var("ps_Apply")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Data_Functor" )
                                                           , "functorFn" ) ) ) )
                             , define( None
                                     , ["ps_f"]
                                     , block( ret( define( None
                                                         , ["ps_g"]
                                                         , block( ret( define( None
                                                                             , [ "ps_x" ]
                                                                             , block( ret( call( call( var( "ps_f" )
                                                                                                     , var( "ps_x" ) )
                                                                                               , call( var( "ps_g" )
                                                                                                     , var( "ps_x" ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_applyArray"
                        , new( var("ps_Apply")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Data_Functor" )
                                                           , "functorArray" ) ) ) )
                             , get_item(var("$foreign"), "arrayApply") ) )
           , assign_star( "ps_apply"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "apply" ) ) ) ) )
           , assign_star( "ps_applyFirst"
                        , define( None
                                , ["ps_dictApply"]
                                , block( ret( define( None
                                                    , ["ps_a"]
                                                    , block( ret( define( None
                                                                        , [ "ps_b" ]
                                                                        , block( ret( call( call( call( var( "ps_apply" )
                                                                                                      , var( "ps_dictApply" ) )
                                                                                                , call( call( call( get_item( var( "ps_Data_Functor" )
                                                                                                                            , "map" )
                                                                                                                  , call( get_item( var( "ps_dictApply" )
                                                                                                                                  , "Functor0" ) ) )
                                                                                                            , get_item( var( "ps_Data_Function" )
                                                                                                                      , "const" ) )
                                                                                                      , var( "ps_a" ) ) )
                                                                                          , var( "ps_b" ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_applySecond"
                        , define( None
                                , ["ps_dictApply"]
                                , block( ret( define( None
                                                    , ["ps_a"]
                                                    , block( ret( define( None
                                                                        , [ "ps_b" ]
                                                                        , block( ret( call( call( call( var( "ps_apply" )
                                                                                                      , var( "ps_dictApply" ) )
                                                                                                , call( call( call( get_item( var( "ps_Data_Functor" )
                                                                                                                            , "map" )
                                                                                                                  , call( get_item( var( "ps_dictApply" )
                                                                                                                                  , "Functor0" ) ) )
                                                                                                            , call( get_item( var( "ps_Data_Function" )
                                                                                                                            , "const" )
                                                                                                                  , call( get_item( var( "ps_Control_Category" )
                                                                                                                                  , "identity" )
                                                                                                                        , get_item( var( "ps_Control_Category" )
                                                                                                                                  , "categoryFn" ) ) ) )
                                                                                                      , var( "ps_a" ) ) )
                                                                                          , var( "ps_b" ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_lift2"
                        , define( None
                                , ["ps_dictApply"]
                                , block( ret( define( None
                                                    , ["ps_f"]
                                                    , block( ret( define( None
                                                                        , [ "ps_a" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_b" ]
                                                                                            , block( ret( call( call( call( var( "ps_apply" )
                                                                                                                          , var( "ps_dictApply" ) )
                                                                                                                    , call( call( call( get_item( var( "ps_Data_Functor" )
                                                                                                                                                , "map" )
                                                                                                                                      , call( get_item( var( "ps_dictApply" )
                                                                                                                                                      , "Functor0" ) ) )
                                                                                                                                , var( "ps_f" ) )
                                                                                                                          , var( "ps_a" ) ) )
                                                                                                              , var( "ps_b" ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_lift3"
                        , define( None
                                , ["ps_dictApply"]
                                , block( ret( define( None
                                                    , ["ps_f"]
                                                    , block( ret( define( None
                                                                        , [ "ps_a" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_b" ]
                                                                                            , block( ret( define( None
                                                                                                                , [ "ps_c" ]
                                                                                                                , block( ret( call( call( call( var( "ps_apply" )
                                                                                                                                              , var( "ps_dictApply" ) )
                                                                                                                                        , call( call( call( var( "ps_apply" )
                                                                                                                                                          , var( "ps_dictApply" ) )
                                                                                                                                                    , call( call( call( get_item( var( "ps_Data_Functor" )
                                                                                                                                                                                , "map" )
                                                                                                                                                                      , call( get_item( var( "ps_dictApply" )
                                                                                                                                                                                      , "Functor0" ) ) )
                                                                                                                                                                , var( "ps_f" ) )
                                                                                                                                                          , var( "ps_a" ) ) )
                                                                                                                                              , var( "ps_b" ) ) )
                                                                                                                                  , var( "ps_c" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_lift4"
                        , define( None
                                , ["ps_dictApply"]
                                , block( ret( define( None
                                                    , ["ps_f"]
                                                    , block( ret( define( None
                                                                        , [ "ps_a" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_b" ]
                                                                                            , block( ret( define( None
                                                                                                                , [ "ps_c" ]
                                                                                                                , block( ret( define( None
                                                                                                                                    , [ "ps_d" ]
                                                                                                                                    , block( ret( call( call( call( var( "ps_apply" )
                                                                                                                                                                  , var( "ps_dictApply" ) )
                                                                                                                                                            , call( call( call( var( "ps_apply" )
                                                                                                                                                                              , var( "ps_dictApply" ) )
                                                                                                                                                                        , call( call( call( var( "ps_apply" )
                                                                                                                                                                                          , var( "ps_dictApply" ) )
                                                                                                                                                                                    , call( call( call( get_item( var( "ps_Data_Functor" )
                                                                                                                                                                                                                , "map" )
                                                                                                                                                                                                      , call( get_item( var( "ps_dictApply" )
                                                                                                                                                                                                                      , "Functor0" ) ) )
                                                                                                                                                                                                , var( "ps_f" ) )
                                                                                                                                                                                          , var( "ps_a" ) ) )
                                                                                                                                                                              , var( "ps_b" ) ) )
                                                                                                                                                                  , var( "ps_c" ) ) )
                                                                                                                                                      , var( "ps_d" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_lift5"
                        , define( None
                                , ["ps_dictApply"]
                                , block( ret( define( None
                                                    , ["ps_f"]
                                                    , block( ret( define( None
                                                                        , [ "ps_a" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_b" ]
                                                                                            , block( ret( define( None
                                                                                                                , [ "ps_c" ]
                                                                                                                , block( ret( define( None
                                                                                                                                    , [ "ps_d" ]
                                                                                                                                    , block( ret( define( None
                                                                                                                                                        , [ "ps_e" ]
                                                                                                                                                        , block( ret( call( call( call( var( "ps_apply" )
                                                                                                                                                                                      , var( "ps_dictApply" ) )
                                                                                                                                                                                , call( call( call( var( "ps_apply" )
                                                                                                                                                                                                  , var( "ps_dictApply" ) )
                                                                                                                                                                                            , call( call( call( var( "ps_apply" )
                                                                                                                                                                                                              , var( "ps_dictApply" ) )
                                                                                                                                                                                                        , call( call( call( var( "ps_apply" )
                                                                                                                                                                                                                          , var( "ps_dictApply" ) )
                                                                                                                                                                                                                    , call( call( call( get_item( var( "ps_Data_Functor" )
                                                                                                                                                                                                                                                , "map" )
                                                                                                                                                                                                                                      , call( get_item( var( "ps_dictApply" )
                                                                                                                                                                                                                                                      , "Functor0" ) ) )
                                                                                                                                                                                                                                , var( "ps_f" ) )
                                                                                                                                                                                                                          , var( "ps_a" ) ) )
                                                                                                                                                                                                              , var( "ps_b" ) ) )
                                                                                                                                                                                                  , var( "ps_c" ) ) )
                                                                                                                                                                                      , var( "ps_d" ) ) )
                                                                                                                                                                          , var( "ps_e" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("Apply", var("ps_Apply"))
                           , ("apply", var("ps_apply"))
                           , ("applyFirst", var("ps_applyFirst"))
                           , ("applySecond", var("ps_applySecond"))
                           , ("lift2", var("ps_lift2"))
                           , ("lift3", var("ps_lift3"))
                           , ("lift4", var("ps_lift4"))
                           , ("lift5", var("ps_lift5"))
                           , ("applyFn", var("ps_applyFn"))
                           , ("applyArray", var("ps_applyArray")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Control\\Apply.purs", name="purescript_show_python.Control.Apply.pure")
