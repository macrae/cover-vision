import unittest

# from pandas import DataFrame

import comics_net.analyzer as analyzer

metadata_path = "./comics_net/resources/metadata.jsonl"


def test_load_metadata():
    metadata = analyzer.load_metadata(metadata_path)
    expected_keys = set(
        [
            "cover_characters",
            "cover_colors",
            "cover_first line of dialogue or text",
            "cover_genre",
            "cover_inks",
            "cover_keywords",
            "cover_letters",
            "cover_pencils",
            "covers",
            "format_binding",
            "format_color",
            "format_dimensions",
            "format_paper_stock",
            "format_publishing_format",
            "indexer_notes",
            "indicia_frequency",
            "issue_brand",
            "issue_indicia_publisher",
            "issue_pages",
            "issue_price",
            "on_sale_date",
            "rating",
            "series_name",
            "synopsis",
            "title",
            "variant_covers",
        ]
    )

    assert set(metadata.keys()).difference(expected_keys) == set()


def test_get_issue_number_from_title():
    title = "Superman #12"
    results = analyzer.get_issue_number_from_title(title)
    assert results == 12


def test_match_brackets():
    characters = "Batman [Bruce Wayne]"
    results = analyzer.match_brackets(characters)
    assert results == {"[Bruce Wayne]": {"end": 20, "start": 7}}

    characters = "Batman [Bruce Wayne], Superman  [Clark Kent]"
    results = analyzer.match_brackets(characters)
    assert results == {
        "[Bruce Wayne]": {"end": 20, "start": 7},
        "[Clark Kent]": {"end": 44, "start": 32},
    }


def test_replace_semicolons_in_brackets():
    test = """Superman [Clark Kent; Kal-El]"""

    results = analyzer.replace_semicolons_in_brackets(test)
    assert results == """Superman [Clark Kent/ Kal-El]"""


def test_look_behind():
    s = "Superman; Batman; Wonder Woman"
    results = analyzer.look_behind(s, len(s) + 1)
    assert results == "Wonder Woman"


# TODO: write better test examples
def test_convert_character_dict_to_str():
    character_dict = {
        "Teams": {"Justice League": {"Batman": "Bruce Wayne", "Superman": "Clark Kent"}}
    }
    results = analyzer.convert_character_dict_to_str(character_dict)
    assert results == "Justice League: Batman: Bruce Wayne; Superman: Clark Kent"


def test_diff_strings():
    s1 = "Hello World!"
    s2 = "Hello"

    assert analyzer.diff_strings(s2, s1) == " World!"
    assert analyzer.diff_strings(s1, s2) == ""


def test_convert_characters_to_list():
    s = "Superman [Clark Kent; Kal-El]; Batman [Bruce Wayne]; Wonder Woman [Diana Prince]"
    results = analyzer.convert_characters_to_list(s)
    assert results == [
        "Superman [Clark Kent/ Kal-El]",
        "Batman [Bruce Wayne]",
        "Wonder Woman [Diana Prince]",
    ]


def test_get_random_sample_of_covers():
    assert True

def test_create_training_dirs():
    assert True