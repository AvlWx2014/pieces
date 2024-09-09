"""Extensions to the `pieces` API for use with `pydantic.BaseModel` types.

These extensions require `pydantic` and, by extensions, `pydantic_core`. Developers can
install `pieces[pydantic]` to enable Pydantic extensions without depending on Pydantic as
a top-level dependency for their project.
"""

from __future__ import annotations

try:
    from pydantic import BaseModel, GetCoreSchemaHandler
except ImportError as ie:
    raise ImportError(
        "Please install pieces[pydantic] to enable pydantic extensions."
    ) from ie

try:
    from pydantic_core import CoreSchema
except ImportError as ie:
    raise ImportError(
        "Please install pieces[pydantic] to enable pydantic extensions."
    ) from ie

from pydantic_core.core_schema import (
    chain_schema,
    is_instance_schema,
    json_or_python_schema,
    no_info_plain_validator_function,
    str_schema,
    to_string_ser_schema,
    union_schema,
)

from ..nvr import NEVR, NEVRA, NVR, NVRA


class NevrSchema:
    """Use with `pydantic.BaseModel` types for NEVR-type fields.

    This type implements some Pydantic dunders to extend the NEVR type for Pydantic
    de/serialization.

    Thanks to the maintainers of the `semver` Python project for figuring out this recipe [1].

    See Also:
        [1]: https://python-semver.readthedocs.io/en/latest/advanced/combine-pydantic-and-semver.html
    """

    @classmethod
    def __get_pydantic_core_schema__(
        cls, _: type[BaseModel], __: GetCoreSchemaHandler
    ) -> CoreSchema:
        schema = chain_schema(
            [str_schema(), no_info_plain_validator_function(NEVR.from_string)]
        )
        return json_or_python_schema(
            json_schema=schema,
            python_schema=union_schema([is_instance_schema(NEVR), schema]),
            serialization=to_string_ser_schema(),
        )


class NevraSchema:
    """Use with `pydantic.BaseModel` types for NEVRA-type fields.

    This type implements some Pydantic dunders to extend the NEVRA type for Pydantic
    de/serialization.

    Thanks to the maintainers of the `semver` Python project for figuring out this recipe [1].

    See Also:
        [1]: https://python-semver.readthedocs.io/en/latest/advanced/combine-pydantic-and-semver.html
    """

    @classmethod
    def __get_pydantic_core_schema__(
        cls, _: type[BaseModel], __: GetCoreSchemaHandler
    ) -> CoreSchema:
        schema = chain_schema(
            [str_schema(), no_info_plain_validator_function(NEVRA.from_string)]
        )
        return json_or_python_schema(
            json_schema=schema,
            python_schema=union_schema([is_instance_schema(NEVRA), schema]),
            serialization=to_string_ser_schema(),
        )


class NvrSchema:
    """Use with `pydantic.BaseModel` types for NVR-type fields.

    This type implements some Pydantic dunders to extend the NVR type for Pydantic
    de/serialization.

    Thanks to the maintainers of the `semver` Python project for figuring out this recipe [1].

    See Also:
        [1]: https://python-semver.readthedocs.io/en/latest/advanced/combine-pydantic-and-semver.html
    """

    @classmethod
    def __get_pydantic_core_schema__(
        cls, _: type[BaseModel], __: GetCoreSchemaHandler
    ) -> CoreSchema:
        schema = chain_schema(
            [str_schema(), no_info_plain_validator_function(NVR.from_string)]
        )
        return json_or_python_schema(
            json_schema=schema,
            python_schema=union_schema([is_instance_schema(NVR), schema]),
            serialization=to_string_ser_schema(),
        )


class NvraSchema:
    """Use with `pydantic.BaseModel` types for NVRA-type fields.

    This type implements some Pydantic dunders to extend the NVRA type for Pydantic
    de/serialization.

    Thanks to the maintainers of the `semver` Python project for figuring out this recipe [1].

    See Also:
        [1]: https://python-semver.readthedocs.io/en/latest/advanced/combine-pydantic-and-semver.html
    """

    @classmethod
    def __get_pydantic_core_schema__(
        cls, _: type[BaseModel], __: GetCoreSchemaHandler
    ) -> CoreSchema:
        schema = chain_schema(
            [str_schema(), no_info_plain_validator_function(NVRA.from_string)]
        )
        return json_or_python_schema(
            json_schema=schema,
            python_schema=union_schema([is_instance_schema(NVRA), schema]),
            serialization=to_string_ser_schema(),
        )
