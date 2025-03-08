

module HybridPyJlPkgExample

export ding, dong, dingnumber

ding() = println("Ding!")
dong() = println("Dong!")

dingnumber = 42

nonexported_func() = println("Non-exported function")

nonexported_number = -999

end
