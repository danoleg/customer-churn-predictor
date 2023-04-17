import iris
from datetime import datetime

from flask import Flask, render_template, request, redirect
from flask_material import Material


app = Flask(__name__)
Material(app)

app.config['iris_host'] = ""
app.config['iris_port'] = 1972
app.config['iris_namespace'] = "USER"
app.config['iris_username'] = "SQLAdmin"
app.config['iris_password'] = ""
app.config['connection'] = None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/config', methods=['GET', 'POST'])
def config():

    data = {
        "hostname": app.config['iris_host'],
        "port": int(app.config['iris_port']),
        "user": app.config['iris_namespace'],
        "namespace": app.config['iris_username'],
        "password": app.config['iris_password']
    }

    if request.method == 'POST':
        app.config['iris_host'] = request.form['hostname']
        app.config['iris_port'] = request.form['port']
        app.config['iris_namespace'] = request.form['user']
        app.config['iris_username'] = request.form['namespace']
        app.config['iris_password'] = request.form['password']

        try:

            app.config['connection'] = conn = iris.connect(
                app.config['iris_host'],
                int(app.config['iris_port']),
                app.config['iris_namespace'],
                app.config['iris_username'],
                app.config['iris_password']
            )

            cur = conn.cursor()

            cur.execute("""DROP TABLE IF EXISTS Customer""")
            print("DROPPED", flush=True)

            cur.execute("""CREATE TABLE IF NOT EXISTS Customer (
                customer_id VARCHAR(256),
                gender VARCHAR(256),
                senior_citizen INT,
                partner VARCHAR(3),
                dependents VARCHAR(3),
                tenure INT,
                phone_service VARCHAR(3),
                multiple_lines VARCHAR(256),
                internet_service VARCHAR(256),
                online_security VARCHAR(256),
                online_backup VARCHAR(256),
                device_protection VARCHAR(256),
                tech_support VARCHAR(256),
                streaming_tv VARCHAR(256),
                streaming_movies VARCHAR(256),
                contract VARCHAR(256),
                paperless_billing VARCHAR(256),
                payment_method VARCHAR(256),
                monthly_charges FLOAT,
                total_charges FLOAT,
                churn VARCHAR(3)
            )""")
            cur.close()
            print("CREATED", flush=True)

            return redirect('/form')
        except Exception as e:
            return str(e)

    return render_template('config.html', data=data)


@app.route('/form', methods=['GET', 'POST'])
def form():

    # Create model demo predicting (churn) from SQLUser.Customer
    # Train model demo as demo_trained

    # cur.execute("SELECT PREDICT('churn') AS predicred_churn FROM %s")

    conn = app.config['connection']
    prediction_churn_val = None
    prediction_churn_prob = None

    if not conn:
        return redirect('/')

    if request.method == 'POST':
        timestamp = int(round(datetime.now().timestamp()))

        insert_query = f"""INSERT INTO Customer VALUES 
        ('{timestamp}',
        '{request.form['gender']}',
        {request.form['senior_citizen']},
        '{request.form['partner']}',
        '{request.form['dependents']}',
        {request.form['tenure']},
        '{request.form['phone_service']}',
        '{request.form['multiple_lines']}',
        '{request.form['internet_service']}',
        '{request.form['online_security']}',
        '{request.form['online_backup']}',
        '{request.form['device_protection']}',
        '{request.form['tech_support']}',
        '{request.form['streaming_tv']}',
        '{request.form['streaming_movies']}',
        '{request.form['contract']}',
        '{request.form['paperless_billing']}',
        '{request.form['payment_method']}',
        {request.form['monthly_charges']},
        {request.form['total_charges']},
        'No')
        """

        cur = conn.cursor()
        cur.execute(insert_query)
        cur.execute("""SELECT TOP(1) PREDICT(customer_churn_predictor_m use customer_churn_predictor_tr) as prediction,
          PROBABILITY(customer_churn_predictor_m use customer_churn_predictor_tr for 'Yes') as probability_churn FROM
          SQLUser.Customer order by customer_id DESC""")
        prediction_churn = cur.fetchall()
        cur.close()

        prediction_churn_val = prediction_churn[0][0]
        prediction_churn_prob = round(round(float(prediction_churn[0][1]), 2) * 100, 2)

        print(prediction_churn[0], flush=True)

    return render_template(
        'form.html',
        prediction_churn_val=prediction_churn_val,
        prediction_churn_prob=prediction_churn_prob
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8011)
