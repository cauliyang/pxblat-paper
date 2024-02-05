from pxblat import Server
from pxblat import Client

client = Client(
    host="localhost",
    port=65000,
    seq_dir="ref/",
    min_score=20,
    min_identity=90,
)

with Server(host, port, two_bit, can_stop=True, step_size=5) as server:
    server.wait_ready()
    result1 = client.query("ATCG")
    result2 = client.query("AtcG")
    result3 = client.query("test_case1.fa")
    result4 = client.query(["ATCG", "ATCG"])
    result5 = client.query(["test_case1.fa"])
    result6 = client.query(["cgTA", "test_case1.fa"])
    print(result3[0]) # print result