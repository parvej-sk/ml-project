IF  U  R  INTERMEDIATE\\ OR PROFESSIONAL\\ IGNORE\\ this file...

1. create env==>>
conda create -p env python==3.9

2. conda cativate ==>>
conda activate ./env

3. create repo & connect git

4. gitignore & license

5. create requirements.txt ==>>
    pip install --upgrade -r requirements.txt

6. create setup.py ==>>
    python setup.py install


7. create logger & exception


8. create source code/ all components

9. Data ingestion => gather data from Mysql
   MYsql => Utils.py => data_ingestion.py

  (I/p) raw data(df) => data ingestion => train,test [O/p](Artifacts)
                                     
10. Data Transformation ==>>
     train/test => Feature Engineering =>(train_arr/test_arr/ Preprocessor.pkl)

11. Model Training ==>
    (train_arr/test_arr) => Fit Best model => create best model (.PKL)

12. training pipeline..

13. prediction pipeline..




* **********************************

#MLFlow Tracting using dagshub....
MLFLOW_TRACKING_URI=https://dagshub.com/parvej-sk/ml-project.mlflow \
MLFLOW_TRACKING_USERNAME=parvej-sk \
MLFLOW_TRACKING_PASSWORD=************************** \
python script.py