from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_Control_Apply"
                        , call( var('import_module')
                              , "purescript_show_python.Control.Apply.pure" ) )
           , assign_star( "ps_Data_Unit"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Unit.pure" ) )
           , assign_star( "ps_Applicative"
                        , define( None
                                , ["ps_Apply0", "ps_pure", ".this"]
                                , block( set_item( var(".this")
                                                 , "Apply0"
                                                 , var("ps_Apply0") )
                                       , set_item( var(".this")
                                                 , "pure"
                                                 , var("ps_pure") )
                                       , var(".this") ) ) )
           , assign_star( "ps_pure"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "pure" ) ) ) ) )
           , assign_star( "ps_unless"
                        , define( None
                                , ["ps_dictApplicative"]
                                , block( ret( define( None
                                                    , ["ps_v"]
                                                    , block( ret( define( None
                                                                        , [ "ps_v1" ]
                                                                        , block( ite( uop( UOp.NOT
                                                                                         , var( "ps_v" ) )
                                                                                    , block( ret( var( "ps_v1" ) ) )
                                                                                    , None )
                                                                               , ite( var( "ps_v" )
                                                                                    , block( ret( call( call( var( "ps_pure" )
                                                                                                            , var( "ps_dictApplicative" ) )
                                                                                                      , get_item( var( "ps_Data_Unit" )
                                                                                                                , "unit" ) ) ) )
                                                                                    , None )
                                                                               , throw( call( var( "Error" )
                                                                                            , binop( "Failed pattern match at purescript_show_python.Control.Applicative.pure (line 62, column 1 - line 62, column 65): "
                                                                                                   , BinOp.ADD
                                                                                                   , call( get_attr( ","
                                                                                                                   , "join" )
                                                                                                         , mktuple( get_attr( get_item( var( "ps_v" )
                                                                                                                                      , ".t" )
                                                                                                                            , "__name__" )
                                                                                                                  , get_attr( get_item( var( "ps_v1" )
                                                                                                                                      , ".t" )
                                                                                                                            , "__name__" ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_when"
                        , define( None
                                , ["ps_dictApplicative"]
                                , block( ret( define( None
                                                    , ["ps_v"]
                                                    , block( ret( define( None
                                                                        , [ "ps_v1" ]
                                                                        , block( ite( var( "ps_v" )
                                                                                    , block( ret( var( "ps_v1" ) ) )
                                                                                    , None )
                                                                               , ite( uop( UOp.NOT
                                                                                         , var( "ps_v" ) )
                                                                                    , block( ret( call( call( var( "ps_pure" )
                                                                                                            , var( "ps_dictApplicative" ) )
                                                                                                      , get_item( var( "ps_Data_Unit" )
                                                                                                                , "unit" ) ) ) )
                                                                                    , None )
                                                                               , throw( call( var( "Error" )
                                                                                            , binop( "Failed pattern match at purescript_show_python.Control.Applicative.pure (line 57, column 1 - line 57, column 63): "
                                                                                                   , BinOp.ADD
                                                                                                   , call( get_attr( ","
                                                                                                                   , "join" )
                                                                                                         , mktuple( get_attr( get_item( var( "ps_v" )
                                                                                                                                      , ".t" )
                                                                                                                            , "__name__" )
                                                                                                                  , get_attr( get_item( var( "ps_v1" )
                                                                                                                                      , ".t" )
                                                                                                                            , "__name__" ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_liftA1"
                        , define( None
                                , ["ps_dictApplicative"]
                                , block( ret( define( None
                                                    , ["ps_f"]
                                                    , block( ret( define( None
                                                                        , [ "ps_a" ]
                                                                        , block( ret( call( call( call( get_item( var( "ps_Control_Apply" )
                                                                                                                , "apply" )
                                                                                                      , call( get_item( var( "ps_dictApplicative" )
                                                                                                                      , "Apply0" ) ) )
                                                                                                , call( call( var( "ps_pure" )
                                                                                                            , var( "ps_dictApplicative" ) )
                                                                                                      , var( "ps_f" ) ) )
                                                                                          , var( "ps_a" ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_applicativeFn"
                        , new( var("ps_Applicative")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Control_Apply" )
                                                           , "applyFn" ) ) ) )
                             , define( None
                                     , ["ps_x"]
                                     , block( ret( define( None
                                                         , ["ps_v"]
                                                         , block( ret( var( "ps_x" ) ) ) ) ) ) ) ) )
           , assign_star( "ps_applicativeArray"
                        , new( var("ps_Applicative")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Control_Apply" )
                                                           , "applyArray" ) ) ) )
                             , define( None
                                     , ["ps_x"]
                                     , block( ret( metadata( 40
                                                           , 12
                                                           , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Control\\Applicative.purs"
                                                           , mktuple( var( "ps_x" ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("Applicative", var("ps_Applicative"))
                           , ("pure", var("ps_pure"))
                           , ("liftA1", var("ps_liftA1"))
                           , ("unless", var("ps_unless"))
                           , ("when", var("ps_when"))
                           , ("applicativeFn", var("ps_applicativeFn"))
                           , ( "applicativeArray"
                             , var("ps_applicativeArray") ) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Control\\Applicative.purs", name="purescript_show_python.Control.Applicative.pure")
