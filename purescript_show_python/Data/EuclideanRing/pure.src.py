from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "$foreign"
                        , call( var('import_module')
                              , "purescript_show_python.ffi.Data.EuclideanRing" ) )
           , assign_star( "ps_Data_CommutativeRing"
                        , call( var('import_module')
                              , "purescript_show_python.Data.CommutativeRing.pure" ) )
           , assign_star( "ps_Data_Eq"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Eq.pure" ) )
           , assign_star( "ps_Data_Semiring"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Semiring.pure" ) )
           , assign_star( "ps_EuclideanRing"
                        , define( None
                                , [ "ps_CommutativeRing0"
                                , "ps_degree"
                                , "ps_div"
                                , "ps_mod"
                                , ".this" ]
                                , block( set_item( var(".this")
                                                 , "CommutativeRing0"
                                                 , var("ps_CommutativeRing0") )
                                       , set_item( var(".this")
                                                 , "degree"
                                                 , var("ps_degree") )
                                       , set_item( var(".this")
                                                 , "div"
                                                 , var("ps_div") )
                                       , set_item( var(".this")
                                                 , "mod"
                                                 , var("ps_mod") )
                                       , var(".this") ) ) )
           , assign_star( "ps_mod"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "mod" ) ) ) ) )
           , assign_star( "ps_gcd"
                        , define( None
                                , ["ps_$copy_dictEq"]
                                , block( ret( define( None
                                                    , [ "ps_$copy_dictEuclideanRing" ]
                                                    , block( ret( define( None
                                                                        , [ "ps_$copy_a" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_$copy_b" ]
                                                                                            , block( assign_star( "ps_$tco_var_dictEq"
                                                                                                                , var( "ps_$copy_dictEq" ) )
                                                                                                   , assign_star( "ps_$tco_var_dictEuclideanRing"
                                                                                                                , var( "ps_$copy_dictEuclideanRing" ) )
                                                                                                   , assign_star( "ps_$tco_var_a"
                                                                                                                , var( "ps_$copy_a" ) )
                                                                                                   , assign_star( "ps_$tco_done"
                                                                                                                , False )
                                                                                                   , assign_star( "ps_$tco_result"
                                                                                                                , None )
                                                                                                   , define( "ps_$tco_loop"
                                                                                                           , [ "ps_dictEq"
                                                                                                           , "ps_dictEuclideanRing"
                                                                                                           , "ps_a"
                                                                                                           , "ps_b" ]
                                                                                                           , block( assign_star( "ps_$5"
                                                                                                                               , call( call( call( get_item( var( "ps_Data_Eq" )
                                                                                                                                                           , "eq" )
                                                                                                                                                 , var( "ps_dictEq" ) )
                                                                                                                                           , var( "ps_b" ) )
                                                                                                                                     , call( get_item( var( "ps_Data_Semiring" )
                                                                                                                                                     , "zero" )
                                                                                                                                           , call( get_item( call( get_item( call( get_item( var( "ps_dictEuclideanRing" )
                                                                                                                                                                                           , "CommutativeRing0" ) )
                                                                                                                                                                           , "Ring0" ) )
                                                                                                                                                           , "Semiring0" ) ) ) ) )
                                                                                                                  , ite( var( "ps_$5" )
                                                                                                                       , block( assign( "ps_$tco_done"
                                                                                                                                      , True )
                                                                                                                              , ret( var( "ps_a" ) ) )
                                                                                                                       , None )
                                                                                                                  , assign( "ps_$tco_var_dictEq"
                                                                                                                          , var( "ps_dictEq" ) )
                                                                                                                  , assign( "ps_$tco_var_dictEuclideanRing"
                                                                                                                          , var( "ps_dictEuclideanRing" ) )
                                                                                                                  , assign( "ps_$tco_var_a"
                                                                                                                          , var( "ps_b" ) )
                                                                                                                  , assign( "ps_$copy_b"
                                                                                                                          , call( call( call( var( "ps_mod" )
                                                                                                                                            , var( "ps_dictEuclideanRing" ) )
                                                                                                                                      , var( "ps_a" ) )
                                                                                                                                , var( "ps_b" ) ) )
                                                                                                                  , ret(None) ) )
                                                                                                   , loop( uop( UOp.NOT
                                                                                                              , var( "ps_$tco_done" ) )
                                                                                                         , block( assign( "ps_$tco_result"
                                                                                                                        , call( var( "ps_$tco_loop" )
                                                                                                                              , var( "ps_$tco_var_dictEq" )
                                                                                                                              , var( "ps_$tco_var_dictEuclideanRing" )
                                                                                                                              , var( "ps_$tco_var_a" )
                                                                                                                              , var( "ps_$copy_b" ) ) ) ) )
                                                                                                   , ret( var( "ps_$tco_result" ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_euclideanRingNumber"
                        , new( var("ps_EuclideanRing")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Data_CommutativeRing" )
                                                           , "commutativeRingNumber" ) ) ) )
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( metadata( 77
                                                           , 14
                                                           , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\EuclideanRing.purs"
                                                           , 1 ) ) ) )
                             , get_item(var("$foreign"), "numDiv")
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( metadata( 79
                                                                               , 13
                                                                               , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\EuclideanRing.purs"
                                                                               , 0.0 ) ) ) ) ) ) ) ) )
           , assign_star( "ps_euclideanRingInt"
                        , new( var("ps_EuclideanRing")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Data_CommutativeRing" )
                                                           , "commutativeRingInt" ) ) ) )
                             , get_item(var("$foreign"), "intDegree")
                             , get_item(var("$foreign"), "intDiv")
                             , get_item(var("$foreign"), "intMod") ) )
           , assign_star( "ps_div"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "div" ) ) ) ) )
           , assign_star( "ps_lcm"
                        , define( None
                                , ["ps_dictEq"]
                                , block( ret( define( None
                                                    , ["ps_dictEuclideanRing"]
                                                    , block( ret( define( None
                                                                        , [ "ps_a" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_b" ]
                                                                                            , block( assign_star( "ps_$6"
                                                                                                                , ite( call( call( call( get_item( var( "ps_Data_Eq" )
                                                                                                                                                 , "eq" )
                                                                                                                                       , var( "ps_dictEq" ) )
                                                                                                                                 , var( "ps_a" ) )
                                                                                                                           , call( get_item( var( "ps_Data_Semiring" )
                                                                                                                                           , "zero" )
                                                                                                                                 , call( get_item( call( get_item( call( get_item( var( "ps_dictEuclideanRing" )
                                                                                                                                                                                 , "CommutativeRing0" ) )
                                                                                                                                                                 , "Ring0" ) )
                                                                                                                                                 , "Semiring0" ) ) ) )
                                                                                                                     , True
                                                                                                                     , call( call( call( get_item( var( "ps_Data_Eq" )
                                                                                                                                                 , "eq" )
                                                                                                                                       , var( "ps_dictEq" ) )
                                                                                                                                 , var( "ps_b" ) )
                                                                                                                           , call( get_item( var( "ps_Data_Semiring" )
                                                                                                                                           , "zero" )
                                                                                                                                 , call( get_item( call( get_item( call( get_item( var( "ps_dictEuclideanRing" )
                                                                                                                                                                                 , "CommutativeRing0" ) )
                                                                                                                                                                 , "Ring0" ) )
                                                                                                                                                 , "Semiring0" ) ) ) ) ) )
                                                                                                   , ite( var( "ps_$6" )
                                                                                                        , block( ret( call( get_item( var( "ps_Data_Semiring" )
                                                                                                                                    , "zero" )
                                                                                                                          , call( get_item( call( get_item( call( get_item( var( "ps_dictEuclideanRing" )
                                                                                                                                                                          , "CommutativeRing0" ) )
                                                                                                                                                          , "Ring0" ) )
                                                                                                                                          , "Semiring0" ) ) ) ) )
                                                                                                        , None )
                                                                                                   , ret( call( call( call( var( "ps_div" )
                                                                                                                          , var( "ps_dictEuclideanRing" ) )
                                                                                                                    , call( call( call( get_item( var( "ps_Data_Semiring" )
                                                                                                                                                , "mul" )
                                                                                                                                      , call( get_item( call( get_item( call( get_item( var( "ps_dictEuclideanRing" )
                                                                                                                                                                                      , "CommutativeRing0" ) )
                                                                                                                                                                      , "Ring0" ) )
                                                                                                                                                      , "Semiring0" ) ) )
                                                                                                                                , var( "ps_a" ) )
                                                                                                                          , var( "ps_b" ) ) )
                                                                                                              , call( call( call( call( var( "ps_gcd" )
                                                                                                                                      , var( "ps_dictEq" ) )
                                                                                                                                , var( "ps_dictEuclideanRing" ) )
                                                                                                                          , var( "ps_a" ) )
                                                                                                                    , var( "ps_b" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_degree"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "degree" ) ) ) ) )
           , assign( "exports"
                   , record( ("EuclideanRing", var("ps_EuclideanRing"))
                           , ("degree", var("ps_degree"))
                           , ("div", var("ps_div"))
                           , ("mod", var("ps_mod"))
                           , ("gcd", var("ps_gcd"))
                           , ("lcm", var("ps_lcm"))
                           , ("euclideanRingInt", var("ps_euclideanRingInt"))
                           , ( "euclideanRingNumber"
                             , var("ps_euclideanRingNumber") ) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\EuclideanRing.purs", name="purescript_show_python.Data.EuclideanRing.pure")
