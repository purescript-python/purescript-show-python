from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "$foreign"
                        , call( var('import_module')
                              , "purescript_show_python.ffi.Data.Semigroup" ) )
           , assign_star( "ps_Data_Symbol"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Symbol.pure" ) )
           , assign_star( "ps_Data_Unit"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Unit.pure" ) )
           , assign_star( "ps_Data_Void"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Void.pure" ) )
           , assign_star( "ps_Record_Unsafe"
                        , call( var('import_module')
                              , "purescript_show_python.Record.Unsafe.pure" ) )
           , assign_star( "ps_Type_Data_RowList"
                        , call( var('import_module')
                              , "purescript_show_python.Type.Data.RowList.pure" ) )
           , assign_star( "ps_SemigroupRecord"
                        , define( None
                                , ["ps_appendRecord", ".this"]
                                , block( set_item( var(".this")
                                                 , "appendRecord"
                                                 , var("ps_appendRecord") )
                                       , var(".this") ) ) )
           , assign_star( "ps_Semigroup"
                        , define( None
                                , ["ps_append", ".this"]
                                , block( set_item( var(".this")
                                                 , "append"
                                                 , var("ps_append") )
                                       , var(".this") ) ) )
           , assign_star( "ps_semigroupVoid"
                        , new( var("ps_Semigroup")
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( get_item( var("ps_Data_Void")
                                                           , "absurd" ) ) ) ) ) )
           , assign_star( "ps_semigroupUnit"
                        , new( var("ps_Semigroup")
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( get_item( var( "ps_Data_Unit" )
                                                                               , "unit" ) ) ) ) ) ) ) ) )
           , assign_star( "ps_semigroupString"
                        , new( var("ps_Semigroup")
                             , get_item(var("$foreign"), "concatString") ) )
           , assign_star( "ps_semigroupRecordNil"
                        , new( var("ps_SemigroupRecord")
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( define( None
                                                                             , [ "ps_v2" ]
                                                                             , block( ret( metadata( 55
                                                                                                   , 24
                                                                                                   , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Semigroup.purs"
                                                                                                   , record(  ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_semigroupArray"
                        , new( var("ps_Semigroup")
                             , get_item(var("$foreign"), "concatArray") ) )
           , assign_star( "ps_appendRecord"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "appendRecord" ) ) ) ) )
           , assign_star( "ps_semigroupRecord"
                        , define( None
                                , ["ps_dictRowToList"]
                                , block( ret( define( None
                                                    , ["ps_dictSemigroupRecord"]
                                                    , block( ret( new( var( "ps_Semigroup" )
                                                                     , call( call( var( "ps_appendRecord" )
                                                                                 , var( "ps_dictSemigroupRecord" ) )
                                                                           , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                               , "RLProxy" )
                                                                                     , "value" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_append"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "append" ) ) ) ) )
           , assign_star( "ps_semigroupFn"
                        , define( None
                                , ["ps_dictSemigroup"]
                                , block( ret( new( var("ps_Semigroup")
                                                 , define( None
                                                         , ["ps_f"]
                                                         , block( ret( define( None
                                                                             , [ "ps_g" ]
                                                                             , block( ret( define( None
                                                                                                 , [ "ps_x" ]
                                                                                                 , block( ret( call( call( call( var( "ps_append" )
                                                                                                                               , var( "ps_dictSemigroup" ) )
                                                                                                                         , call( var( "ps_f" )
                                                                                                                               , var( "ps_x" ) ) )
                                                                                                                   , call( var( "ps_g" )
                                                                                                                         , var( "ps_x" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_semigroupRecordCons"
                        , define( None
                                , ["ps_dictIsSymbol"]
                                , block( ret( define( None
                                                    , ["ps_dictCons"]
                                                    , block( ret( define( None
                                                                        , [ "ps_dictSemigroupRecord" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_dictSemigroup" ]
                                                                                            , block( ret( new( var( "ps_SemigroupRecord" )
                                                                                                             , define( None
                                                                                                                     , [ "ps_v" ]
                                                                                                                     , block( ret( define( None
                                                                                                                                         , [ "ps_ra" ]
                                                                                                                                         , block( ret( define( None
                                                                                                                                                             , [ "ps_rb" ]
                                                                                                                                                             , block( assign_star( "ps_tail"
                                                                                                                                                                                 , call( call( call( call( var( "ps_appendRecord" )
                                                                                                                                                                                                         , var( "ps_dictSemigroupRecord" ) )
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
                                                                                                                                                                                     , call( call( call( var( "ps_append" )
                                                                                                                                                                                                       , var( "ps_dictSemigroup" ) )
                                                                                                                                                                                                 , call( var( "ps_get" )
                                                                                                                                                                                                       , var( "ps_ra" ) ) )
                                                                                                                                                                                           , call( var( "ps_get" )
                                                                                                                                                                                                 , var( "ps_rb" ) ) ) )
                                                                                                                                                                               , var( "ps_tail" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("Semigroup", var("ps_Semigroup"))
                           , ("append", var("ps_append"))
                           , ("SemigroupRecord", var("ps_SemigroupRecord"))
                           , ("appendRecord", var("ps_appendRecord"))
                           , ("semigroupString", var("ps_semigroupString"))
                           , ("semigroupUnit", var("ps_semigroupUnit"))
                           , ("semigroupVoid", var("ps_semigroupVoid"))
                           , ("semigroupFn", var("ps_semigroupFn"))
                           , ("semigroupArray", var("ps_semigroupArray"))
                           , ("semigroupRecord", var("ps_semigroupRecord"))
                           , ( "semigroupRecordNil"
                             , var("ps_semigroupRecordNil") )
                           , ( "semigroupRecordCons"
                             , var("ps_semigroupRecordCons") ) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Semigroup.purs", name="purescript_show_python.Data.Semigroup.pure")
