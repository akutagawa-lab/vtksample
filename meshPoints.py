#!/usr/bin/env python3
''' EVTK sample script '''

import numpy as np
import scipy.constants as const
import scipy
import pyevtk


def main():
    calc_range = 1.0   # 計算範囲 -calc_range から calc_range
    nsamples = 100     # 分割数

    calc_range_x = [-calc_range, calc_range]
    calc_range_y = [-calc_range, calc_range]
    calc_range_z = [-calc_range, calc_range]

    xx = np.linspace(calc_range_x[0], calc_range_x[1], nsamples)
    yy = np.linspace(calc_range_y[0], calc_range_y[1], nsamples)
    #zz = np.linspace(calc_range_z[0], calc_range_z[1], nsamples)
    zz = 0

    # 必ず indexing='ij' を指定する．座標軸が入れ替わらないように
    xxx, yyy, zzz = np.meshgrid(xx, yy, zz, indexing='ij')


    # vtk ファイルの書き出し
    pyevtk.hl.pointsToVTK(
            "./points",  # ファイル名の指定．拡張子は追加される
            xxx, yyy, zzz,      # 各座標軸の座標
            data={      # 格子点上のデータの指定
                'x': xxx,
                },
            )


if __name__ == "__main__":
    main()
