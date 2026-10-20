"""Generate synthetic demo inputs. These are not recovered original records."""
from pathlib import Path
import numpy as np,pandas as pd
rng=np.random.default_rng(42);root=Path(__file__).resolve().parents[1];n=1200
age=rng.integers(18,65,n);bmi=rng.normal(30,5,n).clip(16,52);children=rng.integers(0,6,n);smoker=rng.choice(['yes','no'],n,p=[.2,.8]);region=rng.choice(['northeast','northwest','southeast','southwest'],n)
charges=(2200+220*age+240*bmi+350*children+22000*(smoker=='yes')+rng.normal(0,3500,n)).clip(500)
d=pd.DataFrame({'age':age,'gender':rng.choice(['female','male'],n),'bmi':np.round(bmi,2),'children':children,'smoker':smoker,'region':region,'charges':np.round(charges,2)})
d.to_csv(root/'data/synthetic_insurance.csv',index=False)
print('Created 1200 synthetic insurance demonstration records (seed=42).')
