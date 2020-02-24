from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "$foreign"
                        , call( var('import_module')
                              , "purescript_show_python.ffi.Data.Eq" ) )
           , assign_star( "ps_Data_Symbol"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Symbol.pure" ) )
           , assign_star( "ps_Record_Unsafe"
                        , call( var('import_module')
                              , "purescript_show_python.Record.Unsafe.pure" ) )
           , assign_star( "ps_Type_Data_RowList"
                        , call( var('import_module')
                              , "purescript_show_python.Type.Data.RowList.pure" ) )
           , assign_star( "ps_EqRecord"
                        , define( None
                                , ["ps_eqRecord", ".this"]
                                , block( set_item( var(".this")
                                                 , "eqRecord"
                                                 , var("ps_eqRecord") )
                                       , var(".this") ) ) )
           , assign_star( "ps_Eq1"
                        , define( None
                                , ["ps_eq1", ".this"]
                                , block( set_item( var(".this")
                                                 , "eq1"
                                                 , var("ps_eq1") )
                                       , var(".this") ) ) )
           , assign_star( "ps_Eq"
                        , define( None
                                , ["ps_eq", ".this"]
                                , block( set_item( var(".this")
                                                 , "eq"
                                                 , var("ps_eq") )
                                       , var(".this") ) ) )
           , assign_star( "ps_eqVoid"
                        , new( var("ps_Eq")
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( metadata( 60
                                                                               , 12
                                                                               , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Eq.purs"
                                                                               , True ) ) ) ) ) ) ) ) )
           , assign_star( "ps_eqUnit"
                        , new( var("ps_Eq")
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( metadata( 57
                                                                               , 12
                                                                               , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Eq.purs"
                                                                               , True ) ) ) ) ) ) ) ) )
           , assign_star( "ps_eqString"
                        , new( var("ps_Eq")
                             , get_item(var("$foreign"), "eqStringImpl") ) )
           , assign_star( "ps_eqRowNil"
                        , new( var("ps_EqRecord")
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( define( None
                                                                             , [ "ps_v2" ]
                                                                             , block( ret( metadata( 92
                                                                                                   , 20
                                                                                                   , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Eq.purs"
                                                                                                   , True ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_eqRecord"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "eqRecord" ) ) ) ) )
           , assign_star( "ps_eqRec"
                        , define( None
                                , ["ps_dictRowToList"]
                                , block( ret( define( None
                                                    , ["ps_dictEqRecord"]
                                                    , block( ret( new( var( "ps_Eq" )
                                                                     , call( call( var( "ps_eqRecord" )
                                                                                 , var( "ps_dictEqRecord" ) )
                                                                           , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                               , "RLProxy" )
                                                                                     , "value" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_eqNumber"
                        , new( var("ps_Eq")
                             , get_item(var("$foreign"), "eqNumberImpl") ) )
           , assign_star( "ps_eqInt"
                        , new( var("ps_Eq")
                             , get_item(var("$foreign"), "eqIntImpl") ) )
           , assign_star( "ps_eqChar"
                        , new( var("ps_Eq")
                             , get_item(var("$foreign"), "eqCharImpl") ) )
           , assign_star( "ps_eqBoolean"
                        , new( var("ps_Eq")
                             , get_item(var("$foreign"), "eqBooleanImpl") ) )
           , assign_star( "ps_eq1"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "eq1" ) ) ) ) )
           , assign_star( "ps_eq"
                        , define( None
                                , ["ps_dict"]
                                , block(ret(get_item(var("ps_dict"), "eq"))) ) )
           , assign_star( "ps_eqArray"
                        , define( None
                                , ["ps_dictEq"]
                                , block( ret( new( var("ps_Eq")
                                                 , call( get_item( var( "$foreign" )
                                                                 , "eqArrayImpl" )
                                                       , call( var("ps_eq")
                                                             , var( "ps_dictEq" ) ) ) ) ) ) ) )
           , assign_star( "ps_eq1Array"
                        , new( var("ps_Eq1")
                             , define( None
                                     , ["ps_dictEq"]
                                     , block( ret( call( var("ps_eq")
                                                       , call( var("ps_eqArray")
                                                             , var( "ps_dictEq" ) ) ) ) ) ) ) )
           , assign_star( "ps_eqRowCons"
                        , define( None
                                , ["ps_dictEqRecord"]
                                , block( ret( define( None
                                                    , ["ps_dictCons"]
                                                    , block( ret( define( None
                                                                        , [ "ps_dictIsSymbol" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_dictEq" ]
                                                                                            , block( ret( new( var( "ps_EqRecord" )
                                                                                                             , define( None
                                                                                                                     , [ "ps_v" ]
                                                                                                                     , block( ret( define( None
                                                                                                                                         , [ "ps_ra" ]
                                                                                                                                         , block( ret( define( None
                                                                                                                                                             , [ "ps_rb" ]
                                                                                                                                                             , block( assign_star( "ps_tail"
                                                                                                                                                                                 , call( call( call( call( var( "ps_eqRecord" )
                                                                                                                                                                                                         , var( "ps_dictEqRecord" ) )
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
                                                                                                                                                                    , assign_star( "ps_get"
                                                                                                                                                                                 , call( get_item( var( "ps_Record_Unsafe" )
                                                                                                                                                                                                 , "unsafeGet" )
                                                                                                                                                                                       , var( "ps_key" ) ) )
                                                                                                                                                                    , ret( ite( call( call( call( var( "ps_eq" )
                                                                                                                                                                                                , var( "ps_dictEq" ) )
                                                                                                                                                                                          , call( var( "ps_get" )
                                                                                                                                                                                                , var( "ps_ra" ) ) )
                                                                                                                                                                                    , call( var( "ps_get" )
                                                                                                                                                                                          , var( "ps_rb" ) ) )
                                                                                                                                                                              , var( "ps_tail" )
                                                                                                                                                                              , False ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_notEq"
                        , define( None
                                , ["ps_dictEq"]
                                , block( ret( define( None
                                                    , ["ps_x"]
                                                    , block( ret( define( None
                                                                        , [ "ps_y" ]
                                                                        , block( ret( call( call( call( var( "ps_eq" )
                                                                                                      , var( "ps_eqBoolean" ) )
                                                                                                , call( call( call( var( "ps_eq" )
                                                                                                                  , var( "ps_dictEq" ) )
                                                                                                            , var( "ps_x" ) )
                                                                                                      , var( "ps_y" ) ) )
                                                                                          , metadata( 37
                                                                                                    , 25
                                                                                                    , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Eq.purs"
                                                                                                    , False ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_notEq1"
                        , define( None
                                , ["ps_dictEq1"]
                                , block( ret( define( None
                                                    , ["ps_dictEq"]
                                                    , block( ret( define( None
                                                                        , [ "ps_x" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_y" ]
                                                                                            , block( ret( call( call( call( var( "ps_eq" )
                                                                                                                          , var( "ps_eqBoolean" ) )
                                                                                                                    , call( call( call( call( var( "ps_eq1" )
                                                                                                                                            , var( "ps_dictEq1" ) )
                                                                                                                                      , var( "ps_dictEq" ) )
                                                                                                                                , var( "ps_x" ) )
                                                                                                                          , var( "ps_y" ) ) )
                                                                                                              , metadata( 84
                                                                                                                        , 29
                                                                                                                        , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Eq.purs"
                                                                                                                        , False ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("Eq", var("ps_Eq"))
                           , ("eq", var("ps_eq"))
                           , ("notEq", var("ps_notEq"))
                           , ("Eq1", var("ps_Eq1"))
                           , ("eq1", var("ps_eq1"))
                           , ("notEq1", var("ps_notEq1"))
                           , ("EqRecord", var("ps_EqRecord"))
                           , ("eqRecord", var("ps_eqRecord"))
                           , ("eqBoolean", var("ps_eqBoolean"))
                           , ("eqInt", var("ps_eqInt"))
                           , ("eqNumber", var("ps_eqNumber"))
                           , ("eqChar", var("ps_eqChar"))
                           , ("eqString", var("ps_eqString"))
                           , ("eqUnit", var("ps_eqUnit"))
                           , ("eqVoid", var("ps_eqVoid"))
                           , ("eqArray", var("ps_eqArray"))
                           , ("eqRec", var("ps_eqRec"))
                           , ("eq1Array", var("ps_eq1Array"))
                           , ("eqRowNil", var("ps_eqRowNil"))
                           , ("eqRowCons", var("ps_eqRowCons")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Eq.purs", name="purescript_show_python.Data.Eq.pure")
