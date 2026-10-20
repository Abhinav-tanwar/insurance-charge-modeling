import sys,unittest,tempfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from analysis import run
class InsuranceTest(unittest.TestCase):
 def test_complete_synthetic_run(self):
  root=Path(__file__).resolve().parents[1]
  with tempfile.TemporaryDirectory() as out:
   report=run(root/'data/synthetic_insurance.csv',out)
   self.assertEqual(report['data_kind'],'synthetic demonstration');self.assertEqual(report['training_rows']+report['test_rows'],report['rows']);self.assertTrue(report['test_predictions_finite']);self.assertLess(report['rmse'],report['baseline_rmse'])
if __name__=='__main__':unittest.main()
