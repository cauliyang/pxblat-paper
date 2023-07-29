from pxblat import Server
from pxblat import Client

client = Client(
    host="localhost",
    port=65000,
    seq_dir="ref/",
    min_score=20,
    min_identity=90,
)

server_option = Server.create_option().build()
with Server(
    host="localhost",
    port=65000,
    two_bit="ref/reference.2bit",
    option=server_option
) as server:
    work()  # work that consumes time
    server.wait_for_ready()
    result1 = client.query("ATCG")
    result2 = client.query("AtcG")
    result3 = client.query(["ATCG", "ATCG"])
    result4 = client.query(["cgTA", "fasta.fa"])

    for hsp in result1.hsps:
        print(f"{hsp}")
