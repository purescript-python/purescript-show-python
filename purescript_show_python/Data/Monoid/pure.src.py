from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_Data_Boolean"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Boolean.pure" ) )
           , assign_star( "ps_Data_EuclideanRing"
                        , call( var('import_module')
                              , "purescript_show_python.Data.EuclideanRing.pure" ) )
           , assign_star( "ps_Data_Ordering"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Ordering.pure" ) )
           , assign_star( "ps_Data_Semigroup"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Semigroup.pure" ) )
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
           , assign_star( "ps_MonoidRecord"
                        , define( None
                                , [ "ps_SemigroupRecord0"
                                , "ps_memptyRecord"
                                , ".this" ]
                                , block( set_item( var(".this")
                                                 , "SemigroupRecord0"
                                                 , var("ps_SemigroupRecord0") )
                                       , set_item( var(".this")
                                                 , "memptyRecord"
                                                 , var("ps_memptyRecord") )
                                       , var(".this") ) ) )
           , assign_star( "ps_Monoid"
                        , define( None
                                , ["ps_Semigroup0", "ps_mempty", ".this"]
                                , block( set_item( var(".this")
                                                 , "Semigroup0"
                                                 , var("ps_Semigroup0") )
                                       , set_item( var(".this")
                                                 , "mempty"
                                                 , var("ps_mempty") )
                                       , var(".this") ) ) )
           , assign_star( "ps_monoidUnit"
                        , new( var("ps_Monoid")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Data_Semigroup" )
                                                           , "semigroupUnit" ) ) ) )
                             , get_item(var("ps_Data_Unit"), "unit") ) )
           , assign_star( "ps_monoidString"
                        , new( var("ps_Monoid")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Data_Semigroup" )
                                                           , "semigroupString" ) ) ) )
                             , metadata( 45
                                       , 12
                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Monoid.purs"
                                       , "" ) ) )
           , assign_star( "ps_monoidRecordNil"
                        , new( var("ps_MonoidRecord")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Data_Semigroup" )
                                                           , "semigroupRecordNil" ) ) ) )
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( metadata( 84
                                                           , 20
                                                           , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Monoid.purs"
                                                           , record(  ) ) ) ) ) ) )
           , assign_star( "ps_monoidOrdering"
                        , new( var("ps_Monoid")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Data_Ordering" )
                                                           , "semigroupOrdering" ) ) ) )
                             , get_attr( get_item(var("ps_Data_Ordering"), "EQ")
                                       , "value" ) ) )
           , assign_star( "ps_monoidArray"
                        , new( var("ps_Monoid")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var( "ps_Data_Semigroup" )
                                                           , "semigroupArray" ) ) ) )
                             , metadata( 48
                                       , 12
                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Monoid.purs"
                                       , mktuple() ) ) )
           , assign_star( "ps_memptyRecord"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "memptyRecord" ) ) ) ) )
           , assign_star( "ps_monoidRecord"
                        , define( None
                                , ["ps_dictRowToList"]
                                , block( ret( define( None
                                                    , ["ps_dictMonoidRecord"]
                                                    , block( ret( new( var( "ps_Monoid" )
                                                                     , define( None
                                                                             , [ "ps_$__unused" ]
                                                                             , block( ret( call( call( get_item( var( "ps_Data_Semigroup" )
                                                                                                               , "semigroupRecord" ) )
                                                                                               , call( get_item( var( "ps_dictMonoidRecord" )
                                                                                                               , "SemigroupRecord0" ) ) ) ) ) )
                                                                     , call( call( var( "ps_memptyRecord" )
                                                                                 , var( "ps_dictMonoidRecord" ) )
                                                                           , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                               , "RLProxy" )
                                                                                     , "value" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_mempty"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "mempty" ) ) ) ) )
           , assign_star( "ps_monoidFn"
                        , define( None
                                , ["ps_dictMonoid"]
                                , block( ret( new( var("ps_Monoid")
                                                 , define( None
                                                         , ["ps_$__unused"]
                                                         , block( ret( call( get_item( var( "ps_Data_Semigroup" )
                                                                                     , "semigroupFn" )
                                                                           , call( get_item( var( "ps_dictMonoid" )
                                                                                           , "Semigroup0" ) ) ) ) ) )
                                                 , define( None
                                                         , ["ps_v"]
                                                         , block( ret( call( var( "ps_mempty" )
                                                                           , var( "ps_dictMonoid" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_monoidRecordCons"
                        , define( None
                                , ["ps_dictIsSymbol"]
                                , block( ret( define( None
                                                    , ["ps_dictMonoid"]
                                                    , block( ret( define( None
                                                                        , [ "ps_dictCons" ]
                                                                        , block( ret( define( None
                                                                                            , [ "ps_dictMonoidRecord" ]
                                                                                            , block( ret( new( var( "ps_MonoidRecord" )
                                                                                                             , define( None
                                                                                                                     , [ "ps_$__unused" ]
                                                                                                                     , block( ret( call( call( call( call( get_item( var( "ps_Data_Semigroup" )
                                                                                                                                                                   , "semigroupRecordCons" )
                                                                                                                                                         , var( "ps_dictIsSymbol" ) ) )
                                                                                                                                             , call( get_item( var( "ps_dictMonoidRecord" )
                                                                                                                                                             , "SemigroupRecord0" ) ) )
                                                                                                                                       , call( get_item( var( "ps_dictMonoid" )
                                                                                                                                                       , "Semigroup0" ) ) ) ) ) )
                                                                                                             , define( None
                                                                                                                     , [ "ps_v" ]
                                                                                                                     , block( assign_star( "ps_tail"
                                                                                                                                         , call( call( var( "ps_memptyRecord" )
                                                                                                                                                     , var( "ps_dictMonoidRecord" ) )
                                                                                                                                               , get_attr( get_item( var( "ps_Type_Data_RowList" )
                                                                                                                                                                   , "RLProxy" )
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
                                                                                                                                             , call( var( "ps_mempty" )
                                                                                                                                                   , var( "ps_dictMonoid" ) ) )
                                                                                                                                       , var( "ps_tail" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_power"
                        , define( None
                                , ["ps_dictMonoid"]
                                , block( ret( define( None
                                                    , ["ps_x"]
                                                    , block( assign_star( "ps_go"
                                                                        , define( None
                                                                                , [ "ps_p" ]
                                                                                , block( ite( cmp( var( "ps_p" )
                                                                                                 , Compare.LE
                                                                                                 , metadata( 68
                                                                                                           , 12
                                                                                                           , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Monoid.purs"
                                                                                                           , 0 ) )
                                                                                            , block( ret( call( var( "ps_mempty" )
                                                                                                              , var( "ps_dictMonoid" ) ) ) )
                                                                                            , None )
                                                                                       , ite( cmp( var( "ps_p" )
                                                                                                 , Compare.EQ
                                                                                                 , metadata( 69
                                                                                                           , 12
                                                                                                           , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Monoid.purs"
                                                                                                           , 1 ) )
                                                                                            , block( ret( var( "ps_x" ) ) )
                                                                                            , None )
                                                                                       , ite( cmp( call( call( call( get_item( var( "ps_Data_EuclideanRing" )
                                                                                                                             , "mod" )
                                                                                                                   , get_item( var( "ps_Data_EuclideanRing" )
                                                                                                                             , "euclideanRingInt" ) )
                                                                                                             , var( "ps_p" ) )
                                                                                                       , metadata( 70
                                                                                                                 , 15
                                                                                                                 , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Monoid.purs"
                                                                                                                 , 2 ) )
                                                                                                 , Compare.EQ
                                                                                                 , metadata( 70
                                                                                                           , 20
                                                                                                           , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Monoid.purs"
                                                                                                           , 0 ) )
                                                                                            , block( assign_star( "ps_x'"
                                                                                                                , call( var( "ps_go" )
                                                                                                                      , call( call( call( get_item( var( "ps_Data_EuclideanRing" )
                                                                                                                                                  , "div" )
                                                                                                                                        , get_item( var( "ps_Data_EuclideanRing" )
                                                                                                                                                  , "euclideanRingInt" ) )
                                                                                                                                  , var( "ps_p" ) )
                                                                                                                            , metadata( 70
                                                                                                                                      , 41
                                                                                                                                      , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Monoid.purs"
                                                                                                                                      , 2 ) ) ) )
                                                                                                   , ret( call( call( call( get_item( var( "ps_Data_Semigroup" )
                                                                                                                                    , "append" )
                                                                                                                          , call( get_item( var( "ps_dictMonoid" )
                                                                                                                                          , "Semigroup0" ) ) )
                                                                                                                    , var( "ps_x'" ) )
                                                                                                              , var( "ps_x'" ) ) ) )
                                                                                            , None )
                                                                                       , ite( get_item( var( "ps_Data_Boolean" )
                                                                                                      , "otherwise" )
                                                                                            , block( assign_star( "ps_x'"
                                                                                                                , call( var( "ps_go" )
                                                                                                                      , call( call( call( get_item( var( "ps_Data_EuclideanRing" )
                                                                                                                                                  , "div" )
                                                                                                                                        , get_item( var( "ps_Data_EuclideanRing" )
                                                                                                                                                  , "euclideanRingInt" ) )
                                                                                                                                  , var( "ps_p" ) )
                                                                                                                            , metadata( 71
                                                                                                                                      , 36
                                                                                                                                      , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Monoid.purs"
                                                                                                                                      , 2 ) ) ) )
                                                                                                   , ret( call( call( call( get_item( var( "ps_Data_Semigroup" )
                                                                                                                                    , "append" )
                                                                                                                          , call( get_item( var( "ps_dictMonoid" )
                                                                                                                                          , "Semigroup0" ) ) )
                                                                                                                    , var( "ps_x'" ) )
                                                                                                              , call( call( call( get_item( var( "ps_Data_Semigroup" )
                                                                                                                                          , "append" )
                                                                                                                                , call( get_item( var( "ps_dictMonoid" )
                                                                                                                                                , "Semigroup0" ) ) )
                                                                                                                          , var( "ps_x'" ) )
                                                                                                                    , var( "ps_x" ) ) ) ) )
                                                                                            , None )
                                                                                       , throw( call( var( "Error" )
                                                                                                    , binop( "Failed pattern match at purescript_show_python.Data.Monoid.pure (line 65, column 3 - line 65, column 17): "
                                                                                                           , BinOp.ADD
                                                                                                           , call( get_attr( ","
                                                                                                                           , "join" )
                                                                                                                 , mktuple( get_attr( get_item( var( "ps_p" )
                                                                                                                                              , ".t" )
                                                                                                                                    , "__name__" ) ) ) ) ) ) ) ) )
                                                           , ret( var( "ps_go" ) ) ) ) ) ) ) )
           , assign_star( "ps_guard"
                        , define( None
                                , ["ps_dictMonoid"]
                                , block( ret( define( None
                                                    , ["ps_v"]
                                                    , block( ret( define( None
                                                                        , [ "ps_v1" ]
                                                                        , block( ite( var( "ps_v" )
                                                                                    , block( ret( var( "ps_v1" ) ) )
                                                                                    , None )
                                                                               , ite( uop( UOp.NOT
                                                                                         , var( "ps_v" ) )
                                                                                    , block( ret( call( var( "ps_mempty" )
                                                                                                      , var( "ps_dictMonoid" ) ) ) )
                                                                                    , None )
                                                                               , throw( call( var( "Error" )
                                                                                            , binop( "Failed pattern match at purescript_show_python.Data.Monoid.pure (line 73, column 1 - line 73, column 49): "
                                                                                                   , BinOp.ADD
                                                                                                   , call( get_attr( ","
                                                                                                                   , "join" )
                                                                                                         , mktuple( get_attr( get_item( var( "ps_v" )
                                                                                                                                      , ".t" )
                                                                                                                            , "__name__" )
                                                                                                                  , get_attr( get_item( var( "ps_v1" )
                                                                                                                                      , ".t" )
                                                                                                                            , "__name__" ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("Monoid", var("ps_Monoid"))
                           , ("mempty", var("ps_mempty"))
                           , ("power", var("ps_power"))
                           , ("guard", var("ps_guard"))
                           , ("MonoidRecord", var("ps_MonoidRecord"))
                           , ("memptyRecord", var("ps_memptyRecord"))
                           , ("monoidUnit", var("ps_monoidUnit"))
                           , ("monoidOrdering", var("ps_monoidOrdering"))
                           , ("monoidFn", var("ps_monoidFn"))
                           , ("monoidString", var("ps_monoidString"))
                           , ("monoidArray", var("ps_monoidArray"))
                           , ("monoidRecord", var("ps_monoidRecord"))
                           , ("monoidRecordNil", var("ps_monoidRecordNil"))
                           , ( "monoidRecordCons"
                             , var("ps_monoidRecordCons") ) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Monoid.purs", name="purescript_show_python.Data.Monoid.pure")
