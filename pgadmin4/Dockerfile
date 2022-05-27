FROM dpage/pgadmin4:6.9

COPY config_local.py /pgadmin4/config_local.py

# From https://github.com/postgres/pgadmin4/blob/master/Dockerfile
USER pgadmin

VOLUME /var/lib/pgadmin
EXPOSE 80 443

ENTRYPOINT ["/entrypoint.sh"]