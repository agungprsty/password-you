#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from datetime import datetime
from .utils import *

class TestUtils(TestCase):
    def test_is_int(self):
        test_cases = [
            {
                "test_name": "Test with None value",
                "input": None,
                "output": False,
            },
            {
                "test_name": "Test with non integer string value",
                "input": "21a",
                "output": False,
            },
            {
                "test_name": "Test with integer string value",
                "input": "21",
                "output": True,
            },
            {
                "test_name": "Test with integer value",
                "input": 1,
                "output": True,
            },
        ]

        for test_item in test_cases:
            with self.subTest(test_item.get("test_name")):
                result = is_int(test_item.get("input"))
                self.assertEqual(result, test_item.get("output"))

    def test_safe_bool(self):
        test_cases = [
            {
                "test_name": "Test with invalid value",
                "input": [None],
                "error": ValueError,
            },
            {
                "test_name": "Test with valid string true values",
                "input": ["yes", "true", "t", "y", "1"],
                "output": True,
            },
            {
                "test_name": "Test with valid string false values",
                "input": ["no", "false", "f", "n", "0"],
                "output": False,
            },
            {
                "test_name": "Test with boolean value",
                "input": [True],
                "output": True,
            },
        ]

        for test_item in test_cases:
            with self.subTest(test_item.get("test_name")):
                for input_value in test_item.get("input"):
                    try:
                        result = safe_bool(input_value)
                        self.assertEqual(result, test_item.get("output"))
                    except Exception as e:
                        self.assertIsNotNone(test_item.get("error"))
                        self.assertIsInstance(e, test_item.get("error"))

    def test_safe_int(self):
        test_cases = [
            {
                "test_name": "Test with None value",
                "input": {"data": None},
                "output": 0,
            },
            {
                "test_name": "Test with invalid string values",
                "input": {"data": "21a"},
                "output": 0,
            },
            {
                "test_name": "Test with invalid string with default value",
                "input": {"data": "21a", "default": 32},
                "output": 32,
            },
            {
                "test_name": "Test with valid string",
                "input": {"data": "21", "default": 32},
                "output": 21,
            },
            {
                "test_name": "Test with integer",
                "input": {"data": 21, "default": 32},
                "output": 21,
            },
            {
                "test_name": "Test with invalid negative integer",
                "input": {"data": -21,},
                "output": 0,
            },
            {
                "test_name": "Test with invalid ",
                "input": {"data": 9223372036854775808,},
                "output": 0,
            },
        ]

        for test_item in test_cases:
            with self.subTest(test_item.get("test_name")):
                input_value = test_item.get("input")
                result = safe_int(input_value.get("data"), input_value.get("default", 0))
                self.assertEqual(test_item.get("output"), result)
                        

    def test_safe_float(self):
        test_cases = [
            {
                "test_name": "Test with None value",
                "input": {"data": None},
                "output": 0.0,
            },
            {
                "test_name": "Test with invalid string values",
                "input": {"data": "21a"},
                "output": 0.0,
            },
            {
                "test_name": "Test with invalid string with default value",
                "input": {"data": "21a", "default": 32.4},
                "output": 32.4,
            },
            {
                "test_name": "Test with valid string",
                "input": {"data": "21.2", "default": 32},
                "output": 21.2,
            },
            {
                "test_name": "Test with integer",
                "input": {"data": 21.2, "default": 32.4 },
                "output": 21.2,
            },
        ]

        for test_item in test_cases:
            with self.subTest(test_item.get("test_name")):
                input_value = test_item.get("input")
                result = safe_float(input_value.get("data"), input_value.get("default", 0))
                self.assertEqual(test_item.get("output"), result)

    def test_generate_random_string(self):
        result = generate_random_string(64)
        self.assertIsInstance(result, str)
        self.assertEqual(64 * 2, len(result))

    def test_now(self):
        result = now()
        self.assertIsInstance(result, int)
    