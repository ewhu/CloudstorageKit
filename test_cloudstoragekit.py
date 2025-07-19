# test_cloudstoragekit.py
"""
Tests for CloudstorageKit module.
"""

import unittest
from cloudstoragekit import CloudstorageKit

class TestCloudstorageKit(unittest.TestCase):
    """Test cases for CloudstorageKit class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CloudstorageKit()
        self.assertIsInstance(instance, CloudstorageKit)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CloudstorageKit()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
