"""
asdlfadlkdsajf
"""
import boto3
import yaml
import json
from typing import Dict, List


def deployment_plan() -> Dict[str, Dict[str, List[str]]]:
    return {
        "rolling": {
            "phase 1": ["notification"],
            "phase 2": [
                "tokenservice",
                "devapi",
                "rpapi",
            ],
        },
        "downtime": {"phase 1": ["idpcore", "idpuser"]},
    }


def use_plan(plan: Dict[str, Dict[str, List[str]]]):
    rolling = plan["rolling"]
    downtime = plan["downtime"]
    return rolling["phase 1"][0]


def save_plan(plan: Dict[str, Dict[str, List[str]]]):
    with open(r"data.yaml", "w") as file:
        documents = yaml.dump(plan, file)


def list_clusters() -> List[str]:
    result = []
    client = boto3.client("ecs", region_name="us-east-1")

    paginator = client.get_paginator("list_clusters")

    response_iterator = paginator.paginate(PaginationConfig={"PageSize": 100})

    for each_page in response_iterator:
        for each_arn in each_page["clusterArns"]:
            result.append(each_arn)
    return result


def list_services():
    result = []
    client = boto3.client("ecs")
    paginator = client.get_paginator("list_services")
    response_iterator = paginator.paginate(
        cluster="common-platform-sandbox-cps",
        PaginationConfig={"MaxItems": 100, "PageSize": 100},
    )
    for each_page in response_iterator:
        for each_arn in each_page["serviceArns"]:
            result.append(each_arn)
    return result
    pass


def list_containers():
    result = []
    client = boto3.client("ecs")
    paginator = client.get_paginator("list_container_instances")
    response_iterator = paginator.paginate(
        cluster="common-platform-sandbox-cps",
        PaginationConfig={"MaxItems": 100, "PageSize": 100},
    )
    for each_page in response_iterator:
        for each_arn in each_page["containerInstanceArns"]:
            result.append(each_arn)
    return result
    pass


def list_tasks(cluster: str):
    result = []
    client = boto3.client(
        "ecs",
        region_name="us-east-1",
    )

    paginator = client.get_paginator("list_tasks")

    response_iterator = paginator.paginate(
        cluster=cluster, PaginationConfig={"PageSize": 100}
    )

    for each_page in response_iterator:
        for each_task in each_page["taskArns"]:
            result.append(each_task)
    return result


def describe_tasks(cluster: str, tasks: List[str]):
    client = boto3.client("ecs")
    response = client.describe_tasks(
        cluster="common-sandbox-notificationservice",
        tasks=tasks,
    )
    return response
