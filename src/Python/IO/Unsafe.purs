module Python.IO.Unsafe
    ( show
    , printLn
    , repr
    , assertMsg
    , assert
    )
where

import Prelude

import Effect (Effect)

-- Equal to `str` in Python but wrapped in Effect monad.
foreign import show :: forall a. a -> Effect String

-- Equal to `print` in Python but wrapped in Effect monad.
foreign import printLn :: forall a. a -> Effect Unit

-- Equal to `repr` in Python but wrapped in Effect monad.
foreign import repr :: forall a. a -> Effect String

-- Equal to `assert cond, msg` in Python but wrapped in Effect monad.
foreign import assertMsg :: Boolean -> String -> Effect Unit

-- Equal to `assert cond` in Python but wrapped in Effect monad.
foreign import assert_ :: Boolean -> Effect Unit

-- See assert_
assert :: Boolean -> Effect Unit
assert = assert_
