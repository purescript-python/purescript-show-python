from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_Control_Bind"
                        , call( var('import_module')
                              , "purescript_show_python.Control.Bind.pure" ) )
           , assign_star( "ps_Effect"
                        , call( var('import_module')
                              , "purescript_show_python.Effect.pure" ) )
           , assign_star( "ps_Python_IO_Unsafe"
                        , call( var('import_module')
                              , "purescript_show_python.Python.IO.Unsafe.pure" ) )
           , assign_star( "ps_N"
                        , define(None, ["ps_x"], block(ret(var("ps_x")))) )
           , assign_star( "ps_Box"
                        , define(None, ["ps_x"], block(ret(var("ps_x")))) )
           , assign_star( "ps_A1"
                        , block( define( "ps_A1"
                                       , ["ps_value0", "ps_value1", ".this"]
                                       , block( set_item( var(".this")
                                                        , "value0"
                                                        , var("ps_value0") )
                                              , set_item( var(".this")
                                                        , "value1"
                                                        , var("ps_value1") )
                                              , ret(var(".this")) ) )
                               , set_attr( var("ps_A1")
                                         , "create"
                                         , define( None
                                                 , ["ps_value0"]
                                                 , block( ret( define( None
                                                                     , [ "ps_value1" ]
                                                                     , block( ret( new( var( "ps_A1" )
                                                                                      , var( "ps_value0" )
                                                                                      , var( "ps_value1" ) ) ) ) ) ) ) ) )
                               , var("ps_A1") ) )
           , assign_star( "ps_main"
                        , call( call( call( call( get_item( var( "ps_Control_Bind" )
                                                          , "discard" )
                                                , get_item( var( "ps_Control_Bind" )
                                                          , "discardUnit" ) )
                                          , get_item( var("ps_Effect")
                                                    , "bindEffect" ) )
                                    , call( get_item( var("ps_Python_IO_Unsafe")
                                                    , "printLn" )
                                          , metadata( 17
                                                    , 18
                                                    , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\test\\Main.purs"
                                                    , record( ( "a"
                                                              , metadata( 17
                                                                        , 22
                                                                        , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\test\\Main.purs"
                                                                        , 1 ) ) ) ) ) )
                              , define( None
                                      , ["ps_$__unused"]
                                      , block( ret( call( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                    , "discard" )
                                                                          , get_item( var( "ps_Control_Bind" )
                                                                                    , "discardUnit" ) )
                                                                    , get_item( var( "ps_Effect" )
                                                                              , "bindEffect" ) )
                                                              , call( get_item( var( "ps_Python_IO_Unsafe" )
                                                                              , "printLn" )
                                                                    , new( var( "ps_A1" )
                                                                         , metadata( 19
                                                                                   , 23
                                                                                   , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\test\\Main.purs"
                                                                                   , True )
                                                                         , metadata( 19
                                                                                   , 28
                                                                                   , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\test\\Main.purs"
                                                                                   , False ) ) ) )
                                                        , define( None
                                                                , [ "ps_$__unused" ]
                                                                , block( ret( call( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                              , "discard" )
                                                                                                    , get_item( var( "ps_Control_Bind" )
                                                                                                              , "discardUnit" ) )
                                                                                              , get_item( var( "ps_Effect" )
                                                                                                        , "bindEffect" ) )
                                                                                        , call( get_item( var( "ps_Python_IO_Unsafe" )
                                                                                                        , "printLn" )
                                                                                              , var( "ps_N" ) ) )
                                                                                  , define( None
                                                                                          , [ "ps_$__unused" ]
                                                                                          , block( ret( call( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                                                        , "discard" )
                                                                                                                              , get_item( var( "ps_Control_Bind" )
                                                                                                                                        , "discardUnit" ) )
                                                                                                                        , get_item( var( "ps_Effect" )
                                                                                                                                  , "bindEffect" ) )
                                                                                                                  , call( get_item( var( "ps_Python_IO_Unsafe" )
                                                                                                                                  , "printLn" )
                                                                                                                        , metadata( 21
                                                                                                                                  , 22
                                                                                                                                  , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\test\\Main.purs"
                                                                                                                                  , 1 ) ) )
                                                                                                            , define( None
                                                                                                                    , [ "ps_$__unused" ]
                                                                                                                    , block( ret( define( "ps___do"
                                                                                                                                        , [  ]
                                                                                                                                        , block( assign_star( "ps_x"
                                                                                                                                                            , call( call( get_item( var( "ps_Python_IO_Unsafe" )
                                                                                                                                                                                  , "show" )
                                                                                                                                                                        , metadata( 23
                                                                                                                                                                                  , 23
                                                                                                                                                                                  , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\test\\Main.purs"
                                                                                                                                                                                  , 1 ) ) ) )
                                                                                                                                               , assign_star( "ps_y"
                                                                                                                                                            , call( call( get_item( var( "ps_Python_IO_Unsafe" )
                                                                                                                                                                                  , "show" )
                                                                                                                                                                        , metadata( 24
                                                                                                                                                                                  , 20
                                                                                                                                                                                  , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\test\\Main.purs"
                                                                                                                                                                                  , 1 ) ) ) )
                                                                                                                                               , ret( call( call( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                            , "discard" )
                                                                                                                                                                                  , get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                            , "discardUnit" ) )
                                                                                                                                                                            , get_item( var( "ps_Effect" )
                                                                                                                                                                                      , "bindEffect" ) )
                                                                                                                                                                      , call( get_item( var( "ps_Python_IO_Unsafe" )
                                                                                                                                                                                      , "assert" )
                                                                                                                                                                            , cmp( var( "ps_x" )
                                                                                                                                                                                 , Compare.EQ
                                                                                                                                                                                 , var( "ps_y" ) ) ) )
                                                                                                                                                                , define( None
                                                                                                                                                                        , [ "ps_$__unused" ]
                                                                                                                                                                        , block( ret( define( "ps___do"
                                                                                                                                                                                            , [  ]
                                                                                                                                                                                            , block( assign_star( "ps_x1"
                                                                                                                                                                                                                , call( call( get_item( var( "ps_Python_IO_Unsafe" )
                                                                                                                                                                                                                                      , "repr" )
                                                                                                                                                                                                                            , metadata( 27
                                                                                                                                                                                                                                      , 23
                                                                                                                                                                                                                                      , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\test\\Main.purs"
                                                                                                                                                                                                                                      , 1 ) ) ) )
                                                                                                                                                                                                   , assign_star( "ps_y1"
                                                                                                                                                                                                                , call( call( get_item( var( "ps_Python_IO_Unsafe" )
                                                                                                                                                                                                                                      , "repr" )
                                                                                                                                                                                                                            , metadata( 28
                                                                                                                                                                                                                                      , 20
                                                                                                                                                                                                                                      , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\test\\Main.purs"
                                                                                                                                                                                                                                      , 1 ) ) ) )
                                                                                                                                                                                                   , ret( call( call( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                                                                                , "discard" )
                                                                                                                                                                                                                                      , get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                                                                                , "discardUnit" ) )
                                                                                                                                                                                                                                , get_item( var( "ps_Effect" )
                                                                                                                                                                                                                                          , "bindEffect" ) )
                                                                                                                                                                                                                          , call( get_item( var( "ps_Python_IO_Unsafe" )
                                                                                                                                                                                                                                          , "assert" )
                                                                                                                                                                                                                                , cmp( var( "ps_x1" )
                                                                                                                                                                                                                                     , Compare.EQ
                                                                                                                                                                                                                                     , var( "ps_y1" ) ) ) )
                                                                                                                                                                                                                    , define( None
                                                                                                                                                                                                                            , [ "ps_$__unused" ]
                                                                                                                                                                                                                            , block( ret( define( "ps___do"
                                                                                                                                                                                                                                                , [  ]
                                                                                                                                                                                                                                                , block( assign_star( "ps_x2"
                                                                                                                                                                                                                                                                    , call( call( get_item( var( "ps_Python_IO_Unsafe" )
                                                                                                                                                                                                                                                                                          , "repr" )
                                                                                                                                                                                                                                                                                , metadata( 31
                                                                                                                                                                                                                                                                                          , 25
                                                                                                                                                                                                                                                                                          , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\test\\Main.purs"
                                                                                                                                                                                                                                                                                          , 1 ) ) ) )
                                                                                                                                                                                                                                                       , assign_star( "ps_y2"
                                                                                                                                                                                                                                                                    , call( call( get_item( var( "ps_Python_IO_Unsafe" )
                                                                                                                                                                                                                                                                                          , "repr" )
                                                                                                                                                                                                                                                                                , metadata( 32
                                                                                                                                                                                                                                                                                          , 20
                                                                                                                                                                                                                                                                                          , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\test\\Main.purs"
                                                                                                                                                                                                                                                                                          , 1 ) ) ) )
                                                                                                                                                                                                                                                       , ret( call( call( get_item( var( "ps_Python_IO_Unsafe" )
                                                                                                                                                                                                                                                                                  , "assert" )
                                                                                                                                                                                                                                                                        , cmp( var( "ps_x2" )
                                                                                                                                                                                                                                                                             , Compare.EQ
                                                                                                                                                                                                                                                                             , var( "ps_y2" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("A1", var("ps_A1"))
                           , ("N", var("ps_N"))
                           , ("Box", var("ps_Box"))
                           , ("main", var("ps_main")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\test\\Main.purs", name="purescript_show_python.Test.Main.pure")
