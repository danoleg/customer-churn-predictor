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
![image](https://user-images.githubusercontent.com/31770269/232352621-2189f369-c491-418d-896a-57bb9538c735.png)


3) In Cloud Service Portal open "Add and Manage files" and add WA_Fn-UseC_-Telco-Customer-Churn.csv from /data folder
![image](https://user-images.githubusercontent.com/31770269/232352511-976b63fb-9fc9-4ace-8938-c087447ed627.png)


4) Open "Import files" and import current file to Customers table
![image](https://user-images.githubusercontent.com/31770269/232352526-d56af072-15b4-4654-85a3-8646a6a77618.png)
![Снимок экрана 2023-04-17 в 02 43 36](https://user-images.githubusercontent.com/31770269/232352541-57ef8d19-081d-46df-8292-d29dd1c0155f.png)
![image](https://user-images.githubusercontent.com/31770269/232352545-8726ad39-13a5-4157-bbb7-c7b825ef0ccd.png)


5) Then go to "IntegratedML Tools" and create and train new model with training model name "customer_churn_predictor_tr"
![image](https://user-images.githubusercontent.com/31770269/232352580-422c66a8-7e42-4c73-bc46-38591742c27c.png)
![image](https://user-images.githubusercontent.com/31770269/232352595-49e7602b-4e30-4cff-a407-be2d4653e4d9.png)

5) Go to app again, enter customer data and look to result
![Снимок экрана 2023-04-17 в 03 22 08](https://user-images.githubusercontent.com/31770269/232352644-98643a63-6fb6-4e53-86e4-699dc4136a25.png)
![image](https://user-images.githubusercontent.com/31770269/232352657-84b2547b-8e9e-4bb5-84d3-63857a7f55b5.png)
![image](https://user-images.githubusercontent.com/31770269/232352676-873f29fa-6c0a-4965-ae98-b623a78f7829.png)

