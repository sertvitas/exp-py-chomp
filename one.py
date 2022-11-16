"""
asdlfadlkdsajf
"""
import boto3
import yaml
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
    with open(r'data.yaml', 'w') as file:
        documents = yaml.dump(plan, file)



def list_clusters() -> List[str]:
    result = []
    client = boto3.client("ecs", region_name="us-east-1")

    paginator = client.get_paginator('list_clusters')

    response_iterator = paginator.paginate(
        PaginationConfig={
            'PageSize':100
        })

    for each_page in response_iterator:
        for each_arn in each_page['clusterArns']:
            result.append(each_arn)
    return result
