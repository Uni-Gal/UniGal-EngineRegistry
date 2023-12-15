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
        locale_translation["engine_system"],
        locale_translation["engine_name"],
        locale_translation["engine_main_language"],
        locale_translation["status_alive"],
        locale_translation["native_engine_support"],
        locale_translation["bi_directional_import_export"],
        locale_translation["importable_from_unigal"],
        locale_translation["exportable_to_unigal"],
        locale_translation["no_support_planned"],
        locale_translation["is_free"],
    ]
    return markdown_row(data)


def markdown_table(length: int):
    data = ["-" for i in range(length)]
    return markdown_row(data)


def markdown_entry(engine_entry: dict):
    data = [
        engine_entry["engine_system"],
        engine_entry["engine_name"],
        engine_entry["engine_main_language"],
        engine_entry["status_alive"],
        engine_entry["native_engine_support"],
        engine_entry["bi_directional_import_export"],
        engine_entry["importable_from_unigal"],
        engine_entry["exportable_to_unigal"],
        engine_entry["no_support_planned"],
        engine_entry["is_free"],
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
