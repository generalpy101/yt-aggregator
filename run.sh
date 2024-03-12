set -e

echo "Running the server"

# Set flask app for migration
export FLASK_APP=api.server.py

# Drop all tables for clean db state
# Uncomment the following line to drop all tables
# flask db downgrade base

# Create all tables
flask db upgrade

# Run the server
python api/server.py
