from pxblat.server import Server, Client

server = Server()
client = Client()
client.start()
# do some stuffs that consuming time
# and do not need query result, then get query result
result = client.get()
# do other stuffs that need query result
# close server when needs
server.stop()
