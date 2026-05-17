from agent import generate_project_steps
from file_manager import create_directory, create_file


def main():

    print("=" * 50)
    print("AI Development Agent")
    print("=" * 50)

    user_input = input("\nWhat project do you want to build?\n\n> ")

    result = generate_project_steps(user_input)

    print("\nProject:", result["project_name"])

    steps = result["steps"]

    for step in steps:

        print("\n" + "=" * 50)
        print(f"STEP {step['step']}")
        print("=" * 50)

        action = step["action"]

        print("Action:", action)

        confirm = input("\nExecute this step? (y/n): ")

        if confirm.lower() != "y":
            continue

        # -----------------------------
        # CREATE DIRECTORY
        # -----------------------------
        if action == "create_directory":

            path = step["path"]

            create_directory(path)

        # -----------------------------
        # CREATE FILE
        # -----------------------------
        elif action == "create_file":

            path = step["path"]

            content = step.get("content", "")

            create_file(path, content)

    print("\nProject generation completed.")


if __name__ == "__main__":
    main()