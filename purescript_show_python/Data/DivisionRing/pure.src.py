from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_Data_Ring"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Ring.pure" ) )
           , assign_star( "ps_Data_Semiring"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Semiring.pure" ) )
           , assign_star( "ps_DivisionRing"
                        , define( None
                                , ["ps_Ring0", "ps_recip", ".this"]
                                , block( set_item( var(".this")
                                                 , "Ring0"
                                                 , var("ps_Ring0") )
                                       , set_item( var(".this")
                                                 , "recip"
                                                 , var("ps_recip") )
                                       , var(".this") ) ) )
           , assign_star( "ps_recip"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "recip" ) ) ) ) )
           , assign_star( "ps_rightDiv"
                        , define( None
                                , ["ps_dictDivisionRing"]
                                , block( ret( define( None
                                                    , ["ps_a"]
                                                    , block( ret( define( None
                                                                        , [ "ps_b" ]
                                                                        , block( ret( call( call( call( get_item( var( "ps_Data_Semiring" )
                                                                                                                , "mul" )
                                                                                                      , call( get_item( call( get_item( var( "ps_dictDivisionRing" )
                                                                                                                                      , "Ring0" ) )
                                                                                                                      , "Semiring0" ) ) )
                                                                                                , var( "ps_a" ) )
                                                                                          , call( call( var( "ps_recip" )
                                                                                                      , var( "ps_dictDivisionRing" ) )
                                                                                                , var( "ps_b" ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_leftDiv"
                        , define( None
                                , ["ps_dictDivisionRing"]
                                , block( ret( define( None
                                                    , ["ps_a"]
                                                    , block( ret( define( None
                                                                        , [ "ps_b" ]
                                                                        , block( ret( call( call( call( get_item( var( "ps_Data_Semiring" )
                                                                                                                , "mul" )
                                                                                                      , call( get_item( call( get_item( var( "ps_dictDivisionRing" )
                                                                                                                                      , "Ring0" ) )
                                                                                                                      , "Semiring0" ) ) )
                                                                                                , call( call( var( "ps_recip" )
                                                                                                            , var( "ps_dictDivisionRing" ) )
                                                                                                      , var( "ps_b" ) ) )
                                                                                          , var( "ps_a" ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_divisionringNumber"
                        , new( var("ps_DivisionRing")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Ring")
                                                           , "ringNumber" ) ) ) )
                             , define( None
                                     , ["ps_x"]
                                     , block( ret( ite( call( var('isinstance')
                                                            , metadata( 56
                                                                      , 13
                                                                      , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\DivisionRing.purs"
                                                                      , 1.0 )
                                                            , var('int') )
                                                      , binop( metadata( 56
                                                                       , 13
                                                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\DivisionRing.purs"
                                                                       , 1.0 )
                                                             , BinOp.FLOOR_DIVIDE
                                                             , var("ps_x") )
                                                      , binop( metadata( 56
                                                                       , 13
                                                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\DivisionRing.purs"
                                                                       , 1.0 )
                                                             , BinOp.TRUE_DIVIDE
                                                             , var( "ps_x" ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("DivisionRing", var("ps_DivisionRing"))
                           , ("recip", var("ps_recip"))
                           , ("leftDiv", var("ps_leftDiv"))
                           , ("rightDiv", var("ps_rightDiv"))
                           , ( "divisionringNumber"
                             , var("ps_divisionringNumber") ) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\DivisionRing.purs", name="purescript_show_python.Data.DivisionRing.pure")
