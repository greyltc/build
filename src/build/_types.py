from __future__ import annotations

import os
import typing


__all__ = ['ConfigSettings', 'Distribution', 'StrPath', 'SubprocessRunner']

ConfigSettings = typing.Mapping[str, typing.Union[str, typing.Sequence[str]]]
Distribution = typing.Literal['sdist', 'wheel', 'editable']

StrPath = typing.Union[str, os.PathLike[str]]

if typing.TYPE_CHECKING:
    from pyproject_hooks import SubprocessRunner
else:
    SubprocessRunner = typing.Callable[
        [typing.Sequence[str], typing.Optional[str], typing.Optional[typing.Mapping[str, str]]], None
    ]
