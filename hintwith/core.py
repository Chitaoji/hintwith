"""
Contains the core of hintwith: hintwith(), hintwithmethod(), etc.

NOTE: this module is private. All functions and objects are available in the main
`hintwith` namespace - use that instead.

"""
from typing import Any, Callable, Literal, TypeVar, overload

from typing_extensions import Concatenate, ParamSpec

P = ParamSpec("P")
Q = ParamSpec("Q")
S = TypeVar("S")
T = TypeVar("T")

__all__ = ["hintwith", "hintwithmethod"]


@overload
def hintwith(
    __func: Callable[P, Any], __is_method: Literal[False] = False
) -> Callable[[Callable[..., T]], Callable[P, T]]:
    ...


@overload
def hintwith(
    __func: Callable[P, Any], __is_method: Literal[True] = True
) -> Callable[[Callable[Concatenate[S, Q], T]], Callable[Concatenate[S, P], T]]:
    ...


def hintwith(__func: Callable, __is_method: bool = False) -> Callable:
    """
    This decorator does literally NOTHING to your function, but can annotate it
    with an existing one's annotations. This means that nothing inside the
    function (including attributes like `__doc__` and `__annotations__`) are
    modified, but the annotations may SEEM to be changed in your IDE's type hints.

    Parameters
    ----------
    __func : Callable[P, T]
        The function whose annotations you want to annotate with.

    Returns
    -------
    Callable[[Callable[..., U]], Callable[P, U]]
        A decorator which does nothing to the function.

    """

    def decorator(a: Any) -> Any:
        return a  # See? We do nothing to your function

    return decorator


@overload
def hintwithmethod(
    __method: Callable[Concatenate[Any, P], Any], __is_method: Literal[False] = False
) -> Callable[[Callable[..., T]], Callable[P, T]]:
    ...


@overload
def hintwithmethod(
    __method: Callable[Concatenate[Any, P], Any], __is_method: Literal[True] = True
) -> Callable[[Callable[Concatenate[S, Q], T]], Callable[Concatenate[S, P], T]]:
    ...


def hintwithmethod(__method: Callable, __is_method: bool = False) -> Callable:
    """
    Behaves like `hintwith()` except that it is designed to annotate your function
    with a method rather than another function.

    Parameters
    ----------
    __method : Callable[Concatenate[S, P], T]
        The method whose annotations you want to copy.

    Returns
    -------
    Callable[[Callable[..., U]], Callable[P, U]]
        A decorator which does nothing to the function.

    """

    def decorator(a: Any) -> Any:
        return a  # See? We do nothing to your function

    return decorator
