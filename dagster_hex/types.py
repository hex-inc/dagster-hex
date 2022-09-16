from collections import namedtuple

RunResponse = namedtuple(
    "RunResponse",
    ["projectId", "runId", "runUrl", "runStatusUrl", "traceId"],
)

StatusResponse = namedtuple(
    "StatusResponse",
    [
        "projectId",
        "runId",
        "runUrl",
        "status",
        "startTime",
        "endTime",
        "elapsedTime",
        "traceId",
    ],
)
