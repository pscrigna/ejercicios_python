"""
The aim of this challenge is, given a dictionary of people's online status,
to count the number of people who are online.

For example, consider the following dictionary:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

In this case, the number of people online is 2.

Write a function named online_count that takes one parameter.
The parameter is a dictionary that maps from strings of names to the
string "online" or "offline", as seen above.

Your function should return the number of people who are online.
"""


import pytest


@pytest.fixture
def dic_test():
    dic = {
        "Peter": "online",
        "Bob": "offline",
        "Susan": "offline",
    }
    return dic


def test_ok_online_count(dic_test):
    val = online_count(dic_test)
    assert val == 1


def test_online_count():
    val = online_count(statuses)
    assert val == 2


def online_count(status_users):
    counter = 0
    for status in status_users.values():
        if status == "online":
            counter += 1
    return counter


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


if __name__ == "__main__":
    print(f'online users : {online_count(statuses)}')
