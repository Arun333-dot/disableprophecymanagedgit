from airflow.decorators import task

db_pipeline_id_to_path_dict = {
    "pipelines/customers_orders": "dbfs:/FileStore/prophecy/artifacts/staging/cp/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/customers_orders-1.0-py3-none-any.whl", 
    "pipelines/farmers-markets-irs": "dbfs:/FileStore/prophecy/artifacts/staging/cp/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/farmers_markets_irs-1.0-py3-none-any.whl", 
    "pipelines/join_agg_sort": "dbfs:/FileStore/prophecy/artifacts/staging/cp/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/join_agg_sort-1.0-py3-none-any.whl", 
    "pipelines/json-read": "dbfs:/FileStore/prophecy/artifacts/staging/cp/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/json_read-1.0-py3-none-any.whl", 
    "pipelines/report_top_customers": "dbfs:/FileStore/prophecy/artifacts/staging/cp/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/report_top_customers-1.0-py3-none-any.whl"
}


def task_wrapper(task_id):

    def decorator(func):

        @task(task_id = task_id)
        def wrapper(*args, **context):
            ## running the actual method.
            return func(*args, **context).execute(context)

        return wrapper

    return decorator

pipeline_package_name = {
    "pipelines/json-read": "json-read", 
    "pipelines/join_agg_sort": "join_agg_sort", 
    "pipelines/customers_orders": "customers_orders", 
    "pipelines/report_top_customers": "report_top_customers", 
    "pipelines/farmers-markets-irs": "farmers-markets-irs"
}
