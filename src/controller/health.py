from fastapi import HTTPException


async def health() -> str:
    """
    Retreives a message to perform quick verification about the API status.

    :return: A message indicating all is good. If something goes wrong, throws a exception with 500 code.
    :rtype: str
    :raises HTTPException: If something goes wrong.
    """

    try:
        return "Healthy"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
