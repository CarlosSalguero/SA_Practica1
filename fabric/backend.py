from fabric import Connection
connection = Connection(host="testcollage619@34.121.11.37", connect_kwargs = {"password":"JBFTAjm4cSwk"})
connection.run("whoami")