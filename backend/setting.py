import sys, os
from dotenv import load_dotenv
load_dotenv()

ELSTACE_MODEL = os.getenv("ELSTACE_MODEL")
if not ELSTACE_MODEL: raise ValueError("Cannot find the path of EL-STACE model.")

GARSL2_MODEL = os.getenv("GARSL2_MODEL")
if not GARSL2_MODEL: raise ValueError("Cannot find the path of GARSL2_MODEL.")

GARSL2_SCALE = os.getenv("GARSL2_SCALE")
if not GARSL2_SCALE: raise ValueError("Cannot find the path of EL-GARSL2_SCALE .")

# BOXCOX_LAMBDA = {'Age': 1.74738478014072, 
#     'Tumor counts': -0.3972398366097629, 
#     'Tumor size': -0.0006968928479684463, 
#     'WBC': 0.059809461428072, 
#     'HB': 1.9501226150114916, 
#     'PLAT': 0.18669128027144247, 
#     'PTINR': -2.878411727204587, 
#     'ALB': 1.547361563589302, 
#     'Na': 12.341339860045426, 
#     'K': 1.1498564135100853, 
#     'BUN': -0.41882047424173596, 
#     'CR': -0.9526657876954986, 
#     'BILI': -0.11642450009784068, 
#     'ALT': -0.22391386546817416, 
#     'AST': -0.20320821158653263, 
#     'AFP': -0.1608820067511106, 
#     'UpToScore': -0.022737481422181228, 
#     'FIB4': -0.04126664897026074
# }

CUTPOINTS = {
    'Histologic grade': [float('-inf'), 2, 2.5, 3,float('inf')],
    'AFP': [float('-inf'), 7, 10, 20, 200 ,400, float('inf')],
    'Steatosis grade': [float('-inf'),0.001, float('inf')],
}

RISK_THRESHOLD = 0


if __name__ == "__main__":
    print(f"EL-STACE-MODEL: {ELSTACE_MODEL}")