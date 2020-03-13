from mcstatus import MinecraftServer

# If you know the host and port, you may skip this and use MinecraftServer("example.org", 1234)
server = MinecraftServer("gaymerlads.aternos.me")

# 'status' is supported by all Minecraft servers that are version 1.7 or higher.
status = server.status()
print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))

# 'query' has to be enabled in a servers' server.properties file.
# It may give more information than a ping, such as a full player list or mod information.
query = server.query()
print("The server has the following players online: {0}".format(", ".join(query.players.names)))
