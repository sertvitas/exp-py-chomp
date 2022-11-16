"""
asdlfadlkdsajf
"""

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
