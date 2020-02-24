from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_Effect_Class"
                        , call( var('import_module')
                              , "purescript_show_python.Effect.Class.pure" ) )
           , assign_star( "ps_Effect_Console"
                        , call( var('import_module')
                              , "purescript_show_python.Effect.Console.pure" ) )
           , assign_star( "ps_warnShow"
                        , define( None
                                , ["ps_dictMonadEffect"]
                                , block( ret( define( None
                                                    , ["ps_dictShow"]
                                                    , block( assign_star( "ps_$5"
                                                                        , call( get_item( var( "ps_Effect_Class" )
                                                                                        , "liftEffect" )
                                                                              , var( "ps_dictMonadEffect" ) ) )
                                                           , assign_star( "ps_$6"
                                                                        , call( get_item( var( "ps_Effect_Console" )
                                                                                        , "warnShow" )
                                                                              , var( "ps_dictShow" ) ) )
                                                           , ret( define( None
                                                                        , [ "ps_$7" ]
                                                                        , block( ret( call( var( "ps_$5" )
                                                                                          , call( var( "ps_$6" )
                                                                                                , var( "ps_$7" ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_warn"
                        , define( None
                                , ["ps_dictMonadEffect"]
                                , block( assign_star( "ps_$8"
                                                    , call( get_item( var( "ps_Effect_Class" )
                                                                    , "liftEffect" )
                                                          , var( "ps_dictMonadEffect" ) ) )
                                       , ret( define( None
                                                    , ["ps_$9"]
                                                    , block( ret( call( var( "ps_$8" )
                                                                      , call( get_item( var( "ps_Effect_Console" )
                                                                                      , "warn" )
                                                                            , var( "ps_$9" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_timeLog"
                        , define( None
                                , ["ps_dictMonadEffect"]
                                , block( assign_star( "ps_$10"
                                                    , call( get_item( var( "ps_Effect_Class" )
                                                                    , "liftEffect" )
                                                          , var( "ps_dictMonadEffect" ) ) )
                                       , ret( define( None
                                                    , ["ps_$11"]
                                                    , block( ret( call( var( "ps_$10" )
                                                                      , call( get_item( var( "ps_Effect_Console" )
                                                                                      , "timeLog" )
                                                                            , var( "ps_$11" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_timeEnd"
                        , define( None
                                , ["ps_dictMonadEffect"]
                                , block( assign_star( "ps_$12"
                                                    , call( get_item( var( "ps_Effect_Class" )
                                                                    , "liftEffect" )
                                                          , var( "ps_dictMonadEffect" ) ) )
                                       , ret( define( None
                                                    , ["ps_$13"]
                                                    , block( ret( call( var( "ps_$12" )
                                                                      , call( get_item( var( "ps_Effect_Console" )
                                                                                      , "timeEnd" )
                                                                            , var( "ps_$13" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_time"
                        , define( None
                                , ["ps_dictMonadEffect"]
                                , block( assign_star( "ps_$14"
                                                    , call( get_item( var( "ps_Effect_Class" )
                                                                    , "liftEffect" )
                                                          , var( "ps_dictMonadEffect" ) ) )
                                       , ret( define( None
                                                    , ["ps_$15"]
                                                    , block( ret( call( var( "ps_$14" )
                                                                      , call( get_item( var( "ps_Effect_Console" )
                                                                                      , "time" )
                                                                            , var( "ps_$15" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_logShow"
                        , define( None
                                , ["ps_dictMonadEffect"]
                                , block( ret( define( None
                                                    , ["ps_dictShow"]
                                                    , block( assign_star( "ps_$16"
                                                                        , call( get_item( var( "ps_Effect_Class" )
                                                                                        , "liftEffect" )
                                                                              , var( "ps_dictMonadEffect" ) ) )
                                                           , assign_star( "ps_$17"
                                                                        , call( get_item( var( "ps_Effect_Console" )
                                                                                        , "logShow" )
                                                                              , var( "ps_dictShow" ) ) )
                                                           , ret( define( None
                                                                        , [ "ps_$18" ]
                                                                        , block( ret( call( var( "ps_$16" )
                                                                                          , call( var( "ps_$17" )
                                                                                                , var( "ps_$18" ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_log"
                        , define( None
                                , ["ps_dictMonadEffect"]
                                , block( assign_star( "ps_$19"
                                                    , call( get_item( var( "ps_Effect_Class" )
                                                                    , "liftEffect" )
                                                          , var( "ps_dictMonadEffect" ) ) )
                                       , ret( define( None
                                                    , ["ps_$20"]
                                                    , block( ret( call( var( "ps_$19" )
                                                                      , call( get_item( var( "ps_Effect_Console" )
                                                                                      , "log" )
                                                                            , var( "ps_$20" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_infoShow"
                        , define( None
                                , ["ps_dictMonadEffect"]
                                , block( ret( define( None
                                                    , ["ps_dictShow"]
                                                    , block( assign_star( "ps_$21"
                                                                        , call( get_item( var( "ps_Effect_Class" )
                                                                                        , "liftEffect" )
                                                                              , var( "ps_dictMonadEffect" ) ) )
                                                           , assign_star( "ps_$22"
                                                                        , call( get_item( var( "ps_Effect_Console" )
                                                                                        , "infoShow" )
                                                                              , var( "ps_dictShow" ) ) )
                                                           , ret( define( None
                                                                        , [ "ps_$23" ]
                                                                        , block( ret( call( var( "ps_$21" )
                                                                                          , call( var( "ps_$22" )
                                                                                                , var( "ps_$23" ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_info"
                        , define( None
                                , ["ps_dictMonadEffect"]
                                , block( assign_star( "ps_$24"
                                                    , call( get_item( var( "ps_Effect_Class" )
                                                                    , "liftEffect" )
                                                          , var( "ps_dictMonadEffect" ) ) )
                                       , ret( define( None
                                                    , ["ps_$25"]
                                                    , block( ret( call( var( "ps_$24" )
                                                                      , call( get_item( var( "ps_Effect_Console" )
                                                                                      , "info" )
                                                                            , var( "ps_$25" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_errorShow"
                        , define( None
                                , ["ps_dictMonadEffect"]
                                , block( ret( define( None
                                                    , ["ps_dictShow"]
                                                    , block( assign_star( "ps_$26"
                                                                        , call( get_item( var( "ps_Effect_Class" )
                                                                                        , "liftEffect" )
                                                                              , var( "ps_dictMonadEffect" ) ) )
                                                           , assign_star( "ps_$27"
                                                                        , call( get_item( var( "ps_Effect_Console" )
                                                                                        , "errorShow" )
                                                                              , var( "ps_dictShow" ) ) )
                                                           , ret( define( None
                                                                        , [ "ps_$28" ]
                                                                        , block( ret( call( var( "ps_$26" )
                                                                                          , call( var( "ps_$27" )
                                                                                                , var( "ps_$28" ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_error"
                        , define( None
                                , ["ps_dictMonadEffect"]
                                , block( assign_star( "ps_$29"
                                                    , call( get_item( var( "ps_Effect_Class" )
                                                                    , "liftEffect" )
                                                          , var( "ps_dictMonadEffect" ) ) )
                                       , ret( define( None
                                                    , ["ps_$30"]
                                                    , block( ret( call( var( "ps_$29" )
                                                                      , call( get_item( var( "ps_Effect_Console" )
                                                                                      , "error" )
                                                                            , var( "ps_$30" ) ) ) ) ) ) ) ) ) )
           , assign_star( "ps_clear"
                        , define( None
                                , ["ps_dictMonadEffect"]
                                , block( ret( call( call( get_item( var( "ps_Effect_Class" )
                                                                  , "liftEffect" )
                                                        , var( "ps_dictMonadEffect" ) )
                                                  , get_item( var( "ps_Effect_Console" )
                                                            , "clear" ) ) ) ) ) )
           , assign( "exports"
                   , record( ("log", var("ps_log"))
                           , ("logShow", var("ps_logShow"))
                           , ("warn", var("ps_warn"))
                           , ("warnShow", var("ps_warnShow"))
                           , ("error", var("ps_error"))
                           , ("errorShow", var("ps_errorShow"))
                           , ("info", var("ps_info"))
                           , ("infoShow", var("ps_infoShow"))
                           , ("time", var("ps_time"))
                           , ("timeLog", var("ps_timeLog"))
                           , ("timeEnd", var("ps_timeEnd"))
                           , ("clear", var("ps_clear")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\console\\v4.4.0\\src\\Effect\\Class\\Console.purs", name="purescript_show_python.Effect.Class.Console.pure")
