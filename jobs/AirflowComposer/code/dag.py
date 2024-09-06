import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from staging_abhisheks_e2etests_helloworld_airflowcomposer.tasks import DatabricksPipeline_1, Python_0
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "staging_abhisheks_e2etests_HelloWorld_AirflowComposer", 
    schedule_interval = None, 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.today('UTC'), 
    catchup = False, 
    max_active_runs = 1
) as dag:
    Python_0_op = Python_0()
    DatabricksPipeline_1_op = DatabricksPipeline_1()
    Python_0_op >> DatabricksPipeline_1_op
