# test_routingservice.py
"""
Tests for RoutingService module.
"""

import unittest
from routingservice import RoutingService

class TestRoutingService(unittest.TestCase):
    """Test cases for RoutingService class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RoutingService()
        self.assertIsInstance(instance, RoutingService)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RoutingService()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
