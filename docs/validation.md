# Execution and validation

Executed with Python 3.12 using the versions pinned in requirements.txt. Program run completed successfully. Generated notebook cells passed Python syntax compilation; the notebook wrapper calls the same validated module. Full notebook execution in a separate Jupyter kernel was not performed.

```text
test_complete_synthetic_run (test_analysis.InsuranceTest.test_complete_synthetic_run) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.261s

OK
```

Input/output data were checked for required fields, finite values, and appropriate synthetic-versus-supplied provenance. Output files contain aggregate metrics or non-personal examples; row-level clinical predictions are not published.
