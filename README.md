# Customer churn predictor

This application is an example of using IRIS Cloud SQL and integrated ML to solve customer churn problems.

As an example, the application uses a demo dataset of telecommunications company clients from https://www.kaggle.com/datasets/blastchar/telco-customer-churn.

To start, use the command
```
> docker-compose up --build
```

And open http://127.0.0.1:8011/

1) Open your Cloud Service Portal and create the new Deployment
2) Go to configuration page in the app and set your deployment credentials
3) In Cloud Service Portal open "Add and Manage files" and add WA_Fn-UseC_-Telco-Customer-Churn.csv from /data folder
4) Open "Import files" and import current file to Customers table
5) Then go to "IntegratedML Tools" and create and train new model with training model name "customer_churn_predictor_tr"
5) Go to app again, enter customer data and look to result