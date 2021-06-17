from fabric import Connection
connection = Connection(host="testcollage619@35.188.29.83", connect_kwargs = {"password":"JBFTAjm4cSwk"})
connection.run("whoami")