from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_Data_Boolean"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Boolean.pure" ) )
           , assign_star( "ps_on"
                        , define( None
                                , ["ps_f"]
                                , block( ret( define( None
                                                    , ["ps_g"]
                                                    , block( ret( define( None
                                                                        , [ "ps_x" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_y" ]
                                                                                            , block( ret( call( call( var( "ps_f" )
                                                                                                                    , call( var( "ps_g" )
                                                                                                                          , var( "ps_x" ) ) )
                                                                                                              , call( var( "ps_g" )
                                                                                                                    , var( "ps_y" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_flip"
                        , define( None
                                , ["ps_f"]
                                , block( ret( define( None
                                                    , ["ps_b"]
                                                    , block( ret( define( None
                                                                        , [ "ps_a" ]
                                                                        , block( ret( call( call( var( "ps_f" )
                                                                                                , var( "ps_a" ) )
                                                                                          , var( "ps_b" ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_const"
                        , define( None
                                , ["ps_a"]
                                , block( ret( define( None
                                                    , ["ps_v"]
                                                    , block( ret( var( "ps_a" ) ) ) ) ) ) ) )
           , assign_star( "ps_applyN"
                        , define( None
                                , ["ps_f"]
                                , block( assign_star( "ps_go"
                                                    , define( None
                                                            , ["ps_$copy_n"]
                                                            , block( ret( define( None
                                                                                , [ "ps_$copy_acc" ]
                                                                                , block( assign_star( "ps_$tco_var_n"
                                                                                                    , var( "ps_$copy_n" ) )
                                                                                       , assign_star( "ps_$tco_done"
                                                                                                    , False )
                                                                                       , assign_star( "ps_$tco_result"
                                                                                                    , None )
                                                                                       , define( "ps_$tco_loop"
                                                                                               , [ "ps_n"
                                                                                               , "ps_acc" ]
                                                                                               , block( ite( cmp( var( "ps_n" )
                                                                                                                , Compare.LE
                                                                                                                , metadata( 96
                                                                                                                          , 12
                                                                                                                          , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Function.purs"
                                                                                                                          , 0 ) )
                                                                                                           , block( assign( "ps_$tco_done"
                                                                                                                          , True )
                                                                                                                  , ret( var( "ps_acc" ) ) )
                                                                                                           , None )
                                                                                                      , ite( get_item( var( "ps_Data_Boolean" )
                                                                                                                     , "otherwise" )
                                                                                                           , block( assign( "ps_$tco_var_n"
                                                                                                                          , binop( binop( var( "ps_n" )
                                                                                                                                        , BinOp.SUBTRACT
                                                                                                                                        , metadata( 97
                                                                                                                                                  , 27
                                                                                                                                                  , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Function.purs"
                                                                                                                                                  , 1 ) )
                                                                                                                                 , BinOp.OR
                                                                                                                                 , 0 ) )
                                                                                                                  , assign( "ps_$copy_acc"
                                                                                                                          , call( var( "ps_f" )
                                                                                                                                , var( "ps_acc" ) ) )
                                                                                                                  , ret(None) )
                                                                                                           , None )
                                                                                                      , throw( call( var( "Error" )
                                                                                                                   , binop( "Failed pattern match at purescript_show_python.Data.Function.pure (line 94, column 3 - line 96, column 37): "
                                                                                                                          , BinOp.ADD
                                                                                                                          , call( get_attr( ","
                                                                                                                                          , "join" )
                                                                                                                                , mktuple( get_attr( get_item( var( "ps_n" )
                                                                                                                                                             , ".t" )
                                                                                                                                                   , "__name__" )
                                                                                                                                         , get_attr( get_item( var( "ps_acc" )
                                                                                                                                                             , ".t" )
                                                                                                                                                   , "__name__" ) ) ) ) ) ) ) )
                                                                                       , loop( uop( UOp.NOT
                                                                                                  , var( "ps_$tco_done" ) )
                                                                                             , block( assign( "ps_$tco_result"
                                                                                                            , call( var( "ps_$tco_loop" )
                                                                                                                  , var( "ps_$tco_var_n" )
                                                                                                                  , var( "ps_$copy_acc" ) ) ) ) )
                                                                                       , ret( var( "ps_$tco_result" ) ) ) ) ) ) ) )
                                       , ret(var("ps_go")) ) ) )
           , assign_star( "ps_applyFlipped"
                        , define( None
                                , ["ps_x"]
                                , block( ret( define( None
                                                    , ["ps_f"]
                                                    , block( ret( call( var( "ps_f" )
                                                                      , var( "ps_x" ) ) ) ) ) ) ) ) )
           , assign_star( "ps_apply"
                        , define( None
                                , ["ps_f"]
                                , block( ret( define( None
                                                    , ["ps_x"]
                                                    , block( ret( call( var( "ps_f" )
                                                                      , var( "ps_x" ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("flip", var("ps_flip"))
                           , ("const", var("ps_const"))
                           , ("apply", var("ps_apply"))
                           , ("applyFlipped", var("ps_applyFlipped"))
                           , ("applyN", var("ps_applyN"))
                           , ("on", var("ps_on")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Function.purs", name="purescript_show_python.Data.Function.pure")
