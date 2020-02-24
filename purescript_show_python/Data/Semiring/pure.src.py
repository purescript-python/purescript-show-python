from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "$foreign"
                        , call( var('import_module')
                              , "purescript_show_python.ffi.Data.Semiring" ) )
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
           , assign_star( "ps_SemiringRecord"
                        , define( None
                                , [ "ps_addRecord"
                                , "ps_mulRecord"
                                , "ps_oneRecord"
                                , "ps_zeroRecord"
                                , ".this" ]
                                , block( set_item( var(".this")
                                                 , "addRecord"
                                                 , var("ps_addRecord") )
                                       , set_item( var(".this")
                                                 , "mulRecord"
                                                 , var("ps_mulRecord") )
                                       , set_item( var(".this")
                                                 , "oneRecord"
                                                 , var("ps_oneRecord") )
                                       , set_item( var(".this")
                                                 , "zeroRecord"
                                                 , var("ps_zeroRecord") )
                                       , var(".this") ) ) )
           , assign_star( "ps_Semiring"
                        , define( None
                                , [ "ps_add"
                                , "ps_mul"
                                , "ps_one"
                                , "ps_zero"
                                , ".this" ]
                                , block( set_item( var(".this")
                                                 , "add"
                                                 , var("ps_add") )
                                       , set_item( var(".this")
                                                 , "mul"
                                                 , var("ps_mul") )
                                       , set_item( var(".this")
                                                 , "one"
                                                 , var("ps_one") )
                                       , set_item( var(".this")
                                                 , "zero"
                                                 , var("ps_zero") )
                                       , var(".this") ) ) )
           , assign_star( "ps_zeroRecord"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "zeroRecord" ) ) ) ) )
           , assign_star( "ps_zero"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "zero" ) ) ) ) )
           , assign_star( "ps_semiringUnit"
                        , new( var("ps_Semiring")
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
                             , get_item(var("ps_Data_Unit"), "unit") ) )
           , assign_star( "ps_semiringRecordNil"
                        , new( var("ps_SemiringRecord")
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( define( None
                                                                             , [ "ps_v2" ]
                                                                             , block( ret( metadata( 89
                                                                                                   , 22
                                                                                                   , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Semiring.purs"
                                                                                                   , record(  ) ) ) ) ) ) ) ) ) ) )
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( define( None
                                                                             , [ "ps_v2" ]
                                                                             , block( ret( metadata( 90
                                                                                                   , 22
                                                                                                   , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Semiring.purs"
                                                                                                   , record(  ) ) ) ) ) ) ) ) ) ) )
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( metadata( 91
                                                                               , 20
                                                                               , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Semiring.purs"
                                                                               , record(  ) ) ) ) ) ) ) )
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( metadata( 92
                                                                               , 20
                                                                               , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Semiring.purs"
                                                                               , record(  ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_semiringNumber"
                        , new( var("ps_Semiring")
                             , get_item(var("$foreign"), "numAdd")
                             , get_item(var("$foreign"), "numMul")
                             , metadata( 55
                                       , 9
                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Semiring.purs"
                                       , 1.0 )
                             , metadata( 53
                                       , 10
                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Semiring.purs"
                                       , 0.0 ) ) )
           , assign_star( "ps_semiringInt"
                        , new( var("ps_Semiring")
                             , get_item(var("$foreign"), "intAdd")
                             , get_item(var("$foreign"), "intMul")
                             , metadata( 49
                                       , 9
                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Semiring.purs"
                                       , 1 )
                             , metadata( 47
                                       , 10
                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Semiring.purs"
                                       , 0 ) ) )
           , assign_star( "ps_oneRecord"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "oneRecord" ) ) ) ) )
           , assign_star( "ps_one"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "one" ) ) ) ) )
           , assign_star( "ps_mulRecord"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "mulRecord" ) ) ) ) )
           , assign_star( "ps_mul"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "mul" ) ) ) ) )
           , assign_star( "ps_addRecord"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "addRecord" ) ) ) ) )
           , assign_star( "ps_semiringRecord"
                        , define( None
                                , ["ps_dictRowToList"]
                                , block( ret( define( None
                                                    , ["ps_dictSemiringRecord"]
                                                    , block( ret( new( var( "ps_Semiring" )
                                                                     , call( call( var( "ps_addRecord" )
                                                                                 , var( "ps_dictSemiringRecord" ) )
                                                                           , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                               , "RLProxy" )
                                                                                     , "value" ) )
                                                                     , call( call( var( "ps_mulRecord" )
                                                                                 , var( "ps_dictSemiringRecord" ) )
                                                                           , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                               , "RLProxy" )
                                                                                     , "value" ) )
                                                                     , call( call( call( var( "ps_oneRecord" )
                                                                                       , var( "ps_dictSemiringRecord" ) )
                                                                                 , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                                     , "RLProxy" )
                                                                                           , "value" ) )
                                                                           , get_attr( get_item( var( "ps_Type_Data_Row" )
                                                                                               , "RProxy" )
                                                                                     , "value" ) )
                                                                     , call( call( call( var( "ps_zeroRecord" )
                                                                                       , var( "ps_dictSemiringRecord" ) )
                                                                                 , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                                     , "RLProxy" )
                                                                                           , "value" ) )
                                                                           , get_attr( get_item( var( "ps_Type_Data_Row" )
                                                                                               , "RProxy" )
                                                                                     , "value" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_add"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "add" ) ) ) ) )
           , assign_star( "ps_semiringFn"
                        , define( None
                                , ["ps_dictSemiring"]
                                , block( ret( new( var("ps_Semiring")
                                                 , define( None
                                                         , ["ps_f"]
                                                         , block( ret( define( None
                                                                             , [ "ps_g" ]
                                                                             , block( ret( define( None
                                                                                                 , [ "ps_x" ]
                                                                                                 , block( ret( call( call( call( var( "ps_add" )
                                                                                                                               , var( "ps_dictSemiring" ) )
                                                                                                                         , call( var( "ps_f" )
                                                                                                                               , var( "ps_x" ) ) )
                                                                                                                   , call( var( "ps_g" )
                                                                                                                         , var( "ps_x" ) ) ) ) ) ) ) ) ) ) ) )
                                                 , define( None
                                                         , ["ps_f"]
                                                         , block( ret( define( None
                                                                             , [ "ps_g" ]
                                                                             , block( ret( define( None
                                                                                                 , [ "ps_x" ]
                                                                                                 , block( ret( call( call( call( var( "ps_mul" )
                                                                                                                               , var( "ps_dictSemiring" ) )
                                                                                                                         , call( var( "ps_f" )
                                                                                                                               , var( "ps_x" ) ) )
                                                                                                                   , call( var( "ps_g" )
                                                                                                                         , var( "ps_x" ) ) ) ) ) ) ) ) ) ) ) )
                                                 , define( None
                                                         , ["ps_v"]
                                                         , block( ret( call( var( "ps_one" )
                                                                           , var( "ps_dictSemiring" ) ) ) ) )
                                                 , define( None
                                                         , ["ps_v"]
                                                         , block( ret( call( var( "ps_zero" )
                                                                           , var( "ps_dictSemiring" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_semiringRecordCons"
                        , define( None
                                , ["ps_dictIsSymbol"]
                                , block( ret( define( None
                                                    , ["ps_dictCons"]
                                                    , block( ret( define( None
                                                                        , [ "ps_dictSemiringRecord" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_dictSemiring" ]
                                                                                            , block( ret( new( var( "ps_SemiringRecord" )
                                                                                                             , define( None
                                                                                                                     , [ "ps_v" ]
                                                                                                                     , block( ret( define( None
                                                                                                                                         , [ "ps_ra" ]
                                                                                                                                         , block( ret( define( None
                                                                                                                                                             , [ "ps_rb" ]
                                                                                                                                                             , block( assign_star( "ps_tail"
                                                                                                                                                                                 , call( call( call( call( var( "ps_addRecord" )
                                                                                                                                                                                                         , var( "ps_dictSemiringRecord" ) )
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
                                                                                                                                                                                     , call( call( call( var( "ps_add" )
                                                                                                                                                                                                       , var( "ps_dictSemiring" ) )
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
                                                                                                                                                                                 , call( call( call( call( var( "ps_mulRecord" )
                                                                                                                                                                                                         , var( "ps_dictSemiringRecord" ) )
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
                                                                                                                                                                                     , call( call( call( var( "ps_mul" )
                                                                                                                                                                                                       , var( "ps_dictSemiring" ) )
                                                                                                                                                                                                 , call( var( "ps_get" )
                                                                                                                                                                                                       , var( "ps_ra" ) ) )
                                                                                                                                                                                           , call( var( "ps_get" )
                                                                                                                                                                                                 , var( "ps_rb" ) ) ) )
                                                                                                                                                                               , var( "ps_tail" ) ) ) ) ) ) ) ) ) ) )
                                                                                                             , define( None
                                                                                                                     , [ "ps_v" ]
                                                                                                                     , block( ret( define( None
                                                                                                                                         , [ "ps_v1" ]
                                                                                                                                         , block( assign_star( "ps_tail"
                                                                                                                                                             , call( call( call( var( "ps_oneRecord" )
                                                                                                                                                                               , var( "ps_dictSemiringRecord" ) )
                                                                                                                                                                         , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                                                                                                                             , "RLProxy" )
                                                                                                                                                                                   , "value" ) )
                                                                                                                                                                   , get_attr( get_item( var( "ps_Type_Data_Row" )
                                                                                                                                                                                       , "RProxy" )
                                                                                                                                                                             , "value" ) ) )
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
                                                                                                                                                                 , call( var( "ps_one" )
                                                                                                                                                                       , var( "ps_dictSemiring" ) ) )
                                                                                                                                                           , var( "ps_tail" ) ) ) ) ) ) ) )
                                                                                                             , define( None
                                                                                                                     , [ "ps_v" ]
                                                                                                                     , block( ret( define( None
                                                                                                                                         , [ "ps_v1" ]
                                                                                                                                         , block( assign_star( "ps_tail"
                                                                                                                                                             , call( call( call( var( "ps_zeroRecord" )
                                                                                                                                                                               , var( "ps_dictSemiringRecord" ) )
                                                                                                                                                                         , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                                                                                                                             , "RLProxy" )
                                                                                                                                                                                   , "value" ) )
                                                                                                                                                                   , get_attr( get_item( var( "ps_Type_Data_Row" )
                                                                                                                                                                                       , "RProxy" )
                                                                                                                                                                             , "value" ) ) )
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
                                                                                                                                                                 , call( var( "ps_zero" )
                                                                                                                                                                       , var( "ps_dictSemiring" ) ) )
                                                                                                                                                           , var( "ps_tail" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("Semiring", var("ps_Semiring"))
                           , ("add", var("ps_add"))
                           , ("zero", var("ps_zero"))
                           , ("mul", var("ps_mul"))
                           , ("one", var("ps_one"))
                           , ("SemiringRecord", var("ps_SemiringRecord"))
                           , ("addRecord", var("ps_addRecord"))
                           , ("mulRecord", var("ps_mulRecord"))
                           , ("oneRecord", var("ps_oneRecord"))
                           , ("zeroRecord", var("ps_zeroRecord"))
                           , ("semiringInt", var("ps_semiringInt"))
                           , ("semiringNumber", var("ps_semiringNumber"))
                           , ("semiringFn", var("ps_semiringFn"))
                           , ("semiringUnit", var("ps_semiringUnit"))
                           , ("semiringRecord", var("ps_semiringRecord"))
                           , ("semiringRecordNil", var("ps_semiringRecordNil"))
                           , ( "semiringRecordCons"
                             , var("ps_semiringRecordCons") ) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Semiring.purs", name="purescript_show_python.Data.Semiring.pure")
