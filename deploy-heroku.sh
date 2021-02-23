make build
make start-prod
heroku container:login
heroku container:push web -a balbol
heroku container:release web -a balbol
heroku ps --app balbol
heroku open --app balbol

# get logs
# heroku logs --tail -a balbol

# access docker container
# docker exec -it <container> sh
# docker exec -tiu postgres balbol_db psql