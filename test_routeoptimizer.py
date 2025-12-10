# test_routeoptimizer.py
"""
Tests for RouteOptimizer module.
"""

import unittest
from routeoptimizer import RouteOptimizer

class TestRouteOptimizer(unittest.TestCase):
    """Test cases for RouteOptimizer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RouteOptimizer()
        self.assertIsInstance(instance, RouteOptimizer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RouteOptimizer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
