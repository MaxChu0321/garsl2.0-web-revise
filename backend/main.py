import pandas as pd
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
import joblib
import pickle
import logging
from setting import ELSTACE_MODEL, CUTPOINTS,GARSL2_MODEL,GARSL2_SCALE
from scripts import parse_feature, get_derived_features, predict
from models import PatientData

# Initial
## setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
# get root logger
logger = logging.getLogger(__name__)
logger.info("Logging...")

# logger.info("Import EL-STACE model...")
# estimator = joblib.load(ELSTACE_MODEL)

# logger.info("Get EL-STACE features...")
# feature_details = parse_feature(estimator)

logger.info("Import GARSL2 model...")
estimator = joblib.load(GARSL2_MODEL)

logger.info("Get GARSL features to scale...")
feature_scale = parse_feature(estimator)

logger.info("Get GARSL features...")
feature_details = parse_feature(estimator)

logger.info("Initial API...")
app = FastAPI()



# CORS
origins = [
    "*",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info("Initialization complete.")


# Views
@app.get("/api/test")
def test():
    return feature_details

@app.post("/api/submit/case")
def submit(data: PatientData):
    print("API Called")
    print("PatientData:", data.dict())
    # 打印 feature_details 的键
    print("feature_details keys:", feature_details.keys())

    data_df = pd.DataFrame([data.dict()])[feature_details.keys()].astype('float')
    feature_df = get_derived_features(data_df, feature_details, CUTPOINTS)
    print(feature_df)
    print(estimator.feature_names_in_)
    results = predict(estimator, feature_df[estimator.feature_names_in_])
    return results

@app.post("/api/submit/batch")
def submit(file: UploadFile):
    try:
        data_df = pd.read_excel( BytesIO(file.file.read()) )[feature_details.keys()].astype('float')
        feature_df = get_derived_features(data_df, feature_details, CUTPOINTS)
        results = predict(estimator, feature_df[estimator.feature_names_in_], mode="batch")

        results_df = pd.DataFrame(results)
        excel_file = BytesIO()
        results_df.to_excel(excel_file, index=False)
        excel_file.seek(0)
        response = StreamingResponse(excel_file, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response.headers["Content-Disposition"] = "attachment; filename=results.xlsx"

        return response
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))