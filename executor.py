import subprocess
import os

from validator import validate_command

CURRENT_DIR = os.getcwd()


def execute_command(command):

    global CURRENT_DIR

    print(f"\nCommand: {command}")

    # -----------------------------
    # VALIDATE
    # -----------------------------
    is_safe, message = validate_command(command)

    if not is_safe:

        print(f"\nBLOCKED: {message}")

        return False

    print("\nValidation Passed")

    # -----------------------------
    # HANDLE CD COMMAND
    # -----------------------------
    if command.startswith("cd "):

        new_dir = command[3:].strip()

        new_path = os.path.join(CURRENT_DIR, new_dir)

        if os.path.exists(new_path):

            CURRENT_DIR = new_path

            print(f"\nChanged directory to: {CURRENT_DIR}")

            return True

        else:

            print("\nDirectory does not exist")

            return False

    # -----------------------------
    # EXECUTE COMMAND
    # -----------------------------
    try:

        process = subprocess.run(
            command,
            shell=True,
            text=True,
            capture_output=True,
            timeout=60,
            cwd=CURRENT_DIR
        )

        print("\nSTDOUT:")
        print(process.stdout)

        print("\nSTDERR:")
        print(process.stderr)

        if process.returncode != 0:
            return False

        return True

    except subprocess.TimeoutExpired:

        print("\nCommand timed out")

        return False

    except Exception as e:

        print("\nExecution Error:", str(e))

        return False