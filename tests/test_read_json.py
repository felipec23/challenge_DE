import pytest
from src.q1_memory import read_json_q1_memory
from src.q1_time import read_json_q1_time
from src.q3_memory import read_json_q3_memory
from src.q3_time import read_json_q3_time
import os


def test_read_json_q1_memory():

    file_path = os.path.join(os.path.dirname(__file__), "test_data", "sample.json")

    results = [x for x in read_json_q1_memory(file_path)]

    truth = [
        ["ArjunSinghPanam", "2021-02-24"],
        ["PrdeepNain", "2021-02-24"],
        ["parmarmaninder", "2021-02-24"],
        ["anmoldhaliwal", "2021-02-24"],
        ["KotiaPreet", "2021-02-24"],
    ]
    assert results == truth


def test_read_json_q1_time():

    file_path = os.path.join(os.path.dirname(__file__), "test_data", "sample.json")

    results = [x for x in read_json_q1_time(file_path)]

    truth = [
        ["ArjunSinghPanam", "2021-02-24"],
        ["PrdeepNain", "2021-02-24"],
        ["parmarmaninder", "2021-02-24"],
        ["anmoldhaliwal", "2021-02-24"],
        ["KotiaPreet", "2021-02-24"],
    ]
    assert results == truth


def test_read_json_q3_memory():

    file_path = os.path.join(os.path.dirname(__file__), "test_data", "sample.json")

    results = [x for x in read_json_q3_memory(file_path)]

    truth = [
        ["narendramodi", "DelhiPolice"],
        ["Kisanektamorcha"],
        ["ReallySwara", "rohini_sgh"],
    ]

    assert results == truth


def test_read_json_q3_time():

    file_path = os.path.join(os.path.dirname(__file__), "test_data", "sample.json")

    results = [x for x in read_json_q3_time(file_path)]

    truth = [
        ["narendramodi", "DelhiPolice"],
        ["Kisanektamorcha"],
        ["ReallySwara", "rohini_sgh"],
    ]

    assert results == truth
