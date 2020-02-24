from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_Data_Show"
                        , call( var('import_module')
                              , "purescript_show_python.Data.Show.pure" ) )
           , assign_star( "ps_Void"
                        , define(None, ["ps_x"], block(ret(var("ps_x")))) )
           , assign_star( "ps_absurd"
                        , define( None
                                , ["ps_a"]
                                , block( assign_star( "ps_spin"
                                                    , define( None
                                                            , ["ps_$copy_v"]
                                                            , block( assign_star( "ps_$tco_result"
                                                                                , None )
                                                                   , define( "ps_$tco_loop"
                                                                           , [ "ps_v" ]
                                                                           , block( assign( "ps_$copy_v"
                                                                                          , var( "ps_v" ) )
                                                                                  , ret(None) ) )
                                                                   , loop( uop( UOp.NOT
                                                                              , False )
                                                                         , block( assign( "ps_$tco_result"
                                                                                        , call( var( "ps_$tco_loop" )
                                                                                              , var( "ps_$copy_v" ) ) ) ) )
                                                                   , ret( var( "ps_$tco_result" ) ) ) ) )
                                       , ret( call( var("ps_spin")
                                                  , var("ps_a") ) ) ) ) )
           , assign_star( "ps_showVoid"
                        , new( get_item(var("ps_Data_Show"), "Show")
                             , var("ps_absurd") ) )
           , assign( "exports"
                   , record( ("absurd", var("ps_absurd"))
                           , ("showVoid", var("ps_showVoid")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Void.purs", name="purescript_show_python.Data.Void.pure")
