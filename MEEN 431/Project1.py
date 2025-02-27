import numpy as np

#define all functons to take in vectors for positions

def ProcCalc(A):
    """Function to find U and V"""

    eigVals, eigVec = np.linalg.eig(A)

    normVec = []
    for vec in eigVec.T:
        norm = np.linalg.norm(vec)
        normVec.append(vec/norm)

    eigenvector_matrix = np.column_stack(normVec)

    return eigenvector_matrix

def RavgCalc(R1, R2):
    """R1, R2 are sympy matrices"""

    Ravg = 0.5*(R1+R2)

    U = (Ravg @ Ravg.T)
    V = (Ravg.T @ Ravg)

    R = V @ U.T

    return R
  
def distanceCalc(GPoint, Bpoint):
    """Cartesian distance from points P, Q, R to h, g, f"""

    res = np.sqrt(((GPoint.x-Bpoint.x)^2)+((GPoint.y-Bpoint.y)^2)+((GPoint.z-Bpoint.z)^2))
    return res


