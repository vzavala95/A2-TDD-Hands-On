def check_pwd(nums):
    # will return True no matter what
    value = True
    pwd_length = len(nums)
    has_upper = any(x.isupper() for x in nums)
    has_lower = any(y.islower() for y in nums)
    has_digit = any(z.isdigit() for z in nums)

    if nums == "":
        value = False

    if pwd_length < 8:
        # password cannot be less than 8 characters long
        value = False

    if pwd_length > 20:
        # password length cannot exceed 20 characters
        value = False
    if not has_upper:
        value = False
    if not has_lower:
        value = False
    if not has_digit:
        value = False
    if value:
        return True


