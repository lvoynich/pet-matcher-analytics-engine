{{ config(materialized='table') }}

-- Step 1: Staging our raw institutional data assets
WITH staging_schools AS (
    SELECT 'Oakridge Elementary' AS school_name, 'Primary' AS school_level, 450 AS student_count, 'Parents must sign out at the main office' AS pickup_policy
    UNION ALL
    SELECT 'Bayview High', 'High', 1200, NULL
    UNION ALL
    SELECT 'Sunset Middle', 'Middle', 680, NULL
),

-- Step 2: Transforming data using business logic (Your getters/setters equivalent)
final_catalogue AS (
    SELECT
        MD5(school_name) AS school_integration_key,
        school_name,
        school_level,
        student_count,
        -- Handle data validation dynamically
        CASE 
            WHEN student_count >= 1000 THEN 'Large Tier'
            WHEN student_count >= 500 THEN 'Medium Tier'
            ELSE 'Small Tier'
        END AS school_size_classification,
        -- Coalesce missing attributes for high/middle schools
        COALESCE(pickup_policy, 'No explicit primary pickup policy defined') AS operational_policy,
        CURRENT_TIMESTAMP() AS record_loaded_at
    FROM 
        staging_schools
)

SELECT * FROM final_catalogue
