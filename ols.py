import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

model = sm.OLS(simulated_strain_measurements,p.T)
fit_outcome = model.fit()
