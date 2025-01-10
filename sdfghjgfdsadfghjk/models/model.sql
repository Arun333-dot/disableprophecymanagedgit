WITH customers AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.dev', 'customers') }}

)

SELECT *

FROM customers
