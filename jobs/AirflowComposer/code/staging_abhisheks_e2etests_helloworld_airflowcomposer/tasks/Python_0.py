from staging_abhisheks_e2etests_helloworld_airflowcomposer.utils import *

def Python_0():

    def abc():
        print("Hello world")

    import json
    from datetime import timedelta
    from airflow.operators.python import PythonOperator

    return PythonOperator(task_id = "Python_0", python_callable = abc, show_return_value_in_logs = True)
