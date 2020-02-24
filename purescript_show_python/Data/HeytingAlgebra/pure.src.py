from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "$foreign"
                        , call( var('import_module')
                              , "purescript_show_python.ffi.Data.HeytingAlgebra" ) )
           , assign_star( "ps_Data_Symbol"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Symbol.pure" ) )
           , assign_star( "ps_Data_Unit"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Unit.pure" ) )
           , assign_star( "ps_Record_Unsafe"
                        , call( var('import_module')
                              , "purescript_show_python.Record.Unsafe.pure" ) )
           , assign_star( "ps_Type_Data_Row"
                        , call( var('import_module')
                              , "purescript_show_python.Type.Data.Row.pure" ) )
           , assign_star( "ps_Type_Data_RowList"
                        , call( var('import_module')
                              , "purescript_show_python.Type.Data.RowList.pure" ) )
           , assign_star( "ps_HeytingAlgebraRecord"
                        , define( None
                                , [ "ps_conjRecord"
                                , "ps_disjRecord"
                                , "ps_ffRecord"
                                , "ps_impliesRecord"
                                , "ps_notRecord"
                                , "ps_ttRecord"
                                , ".this" ]
                                , block( set_item( var(".this")
                                                 , "conjRecord"
                                                 , var("ps_conjRecord") )
                                       , set_item( var(".this")
                                                 , "disjRecord"
                                                 , var("ps_disjRecord") )
                                       , set_item( var(".this")
                                                 , "ffRecord"
                                                 , var("ps_ffRecord") )
                                       , set_item( var(".this")
                                                 , "impliesRecord"
                                                 , var("ps_impliesRecord") )
                                       , set_item( var(".this")
                                                 , "notRecord"
                                                 , var("ps_notRecord") )
                                       , set_item( var(".this")
                                                 , "ttRecord"
                                                 , var("ps_ttRecord") )
                                       , var(".this") ) ) )
           , assign_star( "ps_HeytingAlgebra"
                        , define( None
                                , [ "ps_conj"
                                , "ps_disj"
                                , "ps_ff"
                                , "ps_implies"
                                , "ps_not"
                                , "ps_tt"
                                , ".this" ]
                                , block( set_item( var(".this")
                                                 , "conj"
                                                 , var("ps_conj") )
                                       , set_item( var(".this")
                                                 , "disj"
                                                 , var("ps_disj") )
                                       , set_item( var(".this")
                                                 , "ff"
                                                 , var("ps_ff") )
                                       , set_item( var(".this")
                                                 , "implies"
                                                 , var("ps_implies") )
                                       , set_item( var(".this")
                                                 , "not"
                                                 , var("ps_not") )
                                       , set_item( var(".this")
                                                 , "tt"
                                                 , var("ps_tt") )
                                       , var(".this") ) ) )
           , assign_star( "ps_ttRecord"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "ttRecord" ) ) ) ) )
           , assign_star( "ps_tt"
                        , define( None
                                , ["ps_dict"]
                                , block(ret(get_item(var("ps_dict"), "tt"))) ) )
           , assign_star( "ps_notRecord"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "notRecord" ) ) ) ) )
           , assign_star( "ps_not"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "not" ) ) ) ) )
           , assign_star( "ps_impliesRecord"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "impliesRecord" ) ) ) ) )
           , assign_star( "ps_implies"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "implies" ) ) ) ) )
           , assign_star( "ps_heytingAlgebraUnit"
                        , new( var("ps_HeytingAlgebra")
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( get_item( var( "ps_Data_Unit" )
                                                                               , "unit" ) ) ) ) ) ) )
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( get_item( var( "ps_Data_Unit" )
                                                                               , "unit" ) ) ) ) ) ) )
                             , get_item(var("ps_Data_Unit"), "unit")
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( get_item( var( "ps_Data_Unit" )
                                                                               , "unit" ) ) ) ) ) ) )
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( get_item( var("ps_Data_Unit")
                                                           , "unit" ) ) ) )
                             , get_item(var("ps_Data_Unit"), "unit") ) )
           , assign_star( "ps_heytingAlgebraRecordNil"
                        , new( var("ps_HeytingAlgebraRecord")
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( define( None
                                                                             , [ "ps_v2" ]
                                                                             , block( ret( metadata( 98
                                                                                                   , 22
                                                                                                   , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\HeytingAlgebra.purs"
                                                                                                   , record(  ) ) ) ) ) ) ) ) ) ) )
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( define( None
                                                                             , [ "ps_v2" ]
                                                                             , block( ret( metadata( 99
                                                                                                   , 22
                                                                                                   , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\HeytingAlgebra.purs"
                                                                                                   , record(  ) ) ) ) ) ) ) ) ) ) )
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( metadata( 100
                                                                               , 18
                                                                               , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\HeytingAlgebra.purs"
                                                                               , record(  ) ) ) ) ) ) ) )
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( define( None
                                                                             , [ "ps_v2" ]
                                                                             , block( ret( metadata( 101
                                                                                                   , 25
                                                                                                   , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\HeytingAlgebra.purs"
                                                                                                   , record(  ) ) ) ) ) ) ) ) ) ) )
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( metadata( 102
                                                                               , 19
                                                                               , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\HeytingAlgebra.purs"
                                                                               , record(  ) ) ) ) ) ) ) )
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( metadata( 103
                                                                               , 18
                                                                               , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\HeytingAlgebra.purs"
                                                                               , record(  ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_ffRecord"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "ffRecord" ) ) ) ) )
           , assign_star( "ps_ff"
                        , define( None
                                , ["ps_dict"]
                                , block(ret(get_item(var("ps_dict"), "ff"))) ) )
           , assign_star( "ps_disjRecord"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "disjRecord" ) ) ) ) )
           , assign_star( "ps_disj"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "disj" ) ) ) ) )
           , assign_star( "ps_heytingAlgebraBoolean"
                        , new( var("ps_HeytingAlgebra")
                             , get_item(var("$foreign"), "boolConj")
                             , get_item(var("$foreign"), "boolDisj")
                             , metadata( 52
                                       , 8
                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\HeytingAlgebra.purs"
                                       , False )
                             , define( None
                                     , ["ps_a"]
                                     , block( ret( define( None
                                                         , ["ps_b"]
                                                         , block( ret( call( call( call( var( "ps_disj" )
                                                                                       , var( "ps_heytingAlgebraBoolean" ) )
                                                                                 , call( call( var( "ps_not" )
                                                                                             , var( "ps_heytingAlgebraBoolean" ) )
                                                                                       , var( "ps_a" ) ) )
                                                                           , var( "ps_b" ) ) ) ) ) ) ) )
                             , get_item(var("$foreign"), "boolNot")
                             , metadata( 53
                                       , 8
                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\HeytingAlgebra.purs"
                                       , True ) ) )
           , assign_star( "ps_conjRecord"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "conjRecord" ) ) ) ) )
           , assign_star( "ps_heytingAlgebraRecord"
                        , define( None
                                , ["ps_dictRowToList"]
                                , block( ret( define( None
                                                    , [ "ps_dictHeytingAlgebraRecord" ]
                                                    , block( ret( new( var( "ps_HeytingAlgebra" )
                                                                     , call( call( var( "ps_conjRecord" )
                                                                                 , var( "ps_dictHeytingAlgebraRecord" ) )
                                                                           , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                               , "RLProxy" )
                                                                                     , "value" ) )
                                                                     , call( call( var( "ps_disjRecord" )
                                                                                 , var( "ps_dictHeytingAlgebraRecord" ) )
                                                                           , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                               , "RLProxy" )
                                                                                     , "value" ) )
                                                                     , call( call( call( var( "ps_ffRecord" )
                                                                                       , var( "ps_dictHeytingAlgebraRecord" ) )
                                                                                 , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                                     , "RLProxy" )
                                                                                           , "value" ) )
                                                                           , get_attr( get_item( var( "ps_Type_Data_Row" )
                                                                                               , "RProxy" )
                                                                                     , "value" ) )
                                                                     , call( call( var( "ps_impliesRecord" )
                                                                                 , var( "ps_dictHeytingAlgebraRecord" ) )
                                                                           , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                               , "RLProxy" )
                                                                                     , "value" ) )
                                                                     , call( call( var( "ps_notRecord" )
                                                                                 , var( "ps_dictHeytingAlgebraRecord" ) )
                                                                           , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                               , "RLProxy" )
                                                                                     , "value" ) )
                                                                     , call( call( call( var( "ps_ttRecord" )
                                                                                       , var( "ps_dictHeytingAlgebraRecord" ) )
                                                                                 , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                                     , "RLProxy" )
                                                                                           , "value" ) )
                                                                           , get_attr( get_item( var( "ps_Type_Data_Row" )
                                                                                               , "RProxy" )
                                                                                     , "value" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_conj"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "conj" ) ) ) ) )
           , assign_star( "ps_heytingAlgebraFunction"
                        , define( None
                                , ["ps_dictHeytingAlgebra"]
                                , block( ret( new( var("ps_HeytingAlgebra")
                                                 , define( None
                                                         , ["ps_f"]
                                                         , block( ret( define( None
                                                                             , [ "ps_g" ]
                                                                             , block( ret( define( None
                                                                                                 , [ "ps_a" ]
                                                                                                 , block( ret( call( call( call( var( "ps_conj" )
                                                                                                                               , var( "ps_dictHeytingAlgebra" ) )
                                                                                                                         , call( var( "ps_f" )
                                                                                                                               , var( "ps_a" ) ) )
                                                                                                                   , call( var( "ps_g" )
                                                                                                                         , var( "ps_a" ) ) ) ) ) ) ) ) ) ) ) )
                                                 , define( None
                                                         , ["ps_f"]
                                                         , block( ret( define( None
                                                                             , [ "ps_g" ]
                                                                             , block( ret( define( None
                                                                                                 , [ "ps_a" ]
                                                                                                 , block( ret( call( call( call( var( "ps_disj" )
                                                                                                                               , var( "ps_dictHeytingAlgebra" ) )
                                                                                                                         , call( var( "ps_f" )
                                                                                                                               , var( "ps_a" ) ) )
                                                                                                                   , call( var( "ps_g" )
                                                                                                                         , var( "ps_a" ) ) ) ) ) ) ) ) ) ) ) )
                                                 , define( None
                                                         , ["ps_v"]
                                                         , block( ret( call( var( "ps_ff" )
                                                                           , var( "ps_dictHeytingAlgebra" ) ) ) ) )
                                                 , define( None
                                                         , ["ps_f"]
                                                         , block( ret( define( None
                                                                             , [ "ps_g" ]
                                                                             , block( ret( define( None
                                                                                                 , [ "ps_a" ]
                                                                                                 , block( ret( call( call( call( var( "ps_implies" )
                                                                                                                               , var( "ps_dictHeytingAlgebra" ) )
                                                                                                                         , call( var( "ps_f" )
                                                                                                                               , var( "ps_a" ) ) )
                                                                                                                   , call( var( "ps_g" )
                                                                                                                         , var( "ps_a" ) ) ) ) ) ) ) ) ) ) ) )
                                                 , define( None
                                                         , ["ps_f"]
                                                         , block( ret( define( None
                                                                             , [ "ps_a" ]
                                                                             , block( ret( call( call( var( "ps_not" )
                                                                                                     , var( "ps_dictHeytingAlgebra" ) )
                                                                                               , call( var( "ps_f" )
                                                                                                     , var( "ps_a" ) ) ) ) ) ) ) ) )
                                                 , define( None
                                                         , ["ps_v"]
                                                         , block( ret( call( var( "ps_tt" )
                                                                           , var( "ps_dictHeytingAlgebra" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_heytingAlgebraRecordCons"
                        , define( None
                                , ["ps_dictIsSymbol"]
                                , block( ret( define( None
                                                    , ["ps_dictCons"]
                                                    , block( ret( define( None
                                                                        , [ "ps_dictHeytingAlgebraRecord" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_dictHeytingAlgebra" ]
                                                                                            , block( ret( new( var( "ps_HeytingAlgebraRecord" )
                                                                                                             , define( None
                                                                                                                     , [ "ps_v" ]
                                                                                                                     , block( ret( define( None
                                                                                                                                         , [ "ps_ra" ]
                                                                                                                                         , block( ret( define( None
                                                                                                                                                             , [ "ps_rb" ]
                                                                                                                                                             , block( assign_star( "ps_tail"
                                                                                                                                                                                 , call( call( call( call( var( "ps_conjRecord" )
                                                                                                                                                                                                         , var( "ps_dictHeytingAlgebraRecord" ) )
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
                                                                                                                                                                                     , call( call( call( var( "ps_conj" )
                                                                                                                                                                                                       , var( "ps_dictHeytingAlgebra" ) )
                                                                                                                                                                                                 , call( var( "ps_get" )
                                                                                                                                                                                                       , var( "ps_ra" ) ) )
                                                                                                                                                                                           , call( var( "ps_get" )
                                                                                                                                                                                                 , var( "ps_rb" ) ) ) )
                                                                                                                                                                               , var( "ps_tail" ) ) ) ) ) ) ) ) ) ) )
                                                                                                             , define( None
                                                                                                                     , [ "ps_v" ]
                                                                                                                     , block( ret( define( None
                                                                                                                                         , [ "ps_ra" ]
                                                                                                                                         , block( ret( define( None
                                                                                                                                                             , [ "ps_rb" ]
                                                                                                                                                             , block( assign_star( "ps_tail"
                                                                                                                                                                                 , call( call( call( call( var( "ps_disjRecord" )
                                                                                                                                                                                                         , var( "ps_dictHeytingAlgebraRecord" ) )
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
                                                                                                                                                                                     , call( call( call( var( "ps_disj" )
                                                                                                                                                                                                       , var( "ps_dictHeytingAlgebra" ) )
                                                                                                                                                                                                 , call( var( "ps_get" )
                                                                                                                                                                                                       , var( "ps_ra" ) ) )
                                                                                                                                                                                           , call( var( "ps_get" )
                                                                                                                                                                                                 , var( "ps_rb" ) ) ) )
                                                                                                                                                                               , var( "ps_tail" ) ) ) ) ) ) ) ) ) ) )
                                                                                                             , define( None
                                                                                                                     , [ "ps_v" ]
                                                                                                                     , block( ret( define( None
                                                                                                                                         , [ "ps_row" ]
                                                                                                                                         , block( assign_star( "ps_tail"
                                                                                                                                                             , call( call( call( var( "ps_ffRecord" )
                                                                                                                                                                               , var( "ps_dictHeytingAlgebraRecord" ) )
                                                                                                                                                                         , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                                                                                                                             , "RLProxy" )
                                                                                                                                                                                   , "value" ) )
                                                                                                                                                                   , var( "ps_row" ) ) )
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
                                                                                                                                                , ret( call( call( var( "ps_insert" )
                                                                                                                                                                 , call( var( "ps_ff" )
                                                                                                                                                                       , var( "ps_dictHeytingAlgebra" ) ) )
                                                                                                                                                           , var( "ps_tail" ) ) ) ) ) ) ) )
                                                                                                             , define( None
                                                                                                                     , [ "ps_v" ]
                                                                                                                     , block( ret( define( None
                                                                                                                                         , [ "ps_ra" ]
                                                                                                                                         , block( ret( define( None
                                                                                                                                                             , [ "ps_rb" ]
                                                                                                                                                             , block( assign_star( "ps_tail"
                                                                                                                                                                                 , call( call( call( call( var( "ps_impliesRecord" )
                                                                                                                                                                                                         , var( "ps_dictHeytingAlgebraRecord" ) )
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
                                                                                                                                                                                     , call( call( call( var( "ps_implies" )
                                                                                                                                                                                                       , var( "ps_dictHeytingAlgebra" ) )
                                                                                                                                                                                                 , call( var( "ps_get" )
                                                                                                                                                                                                       , var( "ps_ra" ) ) )
                                                                                                                                                                                           , call( var( "ps_get" )
                                                                                                                                                                                                 , var( "ps_rb" ) ) ) )
                                                                                                                                                                               , var( "ps_tail" ) ) ) ) ) ) ) ) ) ) )
                                                                                                             , define( None
                                                                                                                     , [ "ps_v" ]
                                                                                                                     , block( ret( define( None
                                                                                                                                         , [ "ps_row" ]
                                                                                                                                         , block( assign_star( "ps_tail"
                                                                                                                                                             , call( call( call( var( "ps_notRecord" )
                                                                                                                                                                               , var( "ps_dictHeytingAlgebraRecord" ) )
                                                                                                                                                                         , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                                                                                                                             , "RLProxy" )
                                                                                                                                                                                   , "value" ) )
                                                                                                                                                                   , var( "ps_row" ) ) )
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
                                                                                                                                                                 , call( call( var( "ps_not" )
                                                                                                                                                                             , var( "ps_dictHeytingAlgebra" ) )
                                                                                                                                                                       , call( var( "ps_get" )
                                                                                                                                                                             , var( "ps_row" ) ) ) )
                                                                                                                                                           , var( "ps_tail" ) ) ) ) ) ) ) )
                                                                                                             , define( None
                                                                                                                     , [ "ps_v" ]
                                                                                                                     , block( ret( define( None
                                                                                                                                         , [ "ps_row" ]
                                                                                                                                         , block( assign_star( "ps_tail"
                                                                                                                                                             , call( call( call( var( "ps_ttRecord" )
                                                                                                                                                                               , var( "ps_dictHeytingAlgebraRecord" ) )
                                                                                                                                                                         , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                                                                                                                             , "RLProxy" )
                                                                                                                                                                                   , "value" ) )
                                                                                                                                                                   , var( "ps_row" ) ) )
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
                                                                                                                                                , ret( call( call( var( "ps_insert" )
                                                                                                                                                                 , call( var( "ps_tt" )
                                                                                                                                                                       , var( "ps_dictHeytingAlgebra" ) ) )
                                                                                                                                                           , var( "ps_tail" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("HeytingAlgebra", var("ps_HeytingAlgebra"))
                           , ("tt", var("ps_tt"))
                           , ("ff", var("ps_ff"))
                           , ("implies", var("ps_implies"))
                           , ("conj", var("ps_conj"))
                           , ("disj", var("ps_disj"))
                           , ("not", var("ps_not"))
                           , ( "HeytingAlgebraRecord"
                             , var("ps_HeytingAlgebraRecord") )
                           , ("ffRecord", var("ps_ffRecord"))
                           , ("ttRecord", var("ps_ttRecord"))
                           , ("impliesRecord", var("ps_impliesRecord"))
                           , ("conjRecord", var("ps_conjRecord"))
                           , ("disjRecord", var("ps_disjRecord"))
                           , ("notRecord", var("ps_notRecord"))
                           , ( "heytingAlgebraBoolean"
                             , var("ps_heytingAlgebraBoolean") )
                           , ( "heytingAlgebraUnit"
                             , var("ps_heytingAlgebraUnit") )
                           , ( "heytingAlgebraFunction"
                             , var("ps_heytingAlgebraFunction") )
                           , ( "heytingAlgebraRecord"
                             , var("ps_heytingAlgebraRecord") )
                           , ( "heytingAlgebraRecordNil"
                             , var("ps_heytingAlgebraRecordNil") )
                           , ( "heytingAlgebraRecordCons"
                             , var("ps_heytingAlgebraRecordCons") ) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\HeytingAlgebra.purs", name="purescript_show_python.Data.HeytingAlgebra.pure")
