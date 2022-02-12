import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
  def test1(self):
      nums = ""
      # cannot have an empty string in the password
      self.assertFalse(check_pwd(nums))


if __name__ == '__main__':
  unittest.main()