import re
import shlex
import platform

CURRENT_OS = platform.system().lower()

# Dangerous command patterns
BLOCKED_PATTERNS = [

    # Linux dangerous commands
    r"rm\s+-rf\s+/",
    r"mkfs",
    r"dd\s+if=",
    r":\(\)\s*{\s*:\|:&\s*};:",
    r"shutdown",
    r"reboot",
    r"halt",

    # Windows dangerous commands
    r"format\s+c:",
    r"del\s+/f",
    r"rd\s+/s",
    r"powershell\s+-enc",

    # Generic dangerous
    r"curl.*\|\s*sh",
    r"wget.*\|\s*sh",
    r"chmod\s+777\s+/",
    r"sudo\s+rm",
    r"> /dev/sd",
]

# Allowed commands
SAFE_COMMANDS = [

    # File/Folder
    "mkdir",
    "cd",
    "touch",
    "echo",
    "cat",

    # Python
    "python",
    "pip",
    "pip3",

    # Node
    "node",
    "npm",
    "npx",

    # Git
    "git",

    # Django
    "django-admin",

    # Windows compatible
    "type",
    "new-item",
    "set-content",

    # Linux/macOS
    "ls",

    # Other useful commands
    "dir",
    "powershell"
    
]


def validate_command(command):

    command_lower = command.lower()

    # -----------------------------
    # BLOCK DANGEROUS COMMANDS
    # -----------------------------
    for pattern in BLOCKED_PATTERNS:

        if re.search(pattern, command_lower):
            return False, f"Blocked dangerous pattern: {pattern}"

    # -----------------------------
    # ALLOW POWERSHELL SAFE COMMANDS
    # -----------------------------
    if command_lower.startswith("powershell"):

        blocked_inside_powershell = [
            "remove-item",
            "format-volume",
            "shutdown",
            "restart-computer",
            "stop-computer",
            "del ",
            "rd ",
        ]

        for bad in blocked_inside_powershell:

            if bad in command_lower:
                return False, f"Blocked PowerShell command: {bad}"

        return True, "Safe PowerShell command"

    # -----------------------------
    # HANDLE NORMAL COMMANDS
    # -----------------------------
    parts = re.split(r'&&|;', command)

    for part in parts:

        part = part.strip()

        if not part:
            continue

        first_word = part.split()[0]
        first_word = first_word.lower()

        first_word = first_word.strip()

        if first_word not in SAFE_COMMANDS:
            return False, f"Command not allowed: {first_word}"

    return True, "Safe command"