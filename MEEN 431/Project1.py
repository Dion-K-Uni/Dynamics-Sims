import sympy as sp
from sympy import matrix 

#define all functons to take in vectors for positions

def ProcCalc(A):
    """Function to find U and V"""
    
    eVals = A.eigenvals()
    eVec = A.eigenvects()

    normVec = []
    for _, eig_vecs in eVec:
        for vec in eig_vecs:
            norm = vec.norm()
            normVec.append(vec / norm)

    eigenvector_matrix = sp.Matrix.vstack(*normVec)

def RavgCalc(R1, R2):
    """R1, R2 are sympy matrices"""

    Ravg = 0.5*(R1+R2)

    U = (Ravg*sp.transpose(Ravg))
    V = (sp.transpose(Ravg)*Ravg)

    R = V*sp.transpose(U)

    return R
  
def distanceCalc(GPoint, Bpoint):
    """Cartesian distance from points P, Q, R to h, g, f"""

    res = sp.sqrt(((GPoint.x-Bpoint.x)^2)+((GPoint.y-Bpoint.y)^2)+((GPoint.z-Bpoint.z)^2))
    return res


