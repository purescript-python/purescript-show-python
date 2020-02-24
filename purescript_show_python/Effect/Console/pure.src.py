from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "$foreign"
                        , call( var('import_module')
                              , "purescript_show_python.ffi.Effect.Console" ) )
           , assign_star( "ps_Data_Show"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Show.pure" ) )
           , assign_star( "ps_warnShow"
                        , define( None
                                , ["ps_dictShow"]
                                , block( ret( define( None
                                                    , ["ps_a"]
                                                    , block( ret( call( get_item( var( "$foreign" )
                                                                                , "warn" )
                                                                      , call( call( get_item( var( "ps_Data_Show" )
                                                                                            , "show" )
                                                                                  , var( "ps_dictShow" ) )
                                                                            , var( "ps_a" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_logShow"
                        , define( None
                                , ["ps_dictShow"]
                                , block( ret( define( None
                                                    , ["ps_a"]
                                                    , block( ret( call( get_item( var( "$foreign" )
                                                                                , "log" )
                                                                      , call( call( get_item( var( "ps_Data_Show" )
                                                                                            , "show" )
                                                                                  , var( "ps_dictShow" ) )
                                                                            , var( "ps_a" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_infoShow"
                        , define( None
                                , ["ps_dictShow"]
                                , block( ret( define( None
                                                    , ["ps_a"]
                                                    , block( ret( call( get_item( var( "$foreign" )
                                                                                , "info" )
                                                                      , call( call( get_item( var( "ps_Data_Show" )
                                                                                            , "show" )
                                                                                  , var( "ps_dictShow" ) )
                                                                            , var( "ps_a" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_errorShow"
                        , define( None
                                , ["ps_dictShow"]
                                , block( ret( define( None
                                                    , ["ps_a"]
                                                    , block( ret( call( get_item( var( "$foreign" )
                                                                                , "error" )
                                                                      , call( call( get_item( var( "ps_Data_Show" )
                                                                                            , "show" )
                                                                                  , var( "ps_dictShow" ) )
                                                                            , var( "ps_a" ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("logShow", var("ps_logShow"))
                           , ("warnShow", var("ps_warnShow"))
                           , ("errorShow", var("ps_errorShow"))
                           , ("infoShow", var("ps_infoShow"))
                           , ("log", get_item(var("$foreign"), "log"))
                           , ("warn", get_item(var("$foreign"), "warn"))
                           , ("error", get_item(var("$foreign"), "error"))
                           , ("info", get_item(var("$foreign"), "info"))
                           , ("time", get_item(var("$foreign"), "time"))
                           , ("timeLog", get_item(var("$foreign"), "timeLog"))
                           , ("timeEnd", get_item(var("$foreign"), "timeEnd"))
                           , ("clear", get_item(var("$foreign"), "clear")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\console\\v4.4.0\\src\\Effect\\Console.purs", name="purescript_show_python.Effect.Console.pure")
