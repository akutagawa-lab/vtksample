#!/usr/bin/env python3

import numpy as np
import scipy.constants as const
import scipy
import pyevtk


def main():
    calc_range = 1.0
    nsamples = 200
    k = 1/(4 * const.pi * const.epsilon_0)

    charge = [
            {'q': -1.0, 'px': -0.2, 'py': 0.0, 'pz': 0.0},
            {'q':  1.0, 'px':  0.2, 'py': 0.0, 'pz': 0.0},
            ]

    calc_range_x = [-calc_range, calc_range]
    calc_range_y = [-calc_range, calc_range]
    calc_range_z = [-calc_range, calc_range]

    xx = np.linspace(calc_range_x[0], calc_range_x[1], nsamples)
    yy = np.linspace(calc_range_y[0], calc_range_y[1], nsamples)
    zz = np.linspace(calc_range_z[0], calc_range_z[1], nsamples)

    xxx, yyy, zzz = np.meshgrid(xx, yy, zz, indexing='ij')

    potential = np.zeros_like(xxx)
    E_x = np.zeros_like(xxx)
    E_y = np.zeros_like(yyy)
    E_z = np.zeros_like(zzz)

    for ch in charge:
        print(ch)
        dx = xxx - ch['px']
        dy = yyy - ch['py']
        dz = zzz - ch['pz']
        r2 = dx ** 2 + dy ** 2 + dz ** 2
        r = np.sqrt(r2)
        a_V = k * ch['q'] / r
        potential = potential + a_V

        a_E = k * ch['q'] / r2
        E_x = E_x + a_E * dx / r
        E_y = E_y + a_E * dy / r
        E_z = E_z + a_E * dz / r

    print(f"{dx.shape}")

    pyevtk.hl.gridToVTK(
            "./structured",
            xx, yy, zz,
            pointData={
                'potential': potential,
                'efield': (E_x, E_y, E_z),
                },
            )
    
if __name__ == "__main__":
    main()
