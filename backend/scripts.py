import numpy as np
import pandas as pd
from pydantic import BaseModel, Field
import logging
from typing import Type
from scipy.stats import boxcox
from setting import RISK_THRESHOLD


logger = logging.getLogger(__name__)


def parse_feature(estimator):
    selected_features = estimator.feature_names_in_
    features = dict()
    for feature in selected_features:
        if "_" not in feature:
            name = feature
            trans = ""
        else:
            details = feature.split("_")
            name = details[1]
            trans = details[0]
        
        if name not in features.keys():
            features[name] = [trans]
        else:
            features[name].append(trans)

    return features


def get_derived_features(df, feature_details, cutpoints):
    feature_df = pd.DataFrame()
    for name, transes in feature_details.items():
        for trans in transes:
            if trans == "": feature_df[name] = df[name]
            elif trans == "class":
                feature_df[f"{trans}_{name}"] = pd.cut(df[name], bins=cutpoints[name], labels=list(range( len(cutpoints[name])-1 )))
            elif trans == "ln":
                feature_df[f"{trans}_{name}"] = df[name].apply(np.log)
            # elif trans == "bc":
            #     feature_df[f"{name}-{trans}"] = boxcox(df[name], lmbda=boxcox_lambda[name])
    return feature_df


def predict(estimator, feature_df, mode="case"):
    preds = pd.Series(estimator.predict(feature_df), name='risk_score').round(2)
    risk_groups = preds.apply(lambda risk_score: "High" if risk_score >=RISK_THRESHOLD else "Low" )
    risk_groups.name = 'risk_group'
    

    survf = estimator.predict_survival_function(feature_df)
    year1_probs = pd.Series(np.asarray([ fn(6) for fn in survf])).round(2)
    year2_probs = pd.Series(np.asarray([ fn(12) for fn in survf])).round(2)
    year3_probs = pd.Series(np.asarray([ fn(18) for fn in survf])).round(2)
    year4_probs = pd.Series(np.asarray([ fn(24) for fn in survf])).round(2)
    # year5_probs = pd.Series(np.asarray([ fn(60) for fn in survf])).round(2)

    results = pd.concat([preds, risk_groups], axis=1).to_dict(orient='records')

    survival_result = pd.concat([
        year1_probs, 
        year2_probs, 
        year3_probs, 
        year4_probs, 
        # year5_probs
    ], axis=1).to_dict(orient='split')['data']

    if mode == "case":
        for idx, result in enumerate(results):
            result['survival_rates'] = survival_result[idx]
            results[idx] = result
    elif mode == "batch":
        for idx, result in enumerate(results):
            result['1_year_survival_rate'] = survival_result[idx][0]
            result['2_year_survival_rate'] = survival_result[idx][1]
            result['3_year_survival_rate'] = survival_result[idx][2]
            result['4_year_survival_rate'] = survival_result[idx][3]
            # result['5_year_survival_rate'] = survival_result[idx][4]
            results[idx] = result

    return results




if __name__ == "__main__":
    print("test")