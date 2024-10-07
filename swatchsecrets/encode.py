from swatchsecrets.code import coding, flipBits, chunkUp
import re

def generatePattern(needleSize: int, castOn: int, rows: int, selvageStitches: int = 0, code=coding, startOnWS: bool = True, chunkBy: int = 0):
    def encode(s):
        assert s in coding, f"{s} not in coding: {coding}"
        return coding[s]

    def encodeList(strs):
        return "".join([encode(s) for s in strs])

    def padOut(s, padTo: int, padder="0"):
        return s + (padder * (padTo - len(s)))
    # needle size should be in terms of 10 mu-meters, i.e., 1 = .01 mm
    # this avoids silly float business

    strSize = str(needleSize)
    assert(len(strSize) > 2)
    strSize = strSize[0:-2] + "." + strSize[-2:]
    strSize = re.sub(r"0+$", "", strSize)
    if (strSize.endswith(".")):
        strSize = strSize[:-1]
    print(strSize)

    needleSizeParts = [c for c in strSize] + ["mm"]

    castOnParts = ["co", " "] + [c for c in str(castOn)] + ["sts"]

    rowParts = [c for c in str(rows)] + [" ", "rows"]
    stitchParts = [c for c in str(castOn - (selvageStitches * 2))] + [" ", "sts"]

    needleSizeStr = encodeList(needleSizeParts)
    castOnStr = encodeList(castOnParts)
    rowStr = encodeList(rowParts)
    stitchStr = encodeList(stitchParts)

    maxLen = max(len(needleSizeStr), len(castOnStr), len(rowStr), len(stitchStr))

    width = castOn - 2 * selvageStitches

    needleSizePadded = padOut(needleSizeStr, width)
    castOnPadded = padOut(castOnStr, width)
    rowPadded = padOut(rowStr, width)
    stitchPadded = padOut(stitchStr, width)

    def sideify(s, isRightSide: bool):
        if isRightSide:
            return chunkUp(s, chunkBy)[::-1]
        return flipBits(chunkUp(s, chunkBy))

    needleSizeFinal = sideify(needleSizePadded, not startOnWS)
    castOnFinal = sideify(castOnPadded, startOnWS)

    rowOnRS = rows % 2 == 1 if startOnWS else rows % 2 == 0


    rowFinal = sideify(rowPadded, rowOnRS)
    stitchFinal = sideify(stitchPadded, not rowOnRS)


    print(needleSizeFinal)
    print(castOnFinal)
    print(f"{rows} rows of stockinette stitch")
    print(rowFinal)
    print(stitchFinal)







    pass


if __name__ == "__main__":
    generatePattern(375, 21, 10)
    generatePattern(400, 21, 26)
    generatePattern(350, 27, 34, selvageStitches=2, startOnWS=False, chunkBy=4)
    pass
