import json

def format_text(text):
    formatted_sentence = ""
    text_lines = text.split("\n")
    lines = len(text_lines)

    for i in range(lines - 2):  # Skip the "end" in the output
        line = text_lines[i].strip()
        if not line:
            continue

        try:
            data = json.loads(line)
            if "t" in data:
                formatted_sentence += data["t"]
        except json.JSONDecodeError:
            # Handle the case where the line is not a valid JSON string
            print(f"Error decoding JSON for line: {line}")

    formatted_sentence = formatted_sentence.strip()
    return formatted_sentence
