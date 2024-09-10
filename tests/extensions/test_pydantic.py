from pydantic import BaseModel

from pieces import NEVR, NEVRA, NVR, NVRA
from pieces.extensions.pydantic import NevraSchema, NevrSchema, NvraSchema, NvrSchema


class ModelWithNEVR(BaseModel):
    nevr: NevrSchema


# Ignore: ruff N802
# Reason: These test cases are named to reflect the type that they are testing,
#   which is why they use CamelCase.
def test_NevrSchema_validation_from_string():  # noqa: N802
    expected = ModelWithNEVR(
        nevr=NEVR(name="test", epoch=1, version="1.0.0", release="1.fc40")
    )
    actual = ModelWithNEVR.model_validate({"nevr": "test-1:1.0.0-1.fc40"})
    assert actual == expected


# Ignore: ruff N802
# Reason: These test cases are named to reflect the type that they are testing,
#   which is why they use CamelCase.
def test_NevrSchema_validation_from_json():  # noqa: N802
    expected = ModelWithNEVR(
        nevr=NEVR(name="test", epoch=1, version="1.0.0", release="1.fc40")
    )
    actual = ModelWithNEVR.model_validate_json('{"nevr":"test-1:1.0.0-1.fc40"}')
    assert actual == expected


# Ignore: ruff N802
# Reason: These test cases are named to reflect the type that they are testing,
#   which is why they use CamelCase.
def test_NevrSchema_serialization_to_json():  # noqa: N802
    expected = '{"nevr":"test-1:1.0.0-1.fc40"}'
    actual = ModelWithNEVR(
        nevr=NEVR(name="test", epoch=1, version="1.0.0", release="1.fc40")
    ).model_dump_json()
    assert actual == expected


class ModelWithNEVRA(BaseModel):
    nevra: NevraSchema


# Ignore: ruff N802
# Reason: These test cases are named to reflect the type that they are testing,
#   which is why they use CamelCase.
def test_NevraSchema_validation_from_string():  # noqa: N802
    expected = ModelWithNEVRA(
        nevra=NEVRA(
            name="test", epoch=1, version="1.0.0", release="1.fc40", arch="aarch64"
        )
    )
    actual = ModelWithNEVRA.model_validate({"nevra": "test-1:1.0.0-1.fc40.aarch64"})
    assert actual == expected


# Ignore: ruff N802
# Reason: These test cases are named to reflect the type that they are testing,
#   which is why they use CamelCase.
def test_NevraSchema_validation_from_json():  # noqa: N802
    expected = ModelWithNEVRA(
        nevra=NEVRA(
            name="test", epoch=1, version="1.0.0", release="1.fc40", arch="aarch64"
        )
    )
    actual = ModelWithNEVRA.model_validate_json(
        '{"nevra":"test-1:1.0.0-1.fc40.aarch64"}'
    )
    assert actual == expected


# Ignore: ruff N802
# Reason: These test cases are named to reflect the type that they are testing,
#   which is why they use CamelCase.
def test_NevraSchema_serialization_to_json():  # noqa: N802
    expected = '{"nevra":"test-1:1.0.0-1.fc40.aarch64"}'
    actual = ModelWithNEVRA(
        nevra=NEVRA(
            name="test", epoch=1, version="1.0.0", release="1.fc40", arch="aarch64"
        )
    ).model_dump_json()
    assert actual == expected


class ModelWithNVR(BaseModel):
    nvr: NvrSchema


# Ignore: ruff N802
# Reason: These test cases are named to reflect the type that they are testing,
#   which is why they use CamelCase.
def test_NvrSchema_validation_from_string():  # noqa: N802
    expected = ModelWithNVR(nvr=NVR(name="test", version="1.0.0", release="1.fc40"))
    actual = ModelWithNVR.model_validate({"nvr": "test-1.0.0-1.fc40"})
    assert actual == expected


# Ignore: ruff N802
# Reason: These test cases are named to reflect the type that they are testing,
#   which is why they use CamelCase.
def test_NvrSchema_validation_from_json():  # noqa: N802
    expected = ModelWithNVR(nvr=NVR(name="test", version="1.0.0", release="1.fc40"))
    actual = ModelWithNVR.model_validate_json('{"nvr":"test-1.0.0-1.fc40"}')
    assert actual == expected


# Ignore: ruff N802
# Reason: These test cases are named to reflect the type that they are testing,
#   which is why they use CamelCase.
def test_NvrSchema_serialization_to_json():  # noqa: N802
    expected = '{"nvr":"test-1.0.0-1.fc40"}'
    actual = ModelWithNVR(
        nvr=NVR(name="test", version="1.0.0", release="1.fc40")
    ).model_dump_json()
    assert actual == expected


class ModelWithNVRA(BaseModel):
    nvra: NvraSchema


# Ignore: ruff N802
# Reason: These test cases are named to reflect the type that they are testing,
#   which is why they use CamelCase.
def test_NvraSchema_validation_from_string():  # noqa: N802
    expected = ModelWithNVRA(
        nvra=NVRA(name="test", version="1.0.0", release="1.fc40", arch="aarch64")
    )
    actual = ModelWithNVRA.model_validate({"nvra": "test-1.0.0-1.fc40.aarch64"})
    assert actual == expected


# Ignore: ruff N802
# Reason: These test cases are named to reflect the type that they are testing,
#   which is why they use CamelCase.
def test_NvraSchema_validation_from_json():  # noqa: N802
    expected = ModelWithNVRA(
        nvra=NVRA(name="test", version="1.0.0", release="1.fc40", arch="aarch64")
    )
    actual = ModelWithNVRA.model_validate_json('{"nvra":"test-1.0.0-1.fc40.aarch64"}')
    assert actual == expected


# Ignore: ruff N802
# Reason: These test cases are named to reflect the type that they are testing,
#   which is why they use CamelCase.
def test_NvraSchema_serialization_to_json():  # noqa: N802
    expected = '{"nvra":"test-1.0.0-1.fc40.aarch64"}'
    actual = ModelWithNVRA(
        nvra=NVRA(name="test", version="1.0.0", release="1.fc40", arch="aarch64")
    ).model_dump_json()
    assert actual == expected
