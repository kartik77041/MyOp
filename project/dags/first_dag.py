# try:
#     from airflow import DAG
#     from airflow.operators.python_operator import python_operator
#     from airflow.operators.bash_operator import BashOperator
#     from datetime import datetime
#     from datetime import timedelta
#     import pandas as pd

#     print("All Dag modules are ok ......")
# except Exception as e:
#     print("Error  {} ".format(e))


# def first_function_execute(*args, **kwargs):
#     variable = kwargs.get("name", "Did not get the key")
#     print("Hello world: {}".format(variable))
#     return "Hello World" + variable

# # with DAG(
# #         dag_id="first_dag",
# #         schedule_interval="*/2 * * * *",
# #         default_args={
# #             "owner": "airflow",
# #             "retries": 1,
# #             "retry_delay": timedelta(minutes=5),
# #             "start_date": datetime(2021, 1, 1),
# #         },
# #         catchup=False) as f:

# #     first_function_execute = PythonOperator(
# #         task_id="first_function_execute",
# #         python_callable=first_function_execute,
# #         op_kwargs= {"name":"kartik rajput"}
# #     )

# with DAG(
#         dag_id="first_dag",
#         schedule_interval="*/2 * * * *",
#         default_args={
#             "owner": "airflow",
#             "retries": 1,
#             "retry_delay": timedelta(minutes=10),
#             "start_date": datetime(2021, 1, 1),
#         },
#         catchup=False) as f:

#     execute_script_task = BashOperator(
#         task_id="execute_script_task",
#         bash_command= 'C:/Users/hp/Desktop/office_work/Apache_Airflow_project/project/dags/script.py'
#     )

# from airflow import DAG
# from airflow.operators.bash_operator import BashOperator
# from datetime import datetime, timedelta

# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'start_date': datetime(2023, 2, 15),
#     'retries': 0,
# }

# test_dag = DAG(
#     'test_bash_script_dag',
#     default_args=default_args,
#     schedule_interval=timedelta(minutes=5)
# )

# # Define the BashOperator task
# bash_task = BashOperator(
#     task_id='bash_task_execute_script',
#     bash_command='./test_script.sh',
#     dag=test_dag
# )

# Set task dependencies

from airflow import DAG

from airflow.operators.bash_operator import BashOperator

from datetime import datetime, timedelta



default_args = {

    'owner': 'airflow',

    'depends_on_past': False,

    'start_date': datetime(2024, 1, 25),

    'retries': 0,
}



test_dag = DAG(

    'bashscript',

    default_args=default_args,

    schedule_interval= timedelta(hours=3),

)



# Define the BashOperator task

bash_task = BashOperator(

    task_id='bash_task_execute_script',

    bash_command="./test_script.sh",
    env={'name': 'kartik'},  

    dag=test_dag

)



bash_task