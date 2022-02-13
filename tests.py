import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
  def test1(self):
      nums = ""
      # cannot have an empty string in the password
      self.assertFalse(check_pwd(nums))

  def test2(self):
      nums = "8675309"
      # cannot have pwd < 8 characters
      self.assertFalse(check_pwd(nums))

  def test3(self):
      nums = "12345678910111213141516171819202122"
      # cannot have pwd > 20 characters
      self.assertFalse(check_pwd(nums))


if __name__ == '__main__':
  unittest.main()