from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "$foreign"
                        , call( var('import_module')
                              , "purescript_show_python.ffi.Data.Bounded" ) )
           , assign_star( "ps_Data_Ord"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Ord.pure" ) )
           , assign_star( "ps_Data_Ordering"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Ordering.pure" ) )
           , assign_star( "ps_Data_Unit"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Unit.pure" ) )
           , assign_star( "ps_Bounded"
                        , define( None
                                , ["ps_Ord0", "ps_bottom", "ps_top", ".this"]
                                , block( set_item( var(".this")
                                                 , "Ord0"
                                                 , var("ps_Ord0") )
                                       , set_item( var(".this")
                                                 , "bottom"
                                                 , var("ps_bottom") )
                                       , set_item( var(".this")
                                                 , "top"
                                                 , var("ps_top") )
                                       , var(".this") ) ) )
           , assign_star( "ps_top"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "top" ) ) ) ) )
           , assign_star( "ps_boundedUnit"
                        , new( var("ps_Bounded")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Ord")
                                                           , "ordUnit" ) ) ) )
                             , get_item(var("ps_Data_Unit"), "unit")
                             , get_item(var("ps_Data_Unit"), "unit") ) )
           , assign_star( "ps_boundedOrdering"
                        , new( var("ps_Bounded")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Ord")
                                                           , "ordOrdering" ) ) ) )
                             , get_attr( get_item(var("ps_Data_Ordering"), "LT")
                                       , "value" )
                             , get_attr( get_item(var("ps_Data_Ordering"), "GT")
                                       , "value" ) ) )
           , assign_star( "ps_boundedNumber"
                        , new( var("ps_Bounded")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Ord")
                                                           , "ordNumber" ) ) ) )
                             , get_item(var("$foreign"), "bottomNumber")
                             , get_item(var("$foreign"), "topNumber") ) )
           , assign_star( "ps_boundedInt"
                        , new( var("ps_Bounded")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Ord")
                                                           , "ordInt" ) ) ) )
                             , get_item(var("$foreign"), "bottomInt")
                             , get_item(var("$foreign"), "topInt") ) )
           , assign_star( "ps_boundedChar"
                        , new( var("ps_Bounded")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Ord")
                                                           , "ordChar" ) ) ) )
                             , get_item(var("$foreign"), "bottomChar")
                             , get_item(var("$foreign"), "topChar") ) )
           , assign_star( "ps_boundedBoolean"
                        , new( var("ps_Bounded")
                             , define( None
                                     , ["ps_$__unused"]
                                     , block( ret( get_item( var("ps_Data_Ord")
                                                           , "ordBoolean" ) ) ) )
                             , metadata( 24
                                       , 12
                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Bounded.purs"
                                       , False )
                             , metadata( 23
                                       , 9
                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Bounded.purs"
                                       , True ) ) )
           , assign_star( "ps_bottom"
                        , define( None
                                , ["ps_dict"]
                                , block( ret( get_item( var("ps_dict")
                                                      , "bottom" ) ) ) ) )
           , assign( "exports"
                   , record( ("Bounded", var("ps_Bounded"))
                           , ("bottom", var("ps_bottom"))
                           , ("top", var("ps_top"))
                           , ("boundedBoolean", var("ps_boundedBoolean"))
                           , ("boundedInt", var("ps_boundedInt"))
                           , ("boundedChar", var("ps_boundedChar"))
                           , ("boundedOrdering", var("ps_boundedOrdering"))
                           , ("boundedUnit", var("ps_boundedUnit"))
                           , ("boundedNumber", var("ps_boundedNumber")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Bounded.purs", name="purescript_show_python.Data.Bounded.pure")
