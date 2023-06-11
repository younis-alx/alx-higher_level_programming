#!/usr/bin/python3
def multiple_returns(res):
    if res == "":
        return (0, None)
    return (len(res), res[0])
