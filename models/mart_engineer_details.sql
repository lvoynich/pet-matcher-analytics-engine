{{ config(materialized='table') }}

-- Clean and structure our core engineer staging logs
WITH staging_data AS (
    SELECT 
        UPPER('Lana Voynich') AS engineer_name,
        'Codecademy Data Engineer Track' AS core_foundation,
        72 AS completion_percentage,
        'dbt Core + Snowflake Key-Pair' AS cloud_infrastructure
),

-- Transform metrics to calculate our target outputs
final_analytics AS (
    SELECT 
        engineer_name,
        core_foundation,
        completion_percentage,
        (100 - completion_percentage) AS percentage_to_graduation,
        cloud_infrastructure,
        'Analytics Engineer' AS target_market_title
    FROM 
        staging_data
)

SELECT * FROM final_analytics
