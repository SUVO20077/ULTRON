from core.voice_commands import handle_voice_command


def process_voice_command(command, state):
    """
    Sends a spoken command to ULTRON's central command router.

    Returns:
        str | None:
            Response if ULTRON understands the command,
            otherwise None so Gemini can handle it.
    """

    response = handle_voice_command(command, state)

    return response