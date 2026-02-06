"""
Purpose:
Practice basic file input/output with error handling.

What this script does:
- Reads a file
- Processes content
- Writes output safely
"""

from pathlib import Path


def read_file(file_path: Path) -> str:
    try:
        return file_path.read_text()
    except FileNotFoundError:
        print("File not found.")
        return ""
    except Exception as exc:
        print(f"Unexpected error: {exc}")
        return ""


def process_content(content: str) -> str:
    # TODO: add actual logic
    return content.upper()


def write_file(file_path: Path, content: str) -> None:
    file_path.write_text(content)


def main():
    input_file = Path("input.txt")
    output_file = Path("output.txt")

    content = read_file(input_file)
    if not content:
        return

    processed = process_content(content)
    write_file(output_file, processed)


if __name__ == "__main__":
    main()
