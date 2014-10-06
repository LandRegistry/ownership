export SETTINGS='config.TestConfig'
export APP_NAME="ownership_test"

# Here we'll create a test database, and override the database to the test values.
set +o errexit
createuser -s $APP_NAME
createdb -U $APP_NAME -O $APP_NAME $APP_NAME -T template0
set -e

export DATABASE_URL="postgresql://localhost/$APP_NAME"
