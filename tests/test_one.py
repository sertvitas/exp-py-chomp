from one import \
    use_plan, \
    deployment_plan, \
    save_plan, \
    list_clusters, \
    list_services, \
    list_containers, \
    list_tasks
import pytest


@pytest.mark.experimental
def test_use_plan():
    res = deployment_plan()
    assert use_plan(res) == "notification"

@pytest.mark.experimental
def test_save_plan():
    res = deployment_plan()
    gg = save_plan(res)
    assert save_plan(res) == None


def test_list_cluster():
    res = list_clusters()
    assert True

def test_list_services():
    res = list_services()
    assert True

def test_list_containers():
    res = list_containers()
    assert True

def test_list_tasks():
    res = list_tasks()
    assert True
