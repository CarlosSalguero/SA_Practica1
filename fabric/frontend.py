from fabric import Connection

from fabric import Connection

c = Connection(
    host="34.121.11.37",
    user="testcollage619",
    connect_kwargs={
        "key_filename": "./key",
        "passphrase": ""
    },
)

with c.cd("practica2"):

    result = c.run("whoami")
    c.close()

