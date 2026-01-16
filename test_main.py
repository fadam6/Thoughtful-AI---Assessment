import pytest
from main import sort

def test_standard_small_light():
    assert sort(10, 10, 10, 1) == "STANDARD"


def test_heavy_only_boundary():
    assert sort(10, 10, 10, 20) == "SPECIAL"


def test_bulky_by_dimension_boundary():
    assert sort(150, 10, 10, 1) == "SPECIAL" 


def test_bulky_by_volume_boundary_exact():
    assert sort(100, 100, 100, 1) == "SPECIAL"


def test_rejected_when_both_bulky_and_heavy():
    assert sort(100, 100, 100, 20) == "REJECTED"


def test_not_bulky_just_below_volume_threshold():
    assert sort(99, 100, 100, 19.999) == "STANDARD"


def test_invalid_negative_dimension():
    with pytest.raises(ValueError):
        sort(-1, 10, 10, 1)


def test_invalid_negative_mass():
    with pytest.raises(ValueError):
        sort(10, 10, 10, -0.1)
