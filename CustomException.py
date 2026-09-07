class UserExistException(Exception):
    pass
class NoExistBookException(Exception):
    pass
class NoExistMemberException(Exception):
    pass
class NotEnoughBookException(Exception):
    pass
# 연체자가 있는 경우 구현 이곳
class AlreadyBorrowedBookException(Exception):
    pass
class NoBookException(Exception):
    pass