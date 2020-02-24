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

foreign import show :: forall a. a -> Effect String

foreign import printLn :: forall a. a -> Effect Unit

foreign import repr :: forall a. a -> Effect String

foreign import assertMsg :: Boolean -> String -> Effect Unit

foreign import assert_ :: Boolean -> Effect Unit

assert :: Boolean -> Effect Unit
assert = assert_
