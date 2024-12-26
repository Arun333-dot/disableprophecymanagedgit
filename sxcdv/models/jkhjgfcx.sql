WITH databricks_large AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.rohit', 'databricks_large') }}

)

SELECT *

FROM databricks_large
