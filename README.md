# hintwith
Hints your function with an existing one.

## Installation

```sh
$ pip install hintwith
```

## Usage

Use `hintwith()` to hint a function with another function:

```py
>>> from hintwith import hintwith
>>> def a(x: int, y: int, z: int = 0) -> int:
...     """Sums x, y and z."""
...     return x + y + z
... 
>>> @hintwith(a)
... def b(*args, **kwargs) -> float:
...     return float(a(*args, **kwargs))
... 
```

Also, there is `hintwithmethod()` to hint the function with a method rather than a direct callable.

## See Also
### Github repository
* https://github.com/Chitaoji/hintwith/

### PyPI project
* https://pypi.org/project/hintwith/

## License
This project falls under the BSD 3-Clause License.

## History
### v0.1.2
* Updated comments.

### v0.1.1
* New optional parameter for `hintwith()` and `hintwithmethod()`:
  * `__is_method` : determines whether the function to get hinted is a method.

### v0.1.0
* Initial release.
