from fabric import Connection

from fabric import Connection

c = Connection(
    host="34.121.11.37",
    user="testcollage619",
    connect_kwargs={
        "key_filename": "/home/testcollage619/.ssh/",
        "passphrase": ""
    },
)

c.run("whoami")
