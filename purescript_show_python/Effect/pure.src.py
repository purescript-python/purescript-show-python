from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( " | This module provides the `Effect` type, which is used to represent | _native_ effects. The `Effect` type provides a typed API for effectful | computations, while at the same time generating efficient JavaScript."
           , assign_star( "$foreign"
                        , call( var('import_module')
                              , "purescript_show_python.ffi.Effect" ) )
           , assign_star( "ps_Control_Applicative"
                        , call( var('import_module')
                              , "purescript_show_python.Control.Applicative.pure" ) )
           , assign_star( "ps_Control_Apply"
                        , call( var('import_module')
                              , "purescript_show_python.Control.Apply.pure" ) )
           , assign_star( "ps_Control_Bind"
                        , call( var('import_module')
                              , "purescript_show_python.Control.Bind.pure" ) )
           , assign_star( "ps_Control_Monad"
                        , call( var('import_module')
                              , "purescript_show_python.Control.Monad.pure" ) )
           , assign_star( "ps_Data_Functor"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Functor.pure" ) )
           , assign_star( "ps_Data_Monoid"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Monoid.pure" ) )
           , assign_star( "ps_Data_Semigroup"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Semigroup.pure" ) )
           , assign_star( "ps_monadEffect"
                        , new( get_item(var("ps_Control_Monad"), "Monad")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block(ret(var("ps_applicativeEffect"))) )
                             , define( None
                                     , ["ps_$__unused"]
                                     , block(ret(var("ps_bindEffect"))) ) ) )
           , assign_star( "ps_bindEffect"
                        , new( get_item(var("ps_Control_Bind"), "Bind")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block(ret(var("ps_applyEffect"))) )
                             , get_item(var("$foreign"), "bindE") ) )
           , assign_star( "ps_applyEffect"
                        , new( get_item(var("ps_Control_Apply"), "Apply")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block(ret(var("ps_functorEffect"))) )
                             , call( get_item(var("ps_Control_Monad"), "ap")
                                   , var("ps_monadEffect") ) ) )
           , assign_star( "ps_applicativeEffect"
                        , new( get_item( var("ps_Control_Applicative")
                                       , "Applicative" )
                             , define( None
                                     , ["ps_$__unused"]
                                     , block(ret(var("ps_applyEffect"))) )
                             , get_item(var("$foreign"), "pureE") ) )
           , assign_star( "ps_functorEffect"
                        , new( get_item(var("ps_Data_Functor"), "Functor")
                             , call( get_item( var("ps_Control_Applicative")
                                             , "liftA1" )
                                   , var("ps_applicativeEffect") ) ) )
           , assign_star( "ps_semigroupEffect"
                        , define( None
                                , ["ps_dictSemigroup"]
                                , block( ret( new( get_item( var( "ps_Data_Semigroup" )
                                                           , "Semigroup" )
                                                 , call( call( get_item( var( "ps_Control_Apply" )
                                                                       , "lift2" )
                                                             , var( "ps_applyEffect" ) )
                                                       , call( get_item( var( "ps_Data_Semigroup" )
                                                                       , "append" )
                                                             , var( "ps_dictSemigroup" ) ) ) ) ) ) ) )
           , assign_star( "ps_monoidEffect"
                        , define( None
                                , ["ps_dictMonoid"]
                                , block( ret( new( get_item( var( "ps_Data_Monoid" )
                                                           , "Monoid" )
                                                 , define( None
                                                         , ["ps_$__unused"]
                                                         , block( ret( call( var( "ps_semigroupEffect" )
                                                                           , call( get_item( var( "ps_dictMonoid" )
                                                                                           , "Semigroup0" ) ) ) ) ) )
                                                 , call( get_item( var( "$foreign" )
                                                                 , "pureE" )
                                                       , call( get_item( var( "ps_Data_Monoid" )
                                                                       , "mempty" )
                                                             , var( "ps_dictMonoid" ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("functorEffect", var("ps_functorEffect"))
                           , ("applyEffect", var("ps_applyEffect"))
                           , ("applicativeEffect", var("ps_applicativeEffect"))
                           , ("bindEffect", var("ps_bindEffect"))
                           , ("monadEffect", var("ps_monadEffect"))
                           , ("semigroupEffect", var("ps_semigroupEffect"))
                           , ("monoidEffect", var("ps_monoidEffect"))
                           , ("untilE", get_item(var("$foreign"), "untilE"))
                           , ("whileE", get_item(var("$foreign"), "whileE"))
                           , ("forE", get_item(var("$foreign"), "forE"))
                           , ( "foreachE"
                             , get_item(var("$foreign"), "foreachE") ) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\effect\\v2.0.1\\src\\Effect.purs", name="purescript_show_python.Effect.pure")
