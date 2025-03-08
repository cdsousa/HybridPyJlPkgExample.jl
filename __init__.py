jlpkgname = 'HybridPyJlPkgExample'
from juliacall import Main as jl
jl.seval('import ' + jlpkgname)
globals()[jlpkgname] = jl.seval(jlpkgname)
for _name in jl.seval('string.(names(' + jlpkgname + '))'):
    globals()[_name] = jl.seval(jlpkgname + '.' + _name)
