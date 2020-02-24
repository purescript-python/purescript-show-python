{ name = "show-python"
, dependencies = [ "effect", "prelude" ]
, packages = ./packages.dhall
, sources = [ "src/**/*.purs", "test/**/*.purs" ]
, backend = "pspy"
, license = "MIT"
, repository = "https://github.com/thautwarm/purescript-show-python.git"
}
