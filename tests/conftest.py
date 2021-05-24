# -*- coding: utf-8 -*-
import errno

import pytest

try:
    __import__("pytest_xprocess")
    from xprocess import ProcessStarter
except ImportError:

    @pytest.fixture(scope="session")
    def xprocess():
        pytest.skip("pytest-xprocess not installed.")


@pytest.fixture
def db_url():
    return "mysql://root@localhost:3306/lms_test"
