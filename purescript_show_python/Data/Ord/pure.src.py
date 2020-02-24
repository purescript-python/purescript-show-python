from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "$foreign"
                        , call( var('import_module')
                              , "purescript_show_python.ffi.Data.Ord" ) )
           , assign_star( "ps_Data_Eq"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Eq.pure" ) )
           , assign_star( "ps_Data_Ordering"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Ordering.pure" ) )
           , assign_star( "ps_Data_Ring"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Ring.pure" ) )
           , assign_star( "ps_Data_Semiring"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Semiring.pure" ) )
           , assign_star( "ps_Data_Symbol"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Symbol.pure" ) )
           , assign_star( "ps_Record_Unsafe"
                        , call( var('import_module')
                              , "purescript_show_python.Record.Unsafe.pure" ) )
           , assign_star( "ps_Type_Data_RowList"
                        , call( var('import_module')
                              , "purescript_show_python.Type.Data.RowList.pure" ) )
           , assign_star( "ps_OrdRecord"
                        , define( None
                                , ["ps_EqRecord0", "ps_compareRecord", ".this"]
                                , block( set_item( var(".this")
                                                 , "EqRecord0"
                                                 , var("ps_EqRecord0") )
                                       , set_item( var(".this")
                                                 , "compareRecord"
                                                 , var("ps_compareRecord") )
                                       , var(".this") ) ) )
           , assign_star( "ps_Ord1"
                        , define( None
                                , ["ps_Eq10", "ps_compare1", ".this"]
                                , block( set_item( var(".this")
                                                 , "Eq10"
                                                 , var("ps_Eq10") )
                                       , set_item( var(".this")
                                                 , "compare1"
                                                 , var("ps_compare1") )
                                       , var(".this") ) ) )
           , assign_star( "ps_Ord"
                        , define( None
                                , ["ps_Eq0", "ps_compare", ".this"]
                                , block( set_item( var(".this")
                                                 , "Eq0"
                                                 , var("ps_Eq0") )
                                       , set_item( var(".this")
                                                 , "compare"
                                                 , var("ps_compare") )
                                       , var(".this") ) ) )
           , assign_star( "ps_ordVoid"
                        , new( var("ps_Ord")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Eq")
                                                           , "eqVoid" ) ) ) )
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( get_attr( get_item( var( "ps_Data_Ordering" )
                                                                                         , "EQ" )
                                                                               , "value" ) ) ) ) ) ) ) ) )
           , assign_star( "ps_ordUnit"
                        , new( var("ps_Ord")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Eq")
                                                           , "eqUnit" ) ) ) )
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( get_attr( get_item( var( "ps_Data_Ordering" )
                                                                                         , "EQ" )
                                                                               , "value" ) ) ) ) ) ) ) ) )
           , assign_star( "ps_ordString"
                        , new( var("ps_Ord")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Eq")
                                                           , "eqString" ) ) ) )
                             , call( call( call( get_item( var("$foreign")
                                                         , "ordStringImpl" )
                                               , get_attr( get_item( var( "ps_Data_Ordering" )
                                                                   , "LT" )
                                                         , "value" ) )
                                         , get_attr( get_item( var( "ps_Data_Ordering" )
                                                             , "EQ" )
                                                   , "value" ) )
                                   , get_attr( get_item( var("ps_Data_Ordering")
                                                       , "GT" )
                                             , "value" ) ) ) )
           , assign_star( "ps_ordRecordNil"
                        , new( var("ps_OrdRecord")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Eq")
                                                           , "eqRowNil" ) ) ) )
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( define( None
                                                                             , [ "ps_v2" ]
                                                                             , block( ret( get_attr( get_item( var( "ps_Data_Ordering" )
                                                                                                             , "EQ" )
                                                                                                   , "value" ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_ordOrdering"
                        , new( var("ps_Ord")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Data_Ordering" )
                                                           , "eqOrdering" ) ) ) )
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ite( ite( isa( var( "ps_v" )
                                                                               , get_item( var( "ps_Data_Ordering" )
                                                                                         , "LT" ) )
                                                                          , isa( var( "ps_v1" )
                                                                               , get_item( var( "ps_Data_Ordering" )
                                                                                         , "LT" ) )
                                                                          , False )
                                                                     , block( ret( get_attr( get_item( var( "ps_Data_Ordering" )
                                                                                                     , "EQ" )
                                                                                           , "value" ) ) )
                                                                     , None )
                                                                , ite( ite( isa( var( "ps_v" )
                                                                               , get_item( var( "ps_Data_Ordering" )
                                                                                         , "EQ" ) )
                                                                          , isa( var( "ps_v1" )
                                                                               , get_item( var( "ps_Data_Ordering" )
                                                                                         , "EQ" ) )
                                                                          , False )
                                                                     , block( ret( get_attr( get_item( var( "ps_Data_Ordering" )
                                                                                                     , "EQ" )
                                                                                           , "value" ) ) )
                                                                     , None )
                                                                , ite( ite( isa( var( "ps_v" )
                                                                               , get_item( var( "ps_Data_Ordering" )
                                                                                         , "GT" ) )
                                                                          , isa( var( "ps_v1" )
                                                                               , get_item( var( "ps_Data_Ordering" )
                                                                                         , "GT" ) )
                                                                          , False )
                                                                     , block( ret( get_attr( get_item( var( "ps_Data_Ordering" )
                                                                                                     , "EQ" )
                                                                                           , "value" ) ) )
                                                                     , None )
                                                                , ite( isa( var( "ps_v" )
                                                                          , get_item( var( "ps_Data_Ordering" )
                                                                                    , "LT" ) )
                                                                     , block( ret( get_attr( get_item( var( "ps_Data_Ordering" )
                                                                                                     , "LT" )
                                                                                           , "value" ) ) )
                                                                     , None )
                                                                , ite( ite( isa( var( "ps_v" )
                                                                               , get_item( var( "ps_Data_Ordering" )
                                                                                         , "EQ" ) )
                                                                          , isa( var( "ps_v1" )
                                                                               , get_item( var( "ps_Data_Ordering" )
                                                                                         , "LT" ) )
                                                                          , False )
                                                                     , block( ret( get_attr( get_item( var( "ps_Data_Ordering" )
                                                                                                     , "GT" )
                                                                                           , "value" ) ) )
                                                                     , None )
                                                                , ite( ite( isa( var( "ps_v" )
                                                                               , get_item( var( "ps_Data_Ordering" )
                                                                                         , "EQ" ) )
                                                                          , isa( var( "ps_v1" )
                                                                               , get_item( var( "ps_Data_Ordering" )
                                                                                         , "GT" ) )
                                                                          , False )
                                                                     , block( ret( get_attr( get_item( var( "ps_Data_Ordering" )
                                                                                                     , "LT" )
                                                                                           , "value" ) ) )
                                                                     , None )
                                                                , ite( isa( var( "ps_v" )
                                                                          , get_item( var( "ps_Data_Ordering" )
                                                                                    , "GT" ) )
                                                                     , block( ret( get_attr( get_item( var( "ps_Data_Ordering" )
                                                                                                     , "GT" )
                                                                                           , "value" ) ) )
                                                                     , None )
                                                                , throw( call( var( "Error" )
                                                                             , binop( "Failed pattern match at purescript_show_python.Data.Ord.pure (line 112, column 1 - line 119, column 21): "
                                                                                    , BinOp.ADD
                                                                                    , call( get_attr( ","
                                                                                                    , "join" )
                                                                                          , mktuple( get_attr( get_item( var( "ps_v" )
                                                                                                                       , ".t" )
                                                                                                             , "__name__" )
                                                                                                   , get_attr( get_item( var( "ps_v1" )
                                                                                                                       , ".t" )
                                                                                                             , "__name__" ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_ordNumber"
                        , new( var("ps_Ord")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Eq")
                                                           , "eqNumber" ) ) ) )
                             , call( call( call( get_item( var("$foreign")
                                                         , "ordNumberImpl" )
                                               , get_attr( get_item( var( "ps_Data_Ordering" )
                                                                   , "LT" )
                                                         , "value" ) )
                                         , get_attr( get_item( var( "ps_Data_Ordering" )
                                                             , "EQ" )
                                                   , "value" ) )
                                   , get_attr( get_item( var("ps_Data_Ordering")
                                                       , "GT" )
                                             , "value" ) ) ) )
           , assign_star( "ps_ordInt"
                        , new( var("ps_Ord")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Eq")
                                                           , "eqInt" ) ) ) )
                             , call( call( call( get_item( var("$foreign")
                                                         , "ordIntImpl" )
                                               , get_attr( get_item( var( "ps_Data_Ordering" )
                                                                   , "LT" )
                                                         , "value" ) )
                                         , get_attr( get_item( var( "ps_Data_Ordering" )
                                                             , "EQ" )
                                                   , "value" ) )
                                   , get_attr( get_item( var("ps_Data_Ordering")
                                                       , "GT" )
                                             , "value" ) ) ) )
           , assign_star( "ps_ordChar"
                        , new( var("ps_Ord")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Eq")
                                                           , "eqChar" ) ) ) )
                             , call( call( call( get_item( var("$foreign")
                                                         , "ordCharImpl" )
                                               , get_attr( get_item( var( "ps_Data_Ordering" )
                                                                   , "LT" )
                                                         , "value" ) )
                                         , get_attr( get_item( var( "ps_Data_Ordering" )
                                                             , "EQ" )
                                                   , "value" ) )
                                   , get_attr( get_item( var("ps_Data_Ordering")
                                                       , "GT" )
                                             , "value" ) ) ) )
           , assign_star( "ps_ordBoolean"
                        , new( var("ps_Ord")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Eq")
                                                           , "eqBoolean" ) ) ) )
                             , call( call( call( get_item( var("$foreign")
                                                         , "ordBooleanImpl" )
                                               , get_attr( get_item( var( "ps_Data_Ordering" )
                                                                   , "LT" )
                                                         , "value" ) )
                                         , get_attr( get_item( var( "ps_Data_Ordering" )
                                                             , "EQ" )
                                                   , "value" ) )
                                   , get_attr( get_item( var("ps_Data_Ordering")
                                                       , "GT" )
                                             , "value" ) ) ) )
           , assign_star( "ps_compareRecord"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "compareRecord" ) ) ) ) )
           , assign_star( "ps_ordRecord"
                        , define( None
                                , ["ps_dictRowToList"]
                                , block( ret( define( None
                                                    , ["ps_dictOrdRecord"]
                                                    , block( ret( new( var( "ps_Ord" )
                                                                     , define( None
                                                                             , [ "ps_$__unused" ]
                                                                             , block( ret( call( call( get_item( var( "ps_Data_Eq" )
                                                                                                               , "eqRec" ) )
                                                                                               , call( get_item( var( "ps_dictOrdRecord" )
                                                                                                               , "EqRecord0" ) ) ) ) ) )
                                                                     , call( call( var( "ps_compareRecord" )
                                                                                 , var( "ps_dictOrdRecord" ) )
                                                                           , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                               , "RLProxy" )
                                                                                     , "value" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_compare1"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "compare1" ) ) ) ) )
           , assign_star( "ps_compare"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "compare" ) ) ) ) )
           , assign_star( "ps_comparing"
                        , define( None
                                , ["ps_dictOrd"]
                                , block( ret( define( None
                                                    , ["ps_f"]
                                                    , block( ret( define( None
                                                                        , [ "ps_x" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_y" ]
                                                                                            , block( ret( call( call( call( var( "ps_compare" )
                                                                                                                          , var( "ps_dictOrd" ) )
                                                                                                                    , call( var( "ps_f" )
                                                                                                                          , var( "ps_x" ) ) )
                                                                                                              , call( var( "ps_f" )
                                                                                                                    , var( "ps_y" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_greaterThan"
                        , define( None
                                , ["ps_dictOrd"]
                                , block( ret( define( None
                                                    , ["ps_a1"]
                                                    , block( ret( define( None
                                                                        , [ "ps_a2" ]
                                                                        , block( assign_star( "ps_v"
                                                                                            , call( call( call( var( "ps_compare" )
                                                                                                              , var( "ps_dictOrd" ) )
                                                                                                        , var( "ps_a1" ) )
                                                                                                  , var( "ps_a2" ) ) )
                                                                               , ite( isa( var( "ps_v" )
                                                                                         , get_item( var( "ps_Data_Ordering" )
                                                                                                   , "GT" ) )
                                                                                    , block( ret( metadata( 131
                                                                                                          , 9
                                                                                                          , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ord.purs"
                                                                                                          , True ) ) )
                                                                                    , None )
                                                                               , ret( metadata( 132
                                                                                              , 8
                                                                                              , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ord.purs"
                                                                                              , False ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_greaterThanOrEq"
                        , define( None
                                , ["ps_dictOrd"]
                                , block( ret( define( None
                                                    , ["ps_a1"]
                                                    , block( ret( define( None
                                                                        , [ "ps_a2" ]
                                                                        , block( assign_star( "ps_v"
                                                                                            , call( call( call( var( "ps_compare" )
                                                                                                              , var( "ps_dictOrd" ) )
                                                                                                        , var( "ps_a1" ) )
                                                                                                  , var( "ps_a2" ) ) )
                                                                               , ite( isa( var( "ps_v" )
                                                                                         , get_item( var( "ps_Data_Ordering" )
                                                                                                   , "LT" ) )
                                                                                    , block( ret( metadata( 143
                                                                                                          , 9
                                                                                                          , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ord.purs"
                                                                                                          , False ) ) )
                                                                                    , None )
                                                                               , ret( metadata( 144
                                                                                              , 8
                                                                                              , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ord.purs"
                                                                                              , True ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_signum"
                        , define( None
                                , ["ps_dictOrd"]
                                , block( ret( define( None
                                                    , ["ps_dictRing"]
                                                    , block( ret( define( None
                                                                        , [ "ps_x" ]
                                                                        , block( assign_star( "ps_$9"
                                                                                            , call( call( call( var( "ps_greaterThanOrEq" )
                                                                                                              , var( "ps_dictOrd" ) )
                                                                                                        , var( "ps_x" ) )
                                                                                                  , call( get_item( var( "ps_Data_Semiring" )
                                                                                                                  , "zero" )
                                                                                                        , call( get_item( var( "ps_dictRing" )
                                                                                                                        , "Semiring0" ) ) ) ) )
                                                                               , ite( var( "ps_$9" )
                                                                                    , block( ret( call( get_item( var( "ps_Data_Semiring" )
                                                                                                                , "one" )
                                                                                                      , call( get_item( var( "ps_dictRing" )
                                                                                                                      , "Semiring0" ) ) ) ) )
                                                                                    , None )
                                                                               , ret( call( call( get_item( var( "ps_Data_Ring" )
                                                                                                          , "negate" )
                                                                                                , var( "ps_dictRing" ) )
                                                                                          , call( get_item( var( "ps_Data_Semiring" )
                                                                                                          , "one" )
                                                                                                , call( get_item( var( "ps_dictRing" )
                                                                                                                , "Semiring0" ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_lessThan"
                        , define( None
                                , ["ps_dictOrd"]
                                , block( ret( define( None
                                                    , ["ps_a1"]
                                                    , block( ret( define( None
                                                                        , [ "ps_a2" ]
                                                                        , block( assign_star( "ps_v"
                                                                                            , call( call( call( var( "ps_compare" )
                                                                                                              , var( "ps_dictOrd" ) )
                                                                                                        , var( "ps_a1" ) )
                                                                                                  , var( "ps_a2" ) ) )
                                                                               , ite( isa( var( "ps_v" )
                                                                                         , get_item( var( "ps_Data_Ordering" )
                                                                                                   , "LT" ) )
                                                                                    , block( ret( metadata( 125
                                                                                                          , 9
                                                                                                          , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ord.purs"
                                                                                                          , True ) ) )
                                                                                    , None )
                                                                               , ret( metadata( 126
                                                                                              , 8
                                                                                              , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ord.purs"
                                                                                              , False ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_lessThanOrEq"
                        , define( None
                                , ["ps_dictOrd"]
                                , block( ret( define( None
                                                    , ["ps_a1"]
                                                    , block( ret( define( None
                                                                        , [ "ps_a2" ]
                                                                        , block( assign_star( "ps_v"
                                                                                            , call( call( call( var( "ps_compare" )
                                                                                                              , var( "ps_dictOrd" ) )
                                                                                                        , var( "ps_a1" ) )
                                                                                                  , var( "ps_a2" ) ) )
                                                                               , ite( isa( var( "ps_v" )
                                                                                         , get_item( var( "ps_Data_Ordering" )
                                                                                                   , "GT" ) )
                                                                                    , block( ret( metadata( 137
                                                                                                          , 9
                                                                                                          , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ord.purs"
                                                                                                          , False ) ) )
                                                                                    , None )
                                                                               , ret( metadata( 138
                                                                                              , 8
                                                                                              , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ord.purs"
                                                                                              , True ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_max"
                        , define( None
                                , ["ps_dictOrd"]
                                , block( ret( define( None
                                                    , ["ps_x"]
                                                    , block( ret( define( None
                                                                        , [ "ps_y" ]
                                                                        , block( assign_star( "ps_v"
                                                                                            , call( call( call( var( "ps_compare" )
                                                                                                              , var( "ps_dictOrd" ) )
                                                                                                        , var( "ps_x" ) )
                                                                                                  , var( "ps_y" ) ) )
                                                                               , ite( isa( var( "ps_v" )
                                                                                         , get_item( var( "ps_Data_Ordering" )
                                                                                                   , "LT" ) )
                                                                                    , block( ret( var( "ps_y" ) ) )
                                                                                    , None )
                                                                               , ite( isa( var( "ps_v" )
                                                                                         , get_item( var( "ps_Data_Ordering" )
                                                                                                   , "EQ" ) )
                                                                                    , block( ret( var( "ps_x" ) ) )
                                                                                    , None )
                                                                               , ite( isa( var( "ps_v" )
                                                                                         , get_item( var( "ps_Data_Ordering" )
                                                                                                   , "GT" ) )
                                                                                    , block( ret( var( "ps_x" ) ) )
                                                                                    , None )
                                                                               , throw( call( var( "Error" )
                                                                                            , binop( "Failed pattern match at purescript_show_python.Data.Ord.pure (line 167, column 3 - line 170, column 12): "
                                                                                                   , BinOp.ADD
                                                                                                   , call( get_attr( ","
                                                                                                                   , "join" )
                                                                                                         , mktuple( get_attr( get_item( var( "ps_v" )
                                                                                                                                      , ".t" )
                                                                                                                            , "__name__" ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_min"
                        , define( None
                                , ["ps_dictOrd"]
                                , block( ret( define( None
                                                    , ["ps_x"]
                                                    , block( ret( define( None
                                                                        , [ "ps_y" ]
                                                                        , block( assign_star( "ps_v"
                                                                                            , call( call( call( var( "ps_compare" )
                                                                                                              , var( "ps_dictOrd" ) )
                                                                                                        , var( "ps_x" ) )
                                                                                                  , var( "ps_y" ) ) )
                                                                               , ite( isa( var( "ps_v" )
                                                                                         , get_item( var( "ps_Data_Ordering" )
                                                                                                   , "LT" ) )
                                                                                    , block( ret( var( "ps_x" ) ) )
                                                                                    , None )
                                                                               , ite( isa( var( "ps_v" )
                                                                                         , get_item( var( "ps_Data_Ordering" )
                                                                                                   , "EQ" ) )
                                                                                    , block( ret( var( "ps_x" ) ) )
                                                                                    , None )
                                                                               , ite( isa( var( "ps_v" )
                                                                                         , get_item( var( "ps_Data_Ordering" )
                                                                                                   , "GT" ) )
                                                                                    , block( ret( var( "ps_y" ) ) )
                                                                                    , None )
                                                                               , throw( call( var( "Error" )
                                                                                            , binop( "Failed pattern match at purescript_show_python.Data.Ord.pure (line 158, column 3 - line 161, column 12): "
                                                                                                   , BinOp.ADD
                                                                                                   , call( get_attr( ","
                                                                                                                   , "join" )
                                                                                                         , mktuple( get_attr( get_item( var( "ps_v" )
                                                                                                                                      , ".t" )
                                                                                                                            , "__name__" ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_ordArray"
                        , define( None
                                , ["ps_dictOrd"]
                                , block( ret( new( var("ps_Ord")
                                                 , define( None
                                                         , ["ps_$__unused"]
                                                         , block( ret( call( get_item( var( "ps_Data_Eq" )
                                                                                     , "eqArray" )
                                                                           , call( get_item( var( "ps_dictOrd" )
                                                                                           , "Eq0" ) ) ) ) ) )
                                                 , call( define( None
                                                               , []
                                                               , block( assign_star( "ps_toDelta"
                                                                                   , define( None
                                                                                           , [ "ps_x" ]
                                                                                           , block( ret( define( None
                                                                                                               , [ "ps_y" ]
                                                                                                               , block( assign_star( "ps_v"
                                                                                                                                   , call( call( call( var( "ps_compare" )
                                                                                                                                                     , var( "ps_dictOrd" ) )
                                                                                                                                               , var( "ps_x" ) )
                                                                                                                                         , var( "ps_y" ) ) )
                                                                                                                      , ite( isa( var( "ps_v" )
                                                                                                                                , get_item( var( "ps_Data_Ordering" )
                                                                                                                                          , "EQ" ) )
                                                                                                                           , block( ret( metadata( 67
                                                                                                                                                 , 15
                                                                                                                                                 , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ord.purs"
                                                                                                                                                 , 0 ) ) )
                                                                                                                           , None )
                                                                                                                      , ite( isa( var( "ps_v" )
                                                                                                                                , get_item( var( "ps_Data_Ordering" )
                                                                                                                                          , "LT" ) )
                                                                                                                           , block( ret( metadata( 68
                                                                                                                                                 , 15
                                                                                                                                                 , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ord.purs"
                                                                                                                                                 , 1 ) ) )
                                                                                                                           , None )
                                                                                                                      , ite( isa( var( "ps_v" )
                                                                                                                                , get_item( var( "ps_Data_Ordering" )
                                                                                                                                          , "GT" ) )
                                                                                                                           , block( ret( binop( uop( UOp.NEGATIVE
                                                                                                                                                   , metadata( 69
                                                                                                                                                             , 16
                                                                                                                                                             , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ord.purs"
                                                                                                                                                             , 1 ) )
                                                                                                                                              , BinOp.OR
                                                                                                                                              , 0 ) ) )
                                                                                                                           , None )
                                                                                                                      , throw( call( var( "Error" )
                                                                                                                                   , binop( "Failed pattern match at purescript_show_python.Data.Ord.pure (line 65, column 7 - line 68, column 17): "
                                                                                                                                          , BinOp.ADD
                                                                                                                                          , call( get_attr( ","
                                                                                                                                                          , "join" )
                                                                                                                                                , mktuple( get_attr( get_item( var( "ps_v" )
                                                                                                                                                                             , ".t" )
                                                                                                                                                                   , "__name__" ) ) ) ) ) ) ) ) ) ) ) )
                                                                      , ret( define( None
                                                                                   , [ "ps_xs" ]
                                                                                   , block( ret( define( None
                                                                                                       , [ "ps_ys" ]
                                                                                                       , block( ret( call( call( call( var( "ps_compare" )
                                                                                                                                     , var( "ps_ordInt" ) )
                                                                                                                               , metadata( 63
                                                                                                                                         , 31
                                                                                                                                         , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ord.purs"
                                                                                                                                         , 0 ) )
                                                                                                                         , call( call( call( get_item( var( "$foreign" )
                                                                                                                                                     , "ordArrayImpl" )
                                                                                                                                           , var( "ps_toDelta" ) )
                                                                                                                                     , var( "ps_xs" ) )
                                                                                                                               , var( "ps_ys" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_ord1Array"
                        , new( var("ps_Ord1")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Eq")
                                                           , "eq1Array" ) ) ) )
                             , define( None
                                     , ["ps_dictOrd"]
                                     , block( ret( call( var("ps_compare")
                                                       , call( var( "ps_ordArray" )
                                                             , var( "ps_dictOrd" ) ) ) ) ) ) ) )
           , assign_star( "ps_ordRecordCons"
                        , define( None
                                , ["ps_dictOrdRecord"]
                                , block( ret( define( None
                                                    , ["ps_dictCons"]
                                                    , block( ret( define( None
                                                                        , [ "ps_dictIsSymbol" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_dictOrd" ]
                                                                                            , block( ret( new( var( "ps_OrdRecord" )
                                                                                                             , define( None
                                                                                                                     , [ "ps_$__unused" ]
                                                                                                                     , block( ret( call( call( call( call( get_item( var( "ps_Data_Eq" )
                                                                                                                                                                   , "eqRowCons" )
                                                                                                                                                         , call( get_item( var( "ps_dictOrdRecord" )
                                                                                                                                                                         , "EqRecord0" ) ) ) )
                                                                                                                                             , var( "ps_dictIsSymbol" ) )
                                                                                                                                       , call( get_item( var( "ps_dictOrd" )
                                                                                                                                                       , "Eq0" ) ) ) ) ) )
                                                                                                             , define( None
                                                                                                                     , [ "ps_v" ]
                                                                                                                     , block( ret( define( None
                                                                                                                                         , [ "ps_ra" ]
                                                                                                                                         , block( ret( define( None
                                                                                                                                                             , [ "ps_rb" ]
                                                                                                                                                             , block( assign_star( "ps_key"
                                                                                                                                                                                 , call( call( get_item( var( "ps_Data_Symbol" )
                                                                                                                                                                                                       , "reflectSymbol" )
                                                                                                                                                                                             , var( "ps_dictIsSymbol" ) )
                                                                                                                                                                                       , get_attr( get_item( var( "ps_Data_Symbol" )
                                                                                                                                                                                                           , "SProxy" )
                                                                                                                                                                                                 , "value" ) ) )
                                                                                                                                                                    , assign_star( "ps_left"
                                                                                                                                                                                 , call( call( call( var( "ps_compare" )
                                                                                                                                                                                                   , var( "ps_dictOrd" ) )
                                                                                                                                                                                             , call( call( get_item( var( "ps_Record_Unsafe" )
                                                                                                                                                                                                                   , "unsafeGet" )
                                                                                                                                                                                                         , var( "ps_key" ) )
                                                                                                                                                                                                   , var( "ps_ra" ) ) )
                                                                                                                                                                                       , call( call( get_item( var( "ps_Record_Unsafe" )
                                                                                                                                                                                                             , "unsafeGet" )
                                                                                                                                                                                                   , var( "ps_key" ) )
                                                                                                                                                                                             , var( "ps_rb" ) ) ) )
                                                                                                                                                                    , assign_star( "ps_$15"
                                                                                                                                                                                 , call( call( call( get_item( var( "ps_Data_Eq" )
                                                                                                                                                                                                             , "notEq" )
                                                                                                                                                                                                   , get_item( var( "ps_Data_Ordering" )
                                                                                                                                                                                                             , "eqOrdering" ) )
                                                                                                                                                                                             , var( "ps_left" ) )
                                                                                                                                                                                       , get_attr( get_item( var( "ps_Data_Ordering" )
                                                                                                                                                                                                           , "EQ" )
                                                                                                                                                                                                 , "value" ) ) )
                                                                                                                                                                    , ite( var( "ps_$15" )
                                                                                                                                                                         , block( ret( var( "ps_left" ) ) )
                                                                                                                                                                         , None )
                                                                                                                                                                    , ret( call( call( call( call( var( "ps_compareRecord" )
                                                                                                                                                                                                 , var( "ps_dictOrdRecord" ) )
                                                                                                                                                                                           , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                                                                                                                                               , "RLProxy" )
                                                                                                                                                                                                     , "value" ) )
                                                                                                                                                                                     , var( "ps_ra" ) )
                                                                                                                                                                               , var( "ps_rb" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_clamp"
                        , define( None
                                , ["ps_dictOrd"]
                                , block( ret( define( None
                                                    , ["ps_low"]
                                                    , block( ret( define( None
                                                                        , [ "ps_hi" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_x" ]
                                                                                            , block( ret( call( call( call( var( "ps_min" )
                                                                                                                          , var( "ps_dictOrd" ) )
                                                                                                                    , var( "ps_hi" ) )
                                                                                                              , call( call( call( var( "ps_max" )
                                                                                                                                , var( "ps_dictOrd" ) )
                                                                                                                          , var( "ps_low" ) )
                                                                                                                    , var( "ps_x" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_between"
                        , define( None
                                , ["ps_dictOrd"]
                                , block( ret( define( None
                                                    , ["ps_low"]
                                                    , block( ret( define( None
                                                                        , [ "ps_hi" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_x" ]
                                                                                            , block( ite( call( call( call( var( "ps_lessThan" )
                                                                                                                          , var( "ps_dictOrd" ) )
                                                                                                                    , var( "ps_x" ) )
                                                                                                              , var( "ps_low" ) )
                                                                                                        , block( ret( metadata( 197
                                                                                                                              , 15
                                                                                                                              , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ord.purs"
                                                                                                                              , False ) ) )
                                                                                                        , None )
                                                                                                   , ite( call( call( call( var( "ps_greaterThan" )
                                                                                                                          , var( "ps_dictOrd" ) )
                                                                                                                    , var( "ps_x" ) )
                                                                                                              , var( "ps_hi" ) )
                                                                                                        , block( ret( metadata( 198
                                                                                                                              , 14
                                                                                                                              , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ord.purs"
                                                                                                                              , False ) ) )
                                                                                                        , None )
                                                                                                   , ret( metadata( 199
                                                                                                                  , 12
                                                                                                                  , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ord.purs"
                                                                                                                  , True ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_abs"
                        , define( None
                                , ["ps_dictOrd"]
                                , block( ret( define( None
                                                    , ["ps_dictRing"]
                                                    , block( ret( define( None
                                                                        , [ "ps_x" ]
                                                                        , block( assign_star( "ps_$19"
                                                                                            , call( call( call( var( "ps_greaterThanOrEq" )
                                                                                                              , var( "ps_dictOrd" ) )
                                                                                                        , var( "ps_x" ) )
                                                                                                  , call( get_item( var( "ps_Data_Semiring" )
                                                                                                                  , "zero" )
                                                                                                        , call( get_item( var( "ps_dictRing" )
                                                                                                                        , "Semiring0" ) ) ) ) )
                                                                               , ite( var( "ps_$19" )
                                                                                    , block( ret( var( "ps_x" ) ) )
                                                                                    , None )
                                                                               , ret( call( call( get_item( var( "ps_Data_Ring" )
                                                                                                          , "negate" )
                                                                                                , var( "ps_dictRing" ) )
                                                                                          , var( "ps_x" ) ) ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("Ord", var("ps_Ord"))
                           , ("compare", var("ps_compare"))
                           , ("Ord1", var("ps_Ord1"))
                           , ("compare1", var("ps_compare1"))
                           , ("lessThan", var("ps_lessThan"))
                           , ("lessThanOrEq", var("ps_lessThanOrEq"))
                           , ("greaterThan", var("ps_greaterThan"))
                           , ("greaterThanOrEq", var("ps_greaterThanOrEq"))
                           , ("comparing", var("ps_comparing"))
                           , ("min", var("ps_min"))
                           , ("max", var("ps_max"))
                           , ("clamp", var("ps_clamp"))
                           , ("between", var("ps_between"))
                           , ("abs", var("ps_abs"))
                           , ("signum", var("ps_signum"))
                           , ("OrdRecord", var("ps_OrdRecord"))
                           , ("compareRecord", var("ps_compareRecord"))
                           , ("ordBoolean", var("ps_ordBoolean"))
                           , ("ordInt", var("ps_ordInt"))
                           , ("ordNumber", var("ps_ordNumber"))
                           , ("ordString", var("ps_ordString"))
                           , ("ordChar", var("ps_ordChar"))
                           , ("ordUnit", var("ps_ordUnit"))
                           , ("ordVoid", var("ps_ordVoid"))
                           , ("ordArray", var("ps_ordArray"))
                           , ("ordOrdering", var("ps_ordOrdering"))
                           , ("ord1Array", var("ps_ord1Array"))
                           , ("ordRecordNil", var("ps_ordRecordNil"))
                           , ("ordRecordCons", var("ps_ordRecordCons"))
                           , ("ordRecord", var("ps_ordRecord")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Ord.purs", name="purescript_show_python.Data.Ord.pure")
