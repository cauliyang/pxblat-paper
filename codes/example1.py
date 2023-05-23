from pxblat.server import Server, Client

with Server() as server:
    client = Client()
    client.start()
    # do some stuffs that consuming time
    # and do not need query result,
    # then get query result
    ret = client.get()
