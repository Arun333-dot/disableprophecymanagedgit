WITH databricks_large AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.rohit', 'databricks_large') }}

),

FlattenSchema_1 AS (

  {#Simplifies the data structure by selecting specific fields from a large dataset.#}
  SELECT 
    id AS id,
    department AS department
  
  FROM databricks_large AS in0

)

SELECT *

FROM FlattenSchema_1
