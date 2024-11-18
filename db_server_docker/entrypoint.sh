#!/bin/bash

# Start the script to create the DB and user
/usr/config/configure-db.sh &

date
# Start SQL Server
/opt/mssql/bin/sqlservr


