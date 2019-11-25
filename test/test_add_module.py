# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 10:24:39 2019

@author: lennie
"""

import pytest
import sys

sys.path.append(".")
sys.path.append("./src")

from src import add_module


class TestAddModule():
    @pytest.fixture(scope='session')
    def create_object_for_testing(self):
        """ Sets up the object for further testing
        """
        return add_module.AddClass()
    
    
    @pytest.mark.parametrize("test_input,expected", [((3,1), 4), ((0,0), 0), ((1e6,1e6), 2e6),((-1,1), 0)])
    def test_basic_addition(self,test_input,expected,create_object_for_testing):
        """ Does a test on normal inputs. 
        """
        actual = create_object_for_testing.Add(*test_input)
        print(actual)
        message = "Failed with Add({}) giving: {}, instead of the expected: {} ".format(test_input,actual,expected)
        assert actual==expected,message 
        
    def test_type_input(self,create_object_for_testing):
        """ throws in wrong input type. 
        """
        actual = create_object_for_testing.Add(0,'s')
        expected = None
        message = "Failed with Add({}) giving: {}, instead of the expected: {} ".format((0,'s'),actual,expected)
        assert actual==expected, message