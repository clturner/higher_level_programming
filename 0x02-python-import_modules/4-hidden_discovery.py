#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dir(hidden_4)
    for i in dir(hidden_4):
        result = i.startswith('_')
        if result is True:
            continue
        else:
            print(i)
