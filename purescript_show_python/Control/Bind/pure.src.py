from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "$foreign"
                        , call( var('import_module')
                              , "purescript_show_python.ffi.Control.Bind" ) )
           , assign_star( "ps_Control_Apply"
                        , call( var('import_module')
                              , "purescript_show_python.Control.Apply.pure" ) )
           , assign_star( "ps_Control_Category"
                        , call( var('import_module')
                              , "purescript_show_python.Control.Category.pure" ) )
           , assign_star( "ps_Data_Function"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Function.pure" ) )
           , assign_star( "ps_Discard"
                        , define( None
                                , ["ps_discard", ".this"]
                                , block( set_item( var(".this")
                                                 , "discard"
                                                 , var("ps_discard") )
                                       , var(".this") ) ) )
           , assign_star( "ps_Bind"
                        , define( None
                                , ["ps_Apply0", "ps_bind", ".this"]
                                , block( set_item( var(".this")
                                                 , "Apply0"
                                                 , var("ps_Apply0") )
                                       , set_item( var(".this")
                                                 , "bind"
                                                 , var("ps_bind") )
                                       , var(".this") ) ) )
           , assign_star( "ps_discard"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "discard" ) ) ) ) )
           , assign_star( "ps_bindFn"
                        , new( var("ps_Bind")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Control_Apply" )
                                                           , "applyFn" ) ) ) )
                             , define( None
                                     , ["ps_m"]
                                     , block( ret( define( None
                                                         , ["ps_f"]
                                                         , block( ret( define( None
                                                                             , [ "ps_x" ]
                                                                             , block( ret( call( call( var( "ps_f" )
                                                                                                     , call( var( "ps_m" )
                                                                                                           , var( "ps_x" ) ) )
                                                                                               , var( "ps_x" ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_bindArray"
                        , new( var("ps_Bind")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Control_Apply" )
                                                           , "applyArray" ) ) ) )
                             , get_item(var("$foreign"), "arrayBind") ) )
           , assign_star( "ps_bind"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "bind" ) ) ) ) )
           , assign_star( "ps_bindFlipped"
                        , define( None
                                , ["ps_dictBind"]
                                , block( ret( call( get_item( var( "ps_Data_Function" )
                                                            , "flip" )
                                                  , call( var("ps_bind")
                                                        , var( "ps_dictBind" ) ) ) ) ) ) )
           , assign_star( "ps_composeKleisliFlipped"
                        , define( None
                                , ["ps_dictBind"]
                                , block( ret( define( None
                                                    , ["ps_f"]
                                                    , block( ret( define( None
                                                                        , [ "ps_g" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_a" ]
                                                                                            , block( ret( call( call( call( var( "ps_bindFlipped" )
                                                                                                                          , var( "ps_dictBind" ) )
                                                                                                                    , var( "ps_f" ) )
                                                                                                              , call( var( "ps_g" )
                                                                                                                    , var( "ps_a" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_composeKleisli"
                        , define( None
                                , ["ps_dictBind"]
                                , block( ret( define( None
                                                    , ["ps_f"]
                                                    , block( ret( define( None
                                                                        , [ "ps_g" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_a" ]
                                                                                            , block( ret( call( call( call( var( "ps_bind" )
                                                                                                                          , var( "ps_dictBind" ) )
                                                                                                                    , call( var( "ps_f" )
                                                                                                                          , var( "ps_a" ) ) )
                                                                                                              , var( "ps_g" ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_discardUnit"
                        , new( var("ps_Discard")
                             , define( None
                                     , ["ps_dictBind"]
                                     , block( ret( call( var("ps_bind")
                                                       , var( "ps_dictBind" ) ) ) ) ) ) )
           , assign_star( "ps_ifM"
                        , define( None
                                , ["ps_dictBind"]
                                , block( ret( define( None
                                                    , ["ps_cond"]
                                                    , block( ret( define( None
                                                                        , [ "ps_t" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_f" ]
                                                                                            , block( ret( call( call( call( var( "ps_bind" )
                                                                                                                          , var( "ps_dictBind" ) )
                                                                                                                    , var( "ps_cond" ) )
                                                                                                              , define( None
                                                                                                                      , [ "ps_cond'" ]
                                                                                                                      , block( ite( var( "ps_cond'" )
                                                                                                                                  , block( ret( var( "ps_t" ) ) )
                                                                                                                                  , None )
                                                                                                                             , ret( var( "ps_f" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_join"
                        , define( None
                                , ["ps_dictBind"]
                                , block( ret( define( None
                                                    , ["ps_m"]
                                                    , block( ret( call( call( call( var( "ps_bind" )
                                                                                  , var( "ps_dictBind" ) )
                                                                            , var( "ps_m" ) )
                                                                      , call( get_item( var( "ps_Control_Category" )
                                                                                      , "identity" )
                                                                            , get_item( var( "ps_Control_Category" )
                                                                                      , "categoryFn" ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("Bind", var("ps_Bind"))
                           , ("bind", var("ps_bind"))
                           , ("bindFlipped", var("ps_bindFlipped"))
                           , ("Discard", var("ps_Discard"))
                           , ("discard", var("ps_discard"))
                           , ("join", var("ps_join"))
                           , ("composeKleisli", var("ps_composeKleisli"))
                           , ( "composeKleisliFlipped"
                             , var("ps_composeKleisliFlipped") )
                           , ("ifM", var("ps_ifM"))
                           , ("bindFn", var("ps_bindFn"))
                           , ("bindArray", var("ps_bindArray"))
                           , ("discardUnit", var("ps_discardUnit")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Control\\Bind.purs", name="purescript_show_python.Control.Bind.pure")
