from dagster import AssetMaterialization, Field, In, Noneable, Nothing, Out, Output, op

from .resources import DEFAULT_POLL_INTERVAL
from .types import StatusResponse


@op(
    required_resource_keys={"hex"},
    ins={"start_after": In(Nothing)},
    out=Out(
        StatusResponse,
        description="Parsed json dictionary representing the details of the Hex"
        "project after the run successfully completes.",
    ),
    config_schema={
        "sync_id": Field(
            str, is_required=True, description="The Sync ID that this op will trigger."
        ),
        "poll_interval": Field(
            float,
            default_value=DEFAULT_POLL_INTERVAL,
            description="The time (in seconds) that will be waited between successive "
            "polls.",
        ),
        "fail_on_warning": Field(
            bool,
            default_value=False,
            description="Whether to consider warnings a failure or success for an op.",
        ),
        "poll_timeout": Field(
            Noneable(float),
            default_value=None,
            description="The maximum time that will waited before this operation is "
            "timed out. By default, this will never time out.",
        ),
    },
    tags={"kind": "hex"},
)
def hex_project_op(context):
    """
    Executes a Hex project for a given `project_id`, and polls until that run
    completes, raising an error if it is unsuccessful. It outputs a StatusResponse
    which contains the details of the Hex project after the run completes.
    """

    hex_output: StatusResponse = context.resources.hex.run_and_poll(
        project_id=context.op_config["project_id"],
        inputs=context.op_config["inputs"],
        update_cache=context.op_config["update_cache"],
        kill_on_timeout=context.op_config["kill_on_timeout"],
        poll_interval=context.op_config["poll_interval"],
        poll_timeout=context.op_config["poll_timeout"],
    )
    asset_name = ["hex", hex_output.projectId]

    context.log_event(
        AssetMaterialization(
            asset_name,
            description="Hex Project Details",
        )
    )
    yield Output(hex_output)
