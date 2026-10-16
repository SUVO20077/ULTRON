import webbrowser
import subprocess

from urllib.parse import urlparse
from datetime import datetime


# ==========================================
# ULTRON TOOL: OPEN WEBSITE
# ==========================================

def open_website(url: str) -> str:

    try:

        parsed = urlparse(url)

        if parsed.scheme not in ("http", "https"):
            return "I can only open HTTP or HTTPS websites."

        if not parsed.netloc:
            return "That does not appear to be a valid website."

        webbrowser.open(url)

        return f"Website opened successfully: {url}"

    except Exception as e:

        return f"I could not open the website: {e}"


# ==========================================
# ULTRON TOOL: GET TIME
# ==========================================

def get_time() -> str:

    current_time = datetime.now().strftime(
        "%I:%M %p"
    )

    return f"The current local time is {current_time}."


# ==========================================
# ULTRON TOOL: LAUNCH APPLICATION
# ==========================================

ALLOWED_APPLICATIONS = {

    "calculator": "calc.exe",
    "calc": "calc.exe",

    "notepad": "notepad.exe",

    "file explorer": "explorer.exe",
    "explorer": "explorer.exe",

    "chrome": "chrome.exe",
    "google chrome": "chrome.exe",
}


def launch_application(application: str) -> str:

    application = application.lower().strip()

    if application not in ALLOWED_APPLICATIONS:

        return (
            f"I am not authorized to launch "
            f"{application}."
        )

    try:

        subprocess.Popen(
            ALLOWED_APPLICATIONS[application]
        )

        return (
            f"{application} launched successfully."
        )

    except Exception as e:

        return (
            f"I could not launch "
            f"{application}: {e}"
        )