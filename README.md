# hints
Provides more typing tools for python.

## Installation

```sh
$ pip install hints
```

## Usage

Use `hintwith()` to annotate your function with the other one's annotations:

```py
>>> from hints import hintwith
>>> def a(x: int, y: int, z: int = 0) -> int:
...     """Sums x, y and z."""
...     return x + y + z
... 
>>> @hintwith(a)
... def b(*args, **kwargs) -> float:
...     return float(a(*args, **kwargs))
... 
```

Also, there is `hintwithmethod()` to annotate your function with a method rather than a function.

## See Also
### Github repository
* https://github.com/Chitaoji/hints/

### PyPI project
* https://pypi.org/project/hints/

## License
This project falls under the BSD 3-Clause License.

### v0.0.0
* Initial release.