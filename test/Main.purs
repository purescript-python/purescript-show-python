module Test.Main where

import Prelude

import Effect (Effect)

import Python.IO.Unsafe as Unsafe

data A = A1 Boolean Boolean
newtype N = N Int

newtype Box a = Box a

main :: Effect Unit
main = do
  Unsafe.printLn {a: 1}
  
  Unsafe.printLn $ A1 true false
  Unsafe.printLn N
  Unsafe.printLn $ N 1

  x <- Unsafe.show (N 1)
  y <- Unsafe.show 1
  Unsafe.assert $ x == y

  x <- Unsafe.repr (N 1)
  y <- Unsafe.repr 1
  Unsafe.assert $ x == y  

  x <- Unsafe.repr (Box 1)
  y <- Unsafe.repr 1
  Unsafe.assert $ x == y  
