"""Retrospective charges regression, not premium-setting or eligibility software."""
import argparse
from common import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

def run(input_path,output='outputs'):
    d=pd.read_csv(input_path).drop_duplicates();numeric=['age','bmi','children'];categorical=['gender','smoker','region']
    if missing:=set(numeric+categorical+['charges'])-set(d):raise ValueError(f'Missing columns: {sorted(missing)}')
    for c in numeric+['charges']:d[c]=pd.to_numeric(d[c],errors='coerce')
    d=d.dropna(subset=['charges']);x=d[numeric+categorical];y=d.charges
    xt,xv,yt,yv=train_test_split(x,y,test_size=.2,random_state=42)
    model=Pipeline([('preprocess',preprocessor(numeric,categorical)),('regression',LinearRegression())]);model.fit(xt,yt);pred=model.predict(xv)
    baseline=DummyRegressor(strategy='mean').fit(xt,yt).predict(xv)
    report={'data_kind':'synthetic demonstration' if Path(input_path).name.startswith('synthetic_') else 'user-supplied data','rows':len(d),'training_rows':len(xt),'test_rows':len(xv),'r2':float(r2_score(yv,pred)),'rmse':float(np.sqrt(mean_squared_error(yv,pred))),'mae':float(mean_absolute_error(yv,pred)),'baseline_rmse':float(np.sqrt(mean_squared_error(yv,baseline))),'test_predictions_finite':bool(np.isfinite(pred).all())}
    import matplotlib;matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    out=Path(output);out.mkdir(parents=True,exist_ok=True)
    fig,ax=plt.subplots(1,2,figsize=(10,4),layout='constrained');ax[0].scatter(pred,yv-pred,s=10,alpha=.5);ax[0].axhline(0,color='black');ax[0].set(xlabel='Predicted charge',ylabel='Residual',title='Held-out residuals');from scipy import stats;stats.probplot(yv-pred,plot=ax[1]);fig.suptitle('SYNTHETIC DEMONSTRATION' if report['data_kind'].startswith('synthetic') else 'Charge-model diagnostics');fig.savefig(out/'diagnostics.svg');plt.close(fig)
    return save_report(output,report)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--input',default='data/synthetic_insurance.csv');p.add_argument('--output',default='outputs');a=p.parse_args();print(json.dumps(run(a.input,a.output),indent=2))
