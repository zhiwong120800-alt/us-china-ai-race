"""Approximate colour-vision simulations for the US/China chart palette.

These matrices are simple colour-vision approximations, NOT a clinical
diagnosis or substitute for a manual browser/CVD audit. Do not use colour
as the sole indicator: country names, model data tables and numeric labels
remain available independently.
"""
from math import sqrt

US=(40,109,183)   # #286DB7
CN=(213,93,54)    # #D55D36
BG=(250,249,245)  # #FAF9F5
M={
"protanopia":((.567,.433,0),(.558,.442,0),(0,.242,.758)),
"deuteranopia":((.625,.375,0),(.70,.30,0),(0,.30,.70)),
"tritanopia":((.95,.05,0),(0,.433,.567),(0,.475,.525))
}
def apply(rgb,m):
    return [round(sum(a*b for a,b in zip(row,rgb))) for row in m]
def distance(a,b):
    return sqrt(sum((x-y)**2 for x,y in zip(a,b)))
def luminance(rgb):
    seq=[v/255 for v in rgb]
    linear=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in seq]
    return .2126*linear[0]+.7152*linear[1]+.0722*linear[2]
def contrast(a,b):
    x,y=sorted((luminance(a),luminance(b)),reverse=True)
    return (x+.05)/(y+.05)
def main():
    for name,mat in M.items():
        us,cn=apply(US,mat),apply(CN,mat)
        d=distance(us,cn)
        print(name,"US",us,"CN",cn,"distance",round(d,1))
        assert d>80, f"National chart colours insufficiently distinct in {name} approximation"
    assert contrast(US,BG)>=4.5, "US small coloured labels lack contrast"
    assert contrast(CN,BG)>=3.0, "China large serif heading lacks minimum 3:1 contrast"
    print("PASS: series remain distinguishable in three approximate CVD transforms; small US text and large China heading meet their respective contrast thresholds")
if __name__=="__main__":
    main()
