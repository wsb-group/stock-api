import pytest
from user import User
from users import Users



def test_addJohn():
    ''' adding a single user '''
    u = User('john', 'john.winkelman@yahoo.com', 'pwd')
    users = Users()
    users.addUser(u)
    myUser = users.getUser('john.winkelman@yahoo.com')
    assert u == myUser
    assert u.getEmail() == 'john.winkelman@yahoo.com'

def test_add_users():
    usr1 = User("a", "a@pb.com", "aa")
    usr2 = User("b", "b@pb.com", "bb")
    usr3 = User("c", "c@pb.com", "cc")
    users = Users()
    users.addUser(usr1)
    users.addUser(usr2)
    users.addUser(usr3)
    usr4 = users.getUser("a@pb.com")
    assert usr1 == usr4

