from __future__ import annotations

__all__ = ["NVR", "NEVR", "NVRA", "NEVRA"]

from collections.abc import Mapping
from typing import NoReturn

from attr import asdict, field, frozen
from attr.validators import ge

from ._exceptions import MalformedCoordinates


def _malformed_coordinates(
    offender: str, type_: str, initiating_exception: Exception | None = None
) -> NoReturn:
    raise MalformedCoordinates(
        f"Malformed {type_} {offender}"
    ) from initiating_exception


@frozen(kw_only=True)
class NVR:
    """A class representing build/package name-version-release coordinates.

    This class supports iteration, allowing tuple-unpacking-like behavior in
    assignment expressions e.g.

    ```python
    nvr = NVR.from_string("curl-7.76.1-26.el9")
    name, version, release = nvr
    print(f"{name=} {version=} {release=}")
    # name=curl version=7.76.1 release=26.el9
    ```

    """

    name: str
    """Name."""
    version: str
    """Version."""
    release: str
    """Release."""

    @classmethod
    def from_string(cls, nvr: str) -> NVR:
        try:
            n, v, r = nvr.rsplit("-", 2)
        except ValueError as ve:
            # Expected case: ValueError raised if there are not enough items
            # to unpack in to all of `n`, `v`, and `r`
            _malformed_coordinates(nvr, cls.__name__, initiating_exception=ve)
        return cls(name=n, version=v, release=r)

    @classmethod
    def from_string_or_none(cls, coordinate: str | None) -> NVR | None:
        if coordinate is None:
            return None
        return cls.from_string(coordinate)

    def __str__(self) -> str:
        return f"{self.name}-{self.version}-{self.release}"

    def __iter__(self):
        return iter((self.name, self.version, self.release))

    def to_dict(self) -> Mapping[str, str]:
        return asdict(self)


@frozen(kw_only=True)
class NEVR(NVR):
    """A class representing build/package name-epoch:version-release coordinates.

    This class supports iteration, allowing tuple-unpacking-like behavior in
    assignment expressions e.g.

    ```python
    nevr = NEVR.from_string("curl-1:7.76.1-26.el9")
    name, epoch, version, release = nevr
    print(f"{name=} {epoch=} {version=} {release=}")
    # name=curl epoch=1 version=7.76.1 release=26.el9
    ```
    """

    epoch: int = field(default=0, validator=ge(0))
    """Epoch."""

    @classmethod
    def from_string(cls, nevr: str) -> NEVR:
        try:
            n, ev, r = nevr.rsplit("-", 2)
        except ValueError as ve:
            # Expected case: ValueError raised if there are not enough items
            # to unpack in to all of `n`, `v`, and `r`
            _malformed_coordinates(nevr, cls.__name__, initiating_exception=ve)
        # not wrapped in try/except because split here will result in at least a one-item
        # list, meaning worst case `rest` will be an empty list
        *rest, v = ev.split(":", 1)
        e: int = int(rest[0]) if rest else 0
        return cls(name=n, epoch=e, version=v, release=r)

    def __str__(self) -> str:
        epoch_string = f"{self.epoch}:" if self.epoch else ""
        return f"{self.name}-{epoch_string}{self.version}-{self.release}"

    def __iter__(self):
        return iter((self.name, self.epoch, self.version, self.release))


@frozen(kw_only=True)
class NVRA(NVR):
    """A class representing build/package name-version-release.architecture coordinates.

    This class supports iteration, allowing tuple-unpacking-like behavior in
    assignment expressions e.g.

    ```python
    nvra = NVRA.from_string("curl-7.76.1-26.el9.aarch64")
    name, version, release, arch = nvra
    print(f"{name=} {version=} {release=} {arch=}")
    # name=curl version=7.76.1 release=26.el9 arch=aarch64
    ```
    """

    arch: str
    """Architecture."""

    @classmethod
    def from_string(cls, nvra: str) -> NVRA:
        try:
            n, v, ra = nvra.rsplit("-", 2)
            r, a = ra.rsplit(".", 1)
        except ValueError as ve:
            # Expected case: ValueError raised if there are not enough items
            # to unpack in to all of `n`, `v`, and `r`
            _malformed_coordinates(nvra, cls.__name__, initiating_exception=ve)
        return cls(name=n, version=v, release=r, arch=a)

    def __str__(self) -> str:
        return f"{self.name}-{self.version}-{self.release}.{self.arch}"

    def __iter__(self):
        return iter((self.name, self.version, self.release, self.arch))

    @property
    def architecture(self):
        """An alias of `arch` for those who prefer the long-form name."""
        return self.arch


@frozen(kw_only=True)
class NEVRA(NVR):
    """A class representing build/package name-epoch:version-release.architecture coordinates.

    This class supports iteration, allowing tuple-unpacking-like behavior in
    assignment expressions e.g.

    ```python
    nevra = NEVRA.from_string("curl-1:7.76.1-26.el9.aarch64")
    name, epoch, version, release, arch = nevra
    print(f"{name=} {epoch=} {version=} {release=} {arch=}")
    # name=curl epoch=1 version=7.76.1 release=26.el9 arch=aarch64
    ```
    """

    arch: str
    """Architecture."""
    epoch: int = field(default=0, validator=ge(0))
    """Epoch."""

    @classmethod
    def from_string(cls, nevra: str) -> NEVRA:
        try:
            n, ev, ra = nevra.rsplit("-", 2)
            r, a = ra.rsplit(".", 1)
        except ValueError as ve:
            # Expected case: ValueError raised if there are not enough items
            # to unpack in to all of `n`, `v`, and `r`
            _malformed_coordinates(nevra, cls.__name__, initiating_exception=ve)
        # not wrapped in try/except because split here will result in at least a one-item
        # list, meaning worst case `rest` will be an empty list
        *rest, v = ev.split(":", 1)
        e: int = int(rest[0]) if rest else 0
        return cls(name=n, epoch=e, version=v, release=r, arch=a)

    def __str__(self) -> str:
        epoch_string = f"{self.epoch}:" if self.epoch else ""
        return f"{self.name}-{epoch_string}{self.version}-{self.release}.{self.arch}"

    def __iter__(self):
        return iter((self.name, self.epoch, self.version, self.release, self.arch))

    @property
    def architecture(self):
        """An alias of `arch` for those who prefer the long-form name."""
        return self.arch
