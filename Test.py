# -*- coding: utf-8 -*-

import sys
from GDSII_Director import GDSII_Director

def main():

    shotRank = [0,1,2]
    G = GDSII_Director()
    
    xy = G.drawCircle(50,8)
    tmp = G.addCell('d50_',xy,shotRank)
    tmp = G.addArray(tmp,500,500,60,400)
    G.addCellRef('main',tmp,[[0,0],[100000,0],[200000,0]])    
    
    xy = G.drawCircle(70,8)
    tmp = G.addCell('d70_',xy,shotRank)
    tmp = G.addArray(tmp,500,500,60,400)
    G.addCellRef('main',tmp,[[0,300000],[100000,300000],[200000,300000]])    
    
    xy = G.drawCircle(90,8)
    tmp = G.addCell('d90_',xy,shotRank)
    tmp = G.addArray(tmp,500,500,60,400)
    G.addCellRef('main',tmp,[[0,600000],[100000,600000],[200000,600000]])
    
    xy = G.drawRectangle(200,50000)
    tmp = G.addCell('w200_',xy,[0])
    tmp = G.addArray(tmp,800,1,62,1)
    G.addCellRef('main',tmp,[[-135000,750000]])
    
    G.writeFile('Test.gds')
    
if __name__ == '__main__':
    main()