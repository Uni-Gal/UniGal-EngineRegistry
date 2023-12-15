import json
from functools import cmp_to_key

syntax_1 = "<!-- MARKDOWN_TABLE BEGIN -->"
syntax_2 = "<!-- WARNING: THIS TABLE IS MAINTAINED BY PROGRAMME, YOU SHOULD ADD DATA TO COLLECTION JSON -->"
syntax_3 = "<!-- MARKDOWN_TABLE END -->"


def x_sort(data):
    def compare(dict_a: dict, dict_b: dict):
        dict_a_packagename = (
            dict_a["engine_name"].replace("_", "").replace("-", "").lower()
        )
        dict_b_packagename = (
            dict_b["engine_name"].replace("_", "").replace("-", "").lower()
        )
        if dict_a_packagename < dict_b_packagename:
                return -1
        if dict_a_packagename > dict_b_packagename:
                return 1

    data = sorted(data, key=cmp_to_key(compare))
    return data

def markdown_row(data: list):
    string = ""
    for i in data:
        string += "| " + i + " "
    string += "|\n"
    return string


def markdown_header(translation: dict, locale: str):
    locale_translation = {}
    for i in range(len(translation)):
        if translation[i]["locale"] == locale:
            locale_translation = translation[i]["translation"]
    data = [
        locale_translation["package_name"],
        locale_translation["institution_name"],
        locale_translation["maintainer_type"],
        locale_translation["repository"],
        locale_translation["ctan_package"],
        locale_translation["status"],
    ]
    return markdown_row(data)


def markdown_table(length: int):
    data = ["-", "-", "-", "-", "-", "-"]
    return markdown_row(data)


def markdown_entry(thesis_entry: dict):
    data = [
        thesis_entry["package_name"],
        thesis_entry["institution_name"],
        thesis_entry["maintainer_type"],
        repos(
            maintainer_type=thesis_entry["maintainer_type"],
            repository_github=thesis_entry["repository_github"],
            repository_gitlab=thesis_entry["repository_gitlab"],
            repository_gitee=thesis_entry["repository_gitee"],
            repository_gitea=thesis_entry["repository_gitea"],
        ),
        badge(
            link=thesis_entry["ctan_package"],
            badge_type="ctan",
        ),
        thesis_entry["status"],
    ]
    return markdown_row(data)


def markdown_gen(locale: str):
    engine_json = open("..\\data\\engine.json", "r", encoding="utf-8")
    engine_data = json.loads(engine_json.read())["engine_data"]
    column_json = open("..\\data\\column.json", "r", encoding="utf-8")
    column_data = json.loads(column_json.read())
    string = ""
    if locale != "Default":
        string += markdown_header(column_data["i18n"], locale)
    else:
        string += markdown_header(column_data["i18n"], "zh-CN")
    string += markdown_table(
        column_data["len"],
    )
    # ALT CODE: engine_data.sort(key=lambda x: x["engine_name"])
    engine_data = x_sort(engine_data)
    for i in range(len(engine_data)):
        string += markdown_entry(engine_data[i])
    return string


def markdown_body(locale, text, token_begin, token_warn, token_end):
    readme_slice = text.split(token_begin)
    readme_slice.append(readme_slice[1].split(token_warn)[0])
    readme_slice.append(readme_slice[1].split(token_end)[1])
    table = markdown_gen(locale)
    markdown = (
        readme_slice[0]
        + token_begin
        + "\n"
        + token_warn
        + "\n"
        + table
        + "\n"
        + token_end
        + readme_slice[3]
    )
    if table == "":
        return text
    else:
        return markdown


def readme_gen(readme_locale):
    if readme_locale != "":
        path = "..\\README" + "-" + readme_locale + ".md"
    else:
        readme_locale = "Default"
        path = "..\\README.md"
    readme_file = open(path, "r", encoding="utf-8")
    readme_text = readme_file.read()
    readme_file.close()
    readme_text = markdown_body(
        readme_locale, readme_text, syntax_1, syntax_2, syntax_3
    )
    readme_file = open(path, "w", encoding="utf-8")
    readme_file.write(readme_text)
    readme_file.close()
    print(readme_locale, ": ", path.replace("..\\", "").replace("../", ""))


readme_gen("")
readme_gen("zh-CN")
readme_gen("en-US")
