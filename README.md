# HybridPyJlPkgExample.jl / hybridpyjlpkgexample

Example of a hybrid Python-Julia package, based on Julia code with a Python wrapper done with JuliaCall.

In Julia:

```julia	
import Pkg
Pkg.add(url="https://github.com/cdsousa/HybridPyJlPkgExample.jl.git")

import HybridPyJlPkgExample
HybridPyJlPkgExample.ding()
```

In Python:

```bash
pip install git+https://github.com/cdsousa/HybridPyJlPkgExample.jl.git
```
```python
import hybridpyjlpkgexample
hybridpyjlpkgexample.ding()
```
