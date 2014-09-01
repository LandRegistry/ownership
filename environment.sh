export DATABASE_URL='postgresql://localhost/ownership'
export SETTINGS='config.DevelopmentConfig'

set +o errexit
createuser -s ownership
createdb -U ownership -O ownership ownership -T template0
