jlpkgname = 'HybridPyJlPkgExample'
jlpkguuid = '046c9583-fc7c-4f0b-bff9-d04135c12147'

import juliapkg
import os
jlpkgpath = os.path.dirname(__file__)
juliapkg.add(jlpkgname, jlpkguuid, dev=True, path=jlpkgpath)
from juliacall import Main as jl
jl.seval('import ' + jlpkgname)
globals()[jlpkgname] = jl.seval(jlpkgname)
for name in jl.seval('string.(names(' + jlpkgname + '))'):
    globals()[name] = jl.seval(jlpkgname + '.' + name)
