#! /bin/sh

psql -c "CREATE DATABASE stock_analytics"
psql stock_analytics -c "CREATE EXTENSION IF NOT EXISTS \"pg_trgm\""