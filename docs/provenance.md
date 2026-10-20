# Source and changes

Insurance Charge Modeling was refactored from the author-supplied Python notebook into a reusable module, a clean demonstration notebook, and focused validation checks. Original files are preserved locally. Embedded notebook outputs were cleared rather than presented as newly reproduced results. Student identifiers, personal phone numbers, source-machine paths, and names from illustrative records are excluded.

New commits describe the actual work done now; original analysis dates are not fabricated.

## Corrections and interpretation

Uses a train-fitted ColumnTransformer and OneHotEncoder instead of reusing LabelEncoder and full-data dummy preparation. Adds a mean-prediction baseline, RMSE, MAE, and residual plots. Coefficients describe association, not causal effects. Synthetic data are designed with known structure; favorable demo scores are not evidence of real-world performance. No insurance eligibility or pricing decisions are implemented.
