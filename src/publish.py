import re

LINE_MAX_TEXT = 38

input_path = "index.md"
output_path = "out/out.md"


def join_files():
    """分割して書いたファイルを結合"""
    result = []

    # main.mdを読み込む
    with open(input_path, "r") as f:
        main_lines = f.readlines()

    # main.mdの中にあるリンクを展開
    for main_line in main_lines:

        # 最初に埋め込みリンクがあるかチェック
        match = re.search(r'!\[\[(.+)\]\]', main_line)
        if not match:
            # 埋め込みリンクがない場合は通常のリンクとして処理
            match = re.search(r'\[\[(.+)\]\]', main_line)

        # main.mdに書いてある場面のタイトルのみを残す
        unlinked_text = re.sub(r"[!\[\]]", "", main_line)
        result.append("scene:" + unlinked_text)

        # ファイルを読み込む
        part_lines = []
        if match:
            path = "Scene/" + match.group(1) + ".md"
            with open(path, "r") as f:
                part_lines = f.readlines()
        # 場面の内容を追加
        for part_line in part_lines:
            part_line = re.sub(r"[\n\[\]]", "", part_line)
            result.append(part_line)

    return result


def indent(text, prefix):
    """天付きのインデントをつける"""
    max_num = LINE_MAX_TEXT - len(prefix)
    result = prefix

    # 一行に収まらない場合は改行
    for _ in range(1000):
        result += text[:max_num]
        text = text[max_num:]
        if len(text) <= max_num:
            if len(text) > 0:
                result += "\n" + "　" * len(prefix)
                result += text
            break
        result += "\n" + "　" * len(prefix)

    return result


def parse(text):
    """セリフとト書き、シーン名を整形"""

    if len(text) == 0:
        return "　\n\n"

    if text[:6] == "scene:":
        text = text[6:]
        text = re.sub(r"([a-zA-Z0-9]+)",
                      r'<span class="tcy">\1</span>',
                      text)
        return text + "\n　\n\n"

    # 縦中横の処理
    text = re.sub(r"([a-zA-Z0-9]+)",
                  r'<span class="tcy">\1</span>',
                  text)

    if text[:3] == "導師：":
        return indent(text[3:], "導師　　　") + "\n\n"

    return indent(text, "　　　") + "\n\n"



def convert(joined_lines, output_path):
    with open(output_path, "w") as f:
        for line in joined_lines:
            f.write(parse(line))


if __name__ == "__main__":
    joined_lines = join_files()
    convert(joined_lines, output_path)
