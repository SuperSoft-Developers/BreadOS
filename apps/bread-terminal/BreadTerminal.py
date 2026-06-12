while True:
    cmd = input("bread@os:$ ")

    if cmd == "exit":
        break

    import os
    os.system(cmd)
