import pickle



with open("./data/006-boxcox-lmbdas.pkl", "rb") as f:
    boxcox_lambda = pickle.load(f)

print(boxcox_lambda)