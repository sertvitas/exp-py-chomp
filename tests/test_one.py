from one import use_plan, deployment_plan
import pytest


@pytest.mark.experimental
def test_use_plan():
    res = deployment_plan()
    assert use_plan(res) == "notification"
