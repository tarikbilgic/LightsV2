
def scaling(level, r, g, b):
    r = int(r * level / 100)
    g = int(g * level / 100)
    b = int(b * level / 100)
    return r, g, b


if __name__ == "__main__":
    print(scaling(50, 200, 100, 50))     # expect (100, 50, 25)
    print(scaling(100, 200, 100, 50))    # expect (200, 100, 50)
    print(scaling(36.45, 255, 0, 0))     # expect about (92, 0, 0)