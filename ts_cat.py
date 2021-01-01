import glob

with open("./ts_cat.txt", mode='w') as txt:

    files = glob.glob("./*.ts")
    lines = [f"file '{line}'" for line in files]
    txt.write("\n".join(lines))
