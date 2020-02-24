from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_Data_Ring"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Ring.pure" ) )
           , assign_star( "ps_CommutativeRingRecord"
                        , define( None
                                , ["ps_RingRecord0", ".this"]
                                , block( set_item( var(".this")
                                                 , "RingRecord0"
                                                 , var("ps_RingRecord0") )
                                       , var(".this") ) ) )
           , assign_star( "ps_CommutativeRing"
                        , define( None
                                , ["ps_Ring0", ".this"]
                                , block( set_item( var(".this")
                                                 , "Ring0"
                                                 , var("ps_Ring0") )
                                       , var(".this") ) ) )
           , assign_star( "ps_commutativeRingUnit"
                        , new( var("ps_CommutativeRing")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Ring")
                                                           , "ringUnit" ) ) ) ) ) )
           , assign_star( "ps_commutativeRingRecordNil"
                        , new( var("ps_CommutativeRingRecord")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Ring")
                                                           , "ringRecordNil" ) ) ) ) ) )
           , assign_star( "ps_commutativeRingRecordCons"
                        , define( None
                                , ["ps_dictIsSymbol"]
                                , block( ret( define( None
                                                    , ["ps_dictCons"]
                                                    , block( ret( define( None
                                                                        , [ "ps_dictCommutativeRingRecord" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_dictCommutativeRing" ]
                                                                                            , block( ret( new( var( "ps_CommutativeRingRecord" )
                                                                                                             , define( None
                                                                                                                     , [ "ps_$__unused" ]
                                                                                                                     , block( ret( call( call( call( call( get_item( var( "ps_Data_Ring" )
                                                                                                                                                                   , "ringRecordCons" )
                                                                                                                                                         , var( "ps_dictIsSymbol" ) ) )
                                                                                                                                             , call( get_item( var( "ps_dictCommutativeRingRecord" )
                                                                                                                                                             , "RingRecord0" ) ) )
                                                                                                                                       , call( get_item( var( "ps_dictCommutativeRing" )
                                                                                                                                                       , "Ring0" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_commutativeRingRecord"
                        , define( None
                                , ["ps_dictRowToList"]
                                , block( ret( define( None
                                                    , [ "ps_dictCommutativeRingRecord" ]
                                                    , block( ret( new( var( "ps_CommutativeRing" )
                                                                     , define( None
                                                                             , [ "ps_$__unused" ]
                                                                             , block( ret( call( call( get_item( var( "ps_Data_Ring" )
                                                                                                               , "ringRecord" ) )
                                                                                               , call( get_item( var( "ps_dictCommutativeRingRecord" )
                                                                                                               , "RingRecord0" ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_commutativeRingNumber"
                        , new( var("ps_CommutativeRing")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Ring")
                                                           , "ringNumber" ) ) ) ) ) )
           , assign_star( "ps_commutativeRingInt"
                        , new( var("ps_CommutativeRing")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Ring")
                                                           , "ringInt" ) ) ) ) ) )
           , assign_star( "ps_commutativeRingFn"
                        , define( None
                                , ["ps_dictCommutativeRing"]
                                , block( ret( new( var("ps_CommutativeRing")
                                                 , define( None
                                                         , ["ps_$__unused"]
                                                         , block( ret( call( get_item( var( "ps_Data_Ring" )
                                                                                     , "ringFn" )
                                                                           , call( get_item( var( "ps_dictCommutativeRing" )
                                                                                           , "Ring0" ) ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("CommutativeRing", var("ps_CommutativeRing"))
                           , ( "CommutativeRingRecord"
                             , var("ps_CommutativeRingRecord") )
                           , ( "commutativeRingInt"
                             , var("ps_commutativeRingInt") )
                           , ( "commutativeRingNumber"
                             , var("ps_commutativeRingNumber") )
                           , ( "commutativeRingUnit"
                             , var("ps_commutativeRingUnit") )
                           , ("commutativeRingFn", var("ps_commutativeRingFn"))
                           , ( "commutativeRingRecord"
                             , var("ps_commutativeRingRecord") )
                           , ( "commutativeRingRecordNil"
                             , var("ps_commutativeRingRecordNil") )
                           , ( "commutativeRingRecordCons"
                             , var("ps_commutativeRingRecordCons") ) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\CommutativeRing.purs", name="purescript_show_python.Data.CommutativeRing.pure")
