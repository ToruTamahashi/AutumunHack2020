FROM mysql:5.7

COPY sql/* /docker-entrypoint-initdb.d/
COPY my.cnf /etc/mysql/my.cnf


CMD ["mysqld"]