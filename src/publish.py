LINE_MAX_TEXT = 38


def indent(text, prefix):
    max_num = LINE_MAX_TEXT - len(prefix)
    result = prefix
    for _ in range(1000):
        result += text[:max_num]
        result += "\n" + "　" * len(prefix)
        text = text[max_num:]
        if len(text) <= max_num:
            result += text
            break

    return result


def parse(text):
    if text[:3] == "導師：":
        return indent(text[3:], "導師　　　")

    else:
        return "　　　" + text


def convert(input_path, output_path):
    with open(input_path, "r") as f:
        lines = f.readlines()
    with open(output_path, "w") as f:
        for line in lines:
            f.write(parse(line))
            f.write("\n")


if __name__ == "__main__":
    input_path = "モノローグ.md"
    output_path = "main.md"
    convert(input_path, output_path)
