from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_Field"
                        , define( None
                                , [ "ps_DivisionRing1"
                                , "ps_EuclideanRing0"
                                , ".this" ]
                                , block( set_item( var(".this")
                                                 , "DivisionRing1"
                                                 , var("ps_DivisionRing1") )
                                       , set_item( var(".this")
                                                 , "EuclideanRing0"
                                                 , var("ps_EuclideanRing0") )
                                       , var(".this") ) ) )
           , assign_star( "ps_field"
                        , define( None
                                , ["ps_dictEuclideanRing"]
                                , block( ret( define( None
                                                    , ["ps_dictDivisionRing"]
                                                    , block( ret( new( var( "ps_Field" )
                                                                     , define( None
                                                                             , [ "ps_$__unused" ]
                                                                             , block( ret( var( "ps_dictDivisionRing" ) ) ) )
                                                                     , define( None
                                                                             , [ "ps_$__unused" ]
                                                                             , block( ret( var( "ps_dictEuclideanRing" ) ) ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("Field", var("ps_Field"))
                           , ("field", var("ps_field")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\purescript-show-python\\.spago\\prelude\\v4.1.1\\src\\Data\\Field.purs", name="purescript_show_python.Data.Field.pure")
