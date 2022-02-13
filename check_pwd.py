def check_pwd(nums):
    # will return True no matter what
    if nums == "":
        return False
    pwd_length = len(nums)

    if pwd_length < 8:
        # password cannot be less than 8 characters long
        return False
    return True


