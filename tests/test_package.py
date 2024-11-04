from __future__ import annotations

import importlib.metadata

import quantity_2_0 as m


def test_version():
    assert importlib.metadata.version("quantity_2_0") == m.__version__
