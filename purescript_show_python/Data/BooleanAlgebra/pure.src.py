from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_Data_HeytingAlgebra"
                        , call( var('import_module')
                              , "purescript_show_python.Data.HeytingAlgebra.pure" ) )
           , assign_star( "ps_BooleanAlgebraRecord"
                        , define( None
                                , ["ps_HeytingAlgebraRecord0", ".this"]
                                , block( set_item( var(".this")
                                                 , "HeytingAlgebraRecord0"
                                                 , var( "ps_HeytingAlgebraRecord0" ) )
                                       , var(".this") ) ) )
           , assign_star( "ps_BooleanAlgebra"
                        , define( None
                                , ["ps_HeytingAlgebra0", ".this"]
                                , block( set_item( var(".this")
                                                 , "HeytingAlgebra0"
                                                 , var("ps_HeytingAlgebra0") )
                                       , var(".this") ) ) )
           , assign_star( "ps_booleanAlgebraUnit"
                        , new( var("ps_BooleanAlgebra")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Data_HeytingAlgebra" )
                                                           , "heytingAlgebraUnit" ) ) ) ) ) )
           , assign_star( "ps_booleanAlgebraRecordNil"
                        , new( var("ps_BooleanAlgebraRecord")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Data_HeytingAlgebra" )
                                                           , "heytingAlgebraRecordNil" ) ) ) ) ) )
           , assign_star( "ps_booleanAlgebraRecordCons"
                        , define( None
                                , ["ps_dictIsSymbol"]
                                , block( ret( define( None
                                                    , ["ps_dictCons"]
                                                    , block( ret( define( None
                                                                        , [ "ps_dictBooleanAlgebraRecord" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_dictBooleanAlgebra" ]
                                                                                            , block( ret( new( var( "ps_BooleanAlgebraRecord" )
                                                                                                             , define( None
                                                                                                                     , [ "ps_$__unused" ]
                                                                                                                     , block( ret( call( call( call( call( get_item( var( "ps_Data_HeytingAlgebra" )
                                                                                                                                                                   , "heytingAlgebraRecordCons" )
                                                                                                                                                         , var( "ps_dictIsSymbol" ) ) )
                                                                                                                                             , call( get_item( var( "ps_dictBooleanAlgebraRecord" )
                                                                                                                                                             , "HeytingAlgebraRecord0" ) ) )
                                                                                                                                       , call( get_item( var( "ps_dictBooleanAlgebra" )
                                                                                                                                                       , "HeytingAlgebra0" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_booleanAlgebraRecord"
                        , define( None
                                , ["ps_dictRowToList"]
                                , block( ret( define( None
                                                    , [ "ps_dictBooleanAlgebraRecord" ]
                                                    , block( ret( new( var( "ps_BooleanAlgebra" )
                                                                     , define( None
                                                                             , [ "ps_$__unused" ]
                                                                             , block( ret( call( call( get_item( var( "ps_Data_HeytingAlgebra" )
                                                                                                               , "heytingAlgebraRecord" ) )
                                                                                               , call( get_item( var( "ps_dictBooleanAlgebraRecord" )
                                                                                                               , "HeytingAlgebraRecord0" ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_booleanAlgebraFn"
                        , define( None
                                , ["ps_dictBooleanAlgebra"]
                                , block( ret( new( var("ps_BooleanAlgebra")
                                                 , define( None
                                                         , ["ps_$__unused"]
                                                         , block( ret( call( get_item( var( "ps_Data_HeytingAlgebra" )
                                                                                     , "heytingAlgebraFunction" )
                                                                           , call( get_item( var( "ps_dictBooleanAlgebra" )
                                                                                           , "HeytingAlgebra0" ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_booleanAlgebraBoolean"
                        , new( var("ps_BooleanAlgebra")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Data_HeytingAlgebra" )
                                                           , "heytingAlgebraBoolean" ) ) ) ) ) )
           , assign( "exports"
                   , record( ("BooleanAlgebra", var("ps_BooleanAlgebra"))
                           , ( "BooleanAlgebraRecord"
                             , var("ps_BooleanAlgebraRecord") )
                           , ( "booleanAlgebraBoolean"
                             , var("ps_booleanAlgebraBoolean") )
                           , ( "booleanAlgebraUnit"
                             , var("ps_booleanAlgebraUnit") )
                           , ("booleanAlgebraFn", var("ps_booleanAlgebraFn"))
                           , ( "booleanAlgebraRecord"
                             , var("ps_booleanAlgebraRecord") )
                           , ( "booleanAlgebraRecordNil"
                             , var("ps_booleanAlgebraRecordNil") )
                           , ( "booleanAlgebraRecordCons"
                             , var("ps_booleanAlgebraRecordCons") ) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\BooleanAlgebra.purs", name="purescript_show_python.Data.BooleanAlgebra.pure")
