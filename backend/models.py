from pydantic import BaseModel

# Tumor size
# lnAST
# BCLC
# Tumor number
# ALBIgrade
# class_Histologic grade
# class_AFP
# Ishak
# Steatosis grade
# K
# class_Steatosis grade
# AST
# HBsAg
# Height
# MVI

default_features = {
    'bclc': 'BCLC',
    'tumor_number': 'Tumor number',
    'tumor_size': 'Tumor size',
    'k': 'K',
    'ast': 'AST',
    'afp': 'AFP',
    'hbsag': 'HBsAg',
    'albigrade': 'ALBIgrade',
    'histologic_grade': 'Histologic grade',
    'ishak': 'Ishak',
    'steatosis_grade': 'Steatosis grade',
    'bmi': 'BMI',
    'mvi': 'MVI',
}


class PatientData(BaseModel):
    bclc: float | None = None
    tumor_number: float | None = None
    tumor_size: float | None = None
    k: float | None = None
    ast: float | None = None
    afp: float | None = None
    hbsag: float | None = None
    albigrade: float | None = None
    histologic_grade: float | None = None
    ishak: float | None = None
    steatosis_grade: float | None = None
    bmi: float | None = None
    mvi: float | None = None
    


    def dict(self, *args, **kwargs):
        original_dict = super().dict(*args, **kwargs)
        return {default_features[key]: original_dict[key] for key in original_dict if key in default_features.keys()}