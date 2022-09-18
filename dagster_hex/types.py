from typing import NamedTuple, TypedDict

RunResponse = TypedDict(
    "RunResponse",
    {
        "projectId": str,
        "runId": str,
        "runUrl": str,
        "runStatusUrl": str,
        "traceId": str,
    },
)

StatusResponse = TypedDict(
    "StatusResponse",
    {
        "projectId": str,
        "runId": str,
        "runUrl": str,
        "status": str,
        "startTime": str,
        "endTime": str,
        "elapsedTime": int,
        "traceId": str,
    },
)


class HexOutput(
    NamedTuple(
        "_HexOutput",
        [
            ("run_response", RunResponse),
            ("status_response", StatusResponse),
        ],
    )
):
    pass
