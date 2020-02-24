from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_Data_Eq"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Eq.pure" ) )
           , assign_star( "ps_Data_Semigroup"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Semigroup.pure" ) )
           , assign_star( "ps_Data_Show"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Show.pure" ) )
           , assign_star( "ps_LT"
                        , block( define("ps_LT", [".this"], block(var(".this")))
                               , set_attr( var("ps_LT")
                                         , "value"
                                         , new(var("ps_LT")) )
                               , var("ps_LT") ) )
           , assign_star( "ps_GT"
                        , block( define("ps_GT", [".this"], block(var(".this")))
                               , set_attr( var("ps_GT")
                                         , "value"
                                         , new(var("ps_GT")) )
                               , var("ps_GT") ) )
           , assign_star( "ps_EQ"
                        , block( define("ps_EQ", [".this"], block(var(".this")))
                               , set_attr( var("ps_EQ")
                                         , "value"
                                         , new(var("ps_EQ")) )
                               , var("ps_EQ") ) )
           , assign_star( "ps_showOrdering"
                        , new( get_item(var("ps_Data_Show"), "Show")
                             , define( None
                                     , ["ps_v"]
                                     , block( ite( isa( var("ps_v")
                                                      , var("ps_LT") )
                                                 , block( ret( metadata( 28
                                                                       , 13
                                                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ordering.purs"
                                                                       , "LT" ) ) )
                                                 , None )
                                            , ite( isa( var("ps_v")
                                                      , var("ps_GT") )
                                                 , block( ret( metadata( 29
                                                                       , 13
                                                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ordering.purs"
                                                                       , "GT" ) ) )
                                                 , None )
                                            , ite( isa( var("ps_v")
                                                      , var("ps_EQ") )
                                                 , block( ret( metadata( 30
                                                                       , 13
                                                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ordering.purs"
                                                                       , "EQ" ) ) )
                                                 , None )
                                            , throw( call( var("Error")
                                                         , binop( "Failed pattern match at purescript_show_python.Data.Ordering.pure (line 26, column 1 - line 29, column 17): "
                                                                , BinOp.ADD
                                                                , call( get_attr( ","
                                                                                , "join" )
                                                                      , mktuple( get_attr( get_item( var( "ps_v" )
                                                                                                   , ".t" )
                                                                                         , "__name__" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_semigroupOrdering"
                        , new( get_item(var("ps_Data_Semigroup"), "Semigroup")
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ite( isa( var( "ps_v" )
                                                                          , var( "ps_LT" ) )
                                                                     , block( ret( get_attr( var( "ps_LT" )
                                                                                           , "value" ) ) )
                                                                     , None )
                                                                , ite( isa( var( "ps_v" )
                                                                          , var( "ps_GT" ) )
                                                                     , block( ret( get_attr( var( "ps_GT" )
                                                                                           , "value" ) ) )
                                                                     , None )
                                                                , ite( isa( var( "ps_v" )
                                                                          , var( "ps_EQ" ) )
                                                                     , block( ret( var( "ps_v1" ) ) )
                                                                     , None )
                                                                , throw( call( var( "Error" )
                                                                             , binop( "Failed pattern match at purescript_show_python.Data.Ordering.pure (line 21, column 1 - line 24, column 18): "
                                                                                    , BinOp.ADD
                                                                                    , call( get_attr( ","
                                                                                                    , "join" )
                                                                                          , mktuple( get_attr( get_item( var( "ps_v" )
                                                                                                                       , ".t" )
                                                                                                             , "__name__" )
                                                                                                   , get_attr( get_item( var( "ps_v1" )
                                                                                                                       , ".t" )
                                                                                                             , "__name__" ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_invert"
                        , define( None
                                , ["ps_v"]
                                , block( ite( isa(var("ps_v"), var("ps_GT"))
                                            , block( ret( get_attr( var("ps_LT")
                                                                  , "value" ) ) )
                                            , None )
                                       , ite( isa(var("ps_v"), var("ps_EQ"))
                                            , block( ret( get_attr( var("ps_EQ")
                                                                  , "value" ) ) )
                                            , None )
                                       , ite( isa(var("ps_v"), var("ps_LT"))
                                            , block( ret( get_attr( var("ps_GT")
                                                                  , "value" ) ) )
                                            , None )
                                       , throw( call( var("Error")
                                                    , binop( "Failed pattern match at purescript_show_python.Data.Ordering.pure (line 33, column 1 - line 33, column 31): "
                                                           , BinOp.ADD
                                                           , call( get_attr( ","
                                                                           , "join" )
                                                                 , mktuple( get_attr( get_item( var( "ps_v" )
                                                                                              , ".t" )
                                                                                    , "__name__" ) ) ) ) ) ) ) ) )
           , assign_star( "ps_eqOrdering"
                        , new( get_item(var("ps_Data_Eq"), "Eq")
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ite( ite( isa( var( "ps_v" )
                                                                               , var( "ps_LT" ) )
                                                                          , isa( var( "ps_v1" )
                                                                               , var( "ps_LT" ) )
                                                                          , False )
                                                                     , block( ret( metadata( 17
                                                                                           , 14
                                                                                           , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ordering.purs"
                                                                                           , True ) ) )
                                                                     , None )
                                                                , ite( ite( isa( var( "ps_v" )
                                                                               , var( "ps_GT" ) )
                                                                          , isa( var( "ps_v1" )
                                                                               , var( "ps_GT" ) )
                                                                          , False )
                                                                     , block( ret( metadata( 18
                                                                                           , 14
                                                                                           , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ordering.purs"
                                                                                           , True ) ) )
                                                                     , None )
                                                                , ite( ite( isa( var( "ps_v" )
                                                                               , var( "ps_EQ" ) )
                                                                          , isa( var( "ps_v1" )
                                                                               , var( "ps_EQ" ) )
                                                                          , False )
                                                                     , block( ret( metadata( 19
                                                                                           , 14
                                                                                           , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ordering.purs"
                                                                                           , True ) ) )
                                                                     , None )
                                                                , ret( metadata( 20
                                                                               , 14
                                                                               , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ordering.purs"
                                                                               , False ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("LT", var("ps_LT"))
                           , ("GT", var("ps_GT"))
                           , ("EQ", var("ps_EQ"))
                           , ("invert", var("ps_invert"))
                           , ("eqOrdering", var("ps_eqOrdering"))
                           , ("semigroupOrdering", var("ps_semigroupOrdering"))
                           , ("showOrdering", var("ps_showOrdering")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ordering.purs", name="purescript_show_python.Data.Ordering.pure")
