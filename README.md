# purescript-show-python

This is a library for accessing Python internal IO operations in PureScript.

Currently only work for PureScript-Python backend.

The generated Python package `purescript_show_python` can also be used in the Python side.

```purescript
import Prelude
import Python.IO.Unsafe as Unsafe

newtype Box a = Box a

ops :: Effect Unit
ops = do
    Unsafe.printLn {a: 1} -- {"a": 1}
    Unsafe.printLn [1, 2] -- (1, 2)
    Unsafe.printLn $ Unsafe.repr "1" -- '1'
    Unsafe.printLn $ Unsafe.show "1" -- 1
    x <- Unsafe.show 1
    y <- Unsafe.show $ Box 1
    Unsafe.assert $ x == y
```