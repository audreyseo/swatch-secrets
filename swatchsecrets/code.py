# A default dictionary for encoding information
# into stitches


# 4 bits seemed like the sweet spot for the amount of information you could encode
coding = {
    " ": "0000", # not zero because having space be 1111 would be very odd -- assuming 0s are knit stitches and 1s are purls
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    ".": "1010",
    "mm": "1011",
    "sts": "1100",
    "rows": "1101",
    "co": "1110",
    "0": "1111"
}

decoding = {v: k for k,v in coding.items()}

def flipBits(encoded: str):
    s = ""
    for c in encoded:
        if c == "0":
            s += "1"
            pass
        elif c == "1":
            s += "0"
            pass
        else:
            s += c
        pass
    return s


def chunkUp(s, chunkBy: int):
    if chunkBy == 0:
        return s
    chunked = ""
    for i in range(0, len(s), 4):
        chunked += " " + s[i:min(i + 4, len(s))]
        pass
    return chunked.strip()
