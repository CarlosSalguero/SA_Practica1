from fabric import Connection

from fabric import Connection

c = Connection(
    host="34.121.11.37",
    user="testcollage619",
    connect_kwargs={
        "key_filename": "./ssh",
        "passphrase": ""
    },
)

with c.cd("/"):

    result = c.run("ls")
    c.close()
