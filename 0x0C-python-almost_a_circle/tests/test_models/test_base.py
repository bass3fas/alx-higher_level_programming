#!/usr/bin/python3
"""Defining unit tests for Base """
import os
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """testing different instantations"""
    def test_init_with_id(self):
        """testing if id is set"""
        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_init_without_id(self):
        """testing if id is not given"""
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_to_json_string(self):
        result1 = Base.to_json_string(None)
        self.assertEqual(result1, '[]')
        result2 = Base.to_json_string([])
        self.assertEqual(result2, '[]')

    def test_save_to_file(self):
        # Implement tests for save_to_file method
        pass
        # Make sure to clean up the generated file after testing

    def test_from_json_string(self):
        # Implement tests for from_json_string method
        pass
        
    def test_create(self):
        # Implement tests for create method
        pass
        
    def test_load_from_file(self):
        # Implement tests for load_from_file method
        pass
        
    def test_save_to_file_csv(self):
        # Implement tests for save_to_file_csv method
        # Make sure to clean up the generated file after testing
        pass
        
    def test_load_from_file_csv(self):
        # Implement tests for load_from_file_csv method
        pass
    
if __name__ == '__main__':
    unittest.main()
