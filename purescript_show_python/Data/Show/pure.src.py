from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "$foreign"
                        , call( var('import_module')
                              , "purescript_show_python.ffi.Data.Show" ) )
           , assign_star( "ps_Data_Symbol"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Symbol.pure" ) )
           , assign_star( "ps_Record_Unsafe"
                        , call( var('import_module')
                              , "purescript_show_python.Record.Unsafe.pure" ) )
           , assign_star( "ps_Type_Data_RowList"
                        , call( var('import_module')
                              , "purescript_show_python.Type.Data.RowList.pure" ) )
           , assign_star( "ps_ShowRecordFields"
                        , define( None
                                , ["ps_showRecordFields", ".this"]
                                , block( set_item( var(".this")
                                                 , "showRecordFields"
                                                 , var("ps_showRecordFields") )
                                       , var(".this") ) ) )
           , assign_star( "ps_Show"
                        , define( None
                                , ["ps_show", ".this"]
                                , block( set_item( var(".this")
                                                 , "show"
                                                 , var("ps_show") )
                                       , var(".this") ) ) )
           , assign_star( "ps_showString"
                        , new( var("ps_Show")
                             , get_item(var("$foreign"), "showStringImpl") ) )
           , assign_star( "ps_showRecordFieldsNil"
                        , new( var("ps_ShowRecordFields")
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( define( None
                                                         , ["ps_v1"]
                                                         , block( ret( metadata( 51
                                                                               , 26
                                                                               , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Show.purs"
                                                                               , mktuple(  ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_showRecordFields"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "showRecordFields" ) ) ) ) )
           , assign_star( "ps_showRecord"
                        , define( None
                                , ["ps_dictRowToList"]
                                , block( ret( define( None
                                                    , [ "ps_dictShowRecordFields" ]
                                                    , block( ret( new( var( "ps_Show" )
                                                                     , define( None
                                                                             , [ "ps_record" ]
                                                                             , block( assign_star( "ps_v"
                                                                                                 , call( call( call( var( "ps_showRecordFields" )
                                                                                                                   , var( "ps_dictShowRecordFields" ) )
                                                                                                             , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                                                                 , "RLProxy" )
                                                                                                                       , "value" ) )
                                                                                                       , var( "ps_record" ) ) )
                                                                                    , ite( cmp( call( var( "len" )
                                                                                                    , var( "ps_v" ) )
                                                                                              , Compare.EQ
                                                                                              , 0 )
                                                                                         , block( ret( metadata( 42
                                                                                                               , 11
                                                                                                               , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Show.purs"
                                                                                                               , "{}" ) ) )
                                                                                         , None )
                                                                                    , ret( call( call( get_item( var( "$foreign" )
                                                                                                               , "join" )
                                                                                                     , metadata( 43
                                                                                                               , 20
                                                                                                               , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Show.purs"
                                                                                                               , " " ) )
                                                                                               , metadata( 43
                                                                                                         , 24
                                                                                                         , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Show.purs"
                                                                                                         , mktuple( metadata( 43
                                                                                                                            , 25
                                                                                                                            , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Show.purs"
                                                                                                                            , "{" )
                                                                                                                  , call( call( get_item( var( "$foreign" )
                                                                                                                                        , "join" )
                                                                                                                              , metadata( 43
                                                                                                                                        , 35
                                                                                                                                        , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Show.purs"
                                                                                                                                        , ", " ) )
                                                                                                                        , var( "ps_v" ) )
                                                                                                                  , metadata( 43
                                                                                                                            , 48
                                                                                                                            , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Show.purs"
                                                                                                                            , "}" ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_showNumber"
                        , new( var("ps_Show")
                             , get_item(var("$foreign"), "showNumberImpl") ) )
           , assign_star( "ps_showInt"
                        , new( var("ps_Show")
                             , get_item(var("$foreign"), "showIntImpl") ) )
           , assign_star( "ps_showChar"
                        , new( var("ps_Show")
                             , get_item(var("$foreign"), "showCharImpl") ) )
           , assign_star( "ps_showBoolean"
                        , new( var("ps_Show")
                             , define( None
                                     , ["ps_v"]
                                     , block( ite( var("ps_v")
                                                 , block( ret( metadata( 22
                                                                       , 15
                                                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Show.purs"
                                                                       , "true" ) ) )
                                                 , None )
                                            , ite( uop(UOp.NOT, var("ps_v"))
                                                 , block( ret( metadata( 23
                                                                       , 16
                                                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Show.purs"
                                                                       , "false" ) ) )
                                                 , None )
                                            , throw( call( var("Error")
                                                         , binop( "Failed pattern match at purescript_show_python.Data.Show.pure (line 20, column 1 - line 22, column 23): "
                                                                , BinOp.ADD
                                                                , call( get_attr( ","
                                                                                , "join" )
                                                                      , mktuple( get_attr( get_item( var( "ps_v" )
                                                                                                   , ".t" )
                                                                                         , "__name__" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_show"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "show" ) ) ) ) )
           , assign_star( "ps_showArray"
                        , define( None
                                , ["ps_dictShow"]
                                , block( ret( new( var("ps_Show")
                                                 , call( get_item( var( "$foreign" )
                                                                 , "showArrayImpl" )
                                                       , call( var("ps_show")
                                                             , var( "ps_dictShow" ) ) ) ) ) ) ) )
           , assign_star( "ps_showRecordFieldsCons"
                        , define( None
                                , ["ps_dictIsSymbol"]
                                , block( ret( define( None
                                                    , [ "ps_dictShowRecordFields" ]
                                                    , block( ret( define( None
                                                                        , [ "ps_dictShow" ]
                                                                        , block( ret( new( var( "ps_ShowRecordFields" )
                                                                                         , define( None
                                                                                                 , [ "ps_v" ]
                                                                                                 , block( ret( define( None
                                                                                                                     , [ "ps_record" ]
                                                                                                                     , block( assign_star( "ps_tail"
                                                                                                                                         , call( call( call( var( "ps_showRecordFields" )
                                                                                                                                                           , var( "ps_dictShowRecordFields" ) )
                                                                                                                                                     , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                                                                                                         , "RLProxy" )
                                                                                                                                                               , "value" ) )
                                                                                                                                               , var( "ps_record" ) ) )
                                                                                                                            , assign_star( "ps_key"
                                                                                                                                         , call( call( get_item( var( "ps_Data_Symbol" )
                                                                                                                                                               , "reflectSymbol" )
                                                                                                                                                     , var( "ps_dictIsSymbol" ) )
                                                                                                                                               , get_attr( get_item( var( "ps_Data_Symbol" )
                                                                                                                                                                   , "SProxy" )
                                                                                                                                                         , "value" ) ) )
                                                                                                                            , assign_star( "ps_focus"
                                                                                                                                         , call( call( get_item( var( "ps_Record_Unsafe" )
                                                                                                                                                               , "unsafeGet" )
                                                                                                                                                     , var( "ps_key" ) )
                                                                                                                                               , var( "ps_record" ) ) )
                                                                                                                            , ret( call( call( get_item( var( "$foreign" )
                                                                                                                                                       , "cons" )
                                                                                                                                             , call( call( get_item( var( "$foreign" )
                                                                                                                                                                   , "join" )
                                                                                                                                                         , metadata( 60
                                                                                                                                                                   , 18
                                                                                                                                                                   , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Show.purs"
                                                                                                                                                                   , ": " ) )
                                                                                                                                                   , metadata( 60
                                                                                                                                                             , 23
                                                                                                                                                             , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Show.purs"
                                                                                                                                                             , mktuple( var( "ps_key" )
                                                                                                                                                                      , call( call( var( "ps_show" )
                                                                                                                                                                                  , var( "ps_dictShow" ) )
                                                                                                                                                                            , var( "ps_focus" ) ) ) ) ) )
                                                                                                                                       , var( "ps_tail" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("Show", var("ps_Show"))
                           , ("show", var("ps_show"))
                           , ("ShowRecordFields", var("ps_ShowRecordFields"))
                           , ("showRecordFields", var("ps_showRecordFields"))
                           , ("showBoolean", var("ps_showBoolean"))
                           , ("showInt", var("ps_showInt"))
                           , ("showNumber", var("ps_showNumber"))
                           , ("showChar", var("ps_showChar"))
                           , ("showString", var("ps_showString"))
                           , ("showArray", var("ps_showArray"))
                           , ("showRecord", var("ps_showRecord"))
                           , ( "showRecordFieldsNil"
                             , var("ps_showRecordFieldsNil") )
                           , ( "showRecordFieldsCons"
                             , var("ps_showRecordFieldsCons") ) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Show.purs", name="purescript_show_python.Data.Show.pure")
