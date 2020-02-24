from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "$foreign"
                        , call( var('import_module')
                              , "purescript_show_python.ffi.Data.Ring" ) )
           , assign_star( "ps_Data_Semiring"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Semiring.pure" ) )
           , assign_star( "ps_Data_Symbol"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Symbol.pure" ) )
           , assign_star( "ps_Data_Unit"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Unit.pure" ) )
           , assign_star( "ps_Record_Unsafe"
                        , call( var('import_module')
                              , "purescript_show_python.Record.Unsafe.pure" ) )
           , assign_star( "ps_Type_Data_RowList"
                        , call( var('import_module')
                              , "purescript_show_python.Type.Data.RowList.pure" ) )
           , assign_star( "ps_RingRecord"
                        , define( None
                                , [ "ps_SemiringRecord0"
                                , "ps_subRecord"
                                , ".this" ]
                                , block( set_item( var(".this")
                                                 , "SemiringRecord0"
                                                 , var("ps_SemiringRecord0") )
                                       , set_item( var(".this")
                                                 , "subRecord"
                                                 , var("ps_subRecord") )
                                       , var(".this") ) ) )
           , assign_star( "ps_Ring"
                        , define( None
                                , ["ps_Semiring0", "ps_sub", ".this"]
                                , block( set_item( var(".this")
                                                 , "Semiring0"
                                                 , var("ps_Semiring0") )
                                       , set_item( var(".this")
                                                 , "sub"
                                                 , var("ps_sub") )
                                       , var(".this") ) ) )
           , assign_star( "ps_subRecord"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "subRecord" ) ) ) ) )
           , assign_star( "ps_sub"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "sub" ) ) ) ) )
           , assign_star( "ps_ringUnit"
                        , new( var("ps_Ring")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Data_Semiring" )
                                                           , "semiringUnit" ) ) ) )
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( get_item( var( "ps_Data_Unit" )
                                                                               , "unit" ) ) ) ) ) ) ) ) )
           , assign_star( "ps_ringRecordNil"
                        , new( var("ps_RingRecord")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Data_Semiring" )
                                                           , "semiringRecordNil" ) ) ) )
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( define( None
                                                                             , [ "ps_v2" ]
                                                                             , block( ret( metadata( 56
                                                                                                   , 21
                                                                                                   , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ring.purs"
                                                                                                   , record(  ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_ringRecordCons"
                        , define( None
                                , ["ps_dictIsSymbol"]
                                , block( ret( define( None
                                                    , ["ps_dictCons"]
                                                    , block( ret( define( None
                                                                        , [ "ps_dictRingRecord" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_dictRing" ]
                                                                                            , block( ret( new( var( "ps_RingRecord" )
                                                                                                             , define( None
                                                                                                                     , [ "ps_$__unused" ]
                                                                                                                     , block( ret( call( call( call( call( get_item( var( "ps_Data_Semiring" )
                                                                                                                                                                   , "semiringRecordCons" )
                                                                                                                                                         , var( "ps_dictIsSymbol" ) ) )
                                                                                                                                             , call( get_item( var( "ps_dictRingRecord" )
                                                                                                                                                             , "SemiringRecord0" ) ) )
                                                                                                                                       , call( get_item( var( "ps_dictRing" )
                                                                                                                                                       , "Semiring0" ) ) ) ) ) )
                                                                                                             , define( None
                                                                                                                     , [ "ps_v" ]
                                                                                                                     , block( ret( define( None
                                                                                                                                         , [ "ps_ra" ]
                                                                                                                                         , block( ret( define( None
                                                                                                                                                             , [ "ps_rb" ]
                                                                                                                                                             , block( assign_star( "ps_tail"
                                                                                                                                                                                 , call( call( call( call( var( "ps_subRecord" )
                                                                                                                                                                                                         , var( "ps_dictRingRecord" ) )
                                                                                                                                                                                                   , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                                                                                                                                                       , "RLProxy" )
                                                                                                                                                                                                             , "value" ) )
                                                                                                                                                                                             , var( "ps_ra" ) )
                                                                                                                                                                                       , var( "ps_rb" ) ) )
                                                                                                                                                                    , assign_star( "ps_key"
                                                                                                                                                                                 , call( call( get_item( var( "ps_Data_Symbol" )
                                                                                                                                                                                                       , "reflectSymbol" )
                                                                                                                                                                                             , var( "ps_dictIsSymbol" ) )
                                                                                                                                                                                       , get_attr( get_item( var( "ps_Data_Symbol" )
                                                                                                                                                                                                           , "SProxy" )
                                                                                                                                                                                                 , "value" ) ) )
                                                                                                                                                                    , assign_star( "ps_insert"
                                                                                                                                                                                 , call( get_item( var( "ps_Record_Unsafe" )
                                                                                                                                                                                                 , "unsafeSet" )
                                                                                                                                                                                       , var( "ps_key" ) ) )
                                                                                                                                                                    , assign_star( "ps_get"
                                                                                                                                                                                 , call( get_item( var( "ps_Record_Unsafe" )
                                                                                                                                                                                                 , "unsafeGet" )
                                                                                                                                                                                       , var( "ps_key" ) ) )
                                                                                                                                                                    , ret( call( call( var( "ps_insert" )
                                                                                                                                                                                     , call( call( call( var( "ps_sub" )
                                                                                                                                                                                                       , var( "ps_dictRing" ) )
                                                                                                                                                                                                 , call( var( "ps_get" )
                                                                                                                                                                                                       , var( "ps_ra" ) ) )
                                                                                                                                                                                           , call( var( "ps_get" )
                                                                                                                                                                                                 , var( "ps_rb" ) ) ) )
                                                                                                                                                                               , var( "ps_tail" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_ringRecord"
                        , define( None
                                , ["ps_dictRowToList"]
                                , block( ret( define( None
                                                    , ["ps_dictRingRecord"]
                                                    , block( ret( new( var( "ps_Ring" )
                                                                     , define( None
                                                                             , [ "ps_$__unused" ]
                                                                             , block( ret( call( call( get_item( var( "ps_Data_Semiring" )
                                                                                                               , "semiringRecord" ) )
                                                                                               , call( get_item( var( "ps_dictRingRecord" )
                                                                                                               , "SemiringRecord0" ) ) ) ) ) )
                                                                     , call( call( var( "ps_subRecord" )
                                                                                 , var( "ps_dictRingRecord" ) )
                                                                           , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                               , "RLProxy" )
                                                                                     , "value" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_ringNumber"
                        , new( var("ps_Ring")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Data_Semiring" )
                                                           , "semiringNumber" ) ) ) )
                             , get_item(var("$foreign"), "numSub") ) )
           , assign_star( "ps_ringInt"
                        , new( var("ps_Ring")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Data_Semiring" )
                                                           , "semiringInt" ) ) ) )
                             , get_item(var("$foreign"), "intSub") ) )
           , assign_star( "ps_ringFn"
                        , define( None
                                , ["ps_dictRing"]
                                , block( ret( new( var("ps_Ring")
                                                 , define( None
                                                         , ["ps_$__unused"]
                                                         , block( ret( call( get_item( var( "ps_Data_Semiring" )
                                                                                     , "semiringFn" )
                                                                           , call( get_item( var( "ps_dictRing" )
                                                                                           , "Semiring0" ) ) ) ) ) )
                                                 , define( None
                                                         , ["ps_f"]
                                                         , block( ret( define( None
                                                                             , [ "ps_g" ]
                                                                             , block( ret( define( None
                                                                                                 , [ "ps_x" ]
                                                                                                 , block( ret( call( call( call( var( "ps_sub" )
                                                                                                                               , var( "ps_dictRing" ) )
                                                                                                                         , call( var( "ps_f" )
                                                                                                                               , var( "ps_x" ) ) )
                                                                                                                   , call( var( "ps_g" )
                                                                                                                         , var( "ps_x" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_negate"
                        , define( None
                                , ["ps_dictRing"]
                                , block( ret( define( None
                                                    , ["ps_a"]
                                                    , block( ret( call( call( call( var( "ps_sub" )
                                                                                  , var( "ps_dictRing" ) )
                                                                            , call( get_item( var( "ps_Data_Semiring" )
                                                                                            , "zero" )
                                                                                  , call( get_item( var( "ps_dictRing" )
                                                                                                  , "Semiring0" ) ) ) )
                                                                      , var( "ps_a" ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("Ring", var("ps_Ring"))
                           , ("sub", var("ps_sub"))
                           , ("negate", var("ps_negate"))
                           , ("RingRecord", var("ps_RingRecord"))
                           , ("subRecord", var("ps_subRecord"))
                           , ("ringInt", var("ps_ringInt"))
                           , ("ringNumber", var("ps_ringNumber"))
                           , ("ringUnit", var("ps_ringUnit"))
                           , ("ringFn", var("ps_ringFn"))
                           , ("ringRecord", var("ps_ringRecord"))
                           , ("ringRecordNil", var("ps_ringRecordNil"))
                           , ("ringRecordCons", var("ps_ringRecordCons")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ring.purs", name="purescript_show_python.Data.Ring.pure")
