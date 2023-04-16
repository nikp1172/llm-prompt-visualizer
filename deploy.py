import argparse
import logging
import os

from servicefoundry import Build, PythonBuild, Resources, Service, LocalSource

logging.basicConfig(level=logging.INFO)

# parsing the input arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "--workspace_fqn",
    type=str,
    required=True,
    help="fqn of workspace where you want to deploy",
)
args = parser.parse_args()

# creating a service object and defining all the configurations
service = Service(
    name="llm-prompt-demo",
    image=Build(
        build_spec=PythonBuild(
            command="streamlit run main.py",
            python_version="3.9",
        ),
        build_source=LocalSource(local_build=False)
    ),
    env={
        "TFY_API_KEY": "tfy-secret://truefoundry:llm-sg:TFY_API_KEY",
        "TFY_HOST": "https://app.truefoundry.com",
        "ML_REPO_ID": "688",
        "MODEL_NAME_VAR": "model_name",
        "PROMPT_VAR": "prompt1",
        "RESPONSE_VAR": "response1",
        "INFERENCE_TIME_VAR": "inference_time",
        "USER_REACTION_VAR": "user_reaction"
    },
    ports=[{"port": 8501, "host": "llm-demo-8080.demo.truefoundry.com"}],
    resources=Resources(
        cpu_request=0.2, cpu_limit=0.2, memory_limit=300, memory_request=300
    ),
    replicas=1
)
service.deploy(workspace_fqn=args.workspace_fqn)