export DATABASE_URL='postgresql://localhost/ownership'

set +o errexit
createuser -s ownership
createdb -U ownership -O ownership ownership -T template0
