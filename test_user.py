from  user import User
import pytest


def test_user_john():
    uname = 'john'
    eml = 'john.winkelman@yahoo.com'
    pwd = 'pwd'
    usr = User(uname, eml, pwd)
    assert usr.getUsername() == uname
    assert usr.getEmail() == eml
    assert usr.getPassword() == pwd

