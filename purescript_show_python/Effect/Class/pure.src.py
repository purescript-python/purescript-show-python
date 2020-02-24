from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_Control_Category"
                        , call( var('import_module')
                              , "purescript_show_python.Control.Category.pure" ) )
           , assign_star( "ps_Effect"
                        , call( var('import_module')
                              , "purescript_show_python.Effect.pure" ) )
           , assign_star( "ps_MonadEffect"
                        , define( None
                                , ["ps_Monad0", "ps_liftEffect", ".this"]
                                , block( set_item( var(".this")
                                                 , "Monad0"
                                                 , var("ps_Monad0") )
                                       , set_item( var(".this")
                                                 , "liftEffect"
                                                 , var("ps_liftEffect") )
                                       , var(".this") ) ) )
           , assign_star( "ps_monadEffectEffect"
                        , new( var("ps_MonadEffect")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Effect")
                                                           , "monadEffect" ) ) ) )
                             , call( get_item( var("ps_Control_Category")
                                             , "identity" )
                                   , get_item( var("ps_Control_Category")
                                             , "categoryFn" ) ) ) )
           , assign_star( "ps_liftEffect"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "liftEffect" ) ) ) ) )
           , assign( "exports"
                   , record( ("liftEffect", var("ps_liftEffect"))
                           , ("MonadEffect", var("ps_MonadEffect"))
                           , ( "monadEffectEffect"
                             , var("ps_monadEffectEffect") ) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\effect\\v2.0.1\\src\\Effect\\Class.purs", name="purescript_show_python.Effect.Class.pure")
