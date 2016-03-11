
CREATE ROLE adi_data LOGIN PASSWORD 'adi_data';

SELECT pg_terminate_backend(pg_stat_activity.pid)
    FROM pg_stat_activity
    WHERE pg_stat_activity.datname = 'adi_data' AND pid <> pg_backend_pid();

CREATE DATABASE adi_data WITH OWNER adi_data;
