from pymilvus import MilvusClient
from numpy import random


def create_collection_and_schema(client: MilvusClient) -> None:
    client.create_collection(collection_name="quick_setup", dimension=5)


def insert_data(client: MilvusClient) -> dict:
    data = [
        {
            "id": 0,
            "vector": [
                0.3580376395471989,
                -0.6023495712049978,
                0.18414012509913835,
                -0.26286205330961354,
                0.9029438446296592,
            ],
            "color": "pink_8682",
        },
        {
            "id": 1,
            "vector": [
                0.19886812562848388,
                0.06023560599112088,
                0.6976963061752597,
                0.2614474506242501,
                0.838729485096104,
            ],
            "color": "red_7025",
        },
        {
            "id": 2,
            "vector": [
                0.43742130801983836,
                -0.5597502546264526,
                0.6457887650909682,
                0.7894058910881185,
                0.20785793220625592,
            ],
            "color": "orange_6781",
        },
        {
            "id": 3,
            "vector": [
                0.3172005263489739,
                0.9719044792798428,
                -0.36981146090600725,
                -0.4860894583077995,
                0.95791889146345,
            ],
            "color": "pink_9298",
        },
        {
            "id": 4,
            "vector": [
                0.4452349528804562,
                -0.8757026943054742,
                0.8220779437047674,
                0.46406290649483184,
                0.30337481143159106,
            ],
            "color": "red_4794",
        },
        {
            "id": 5,
            "vector": [
                0.985825131989184,
                -0.8144651566660419,
                0.6299267002202009,
                0.1206906911183383,
                -0.1446277761879955,
            ],
            "color": "yellow_4222",
        },
        {
            "id": 6,
            "vector": [
                0.8371977790571115,
                -0.015764369584852833,
                -0.31062937026679327,
                -0.562666951622192,
                -0.8984947637863987,
            ],
            "color": "red_9392",
        },
        {
            "id": 7,
            "vector": [
                -0.33445148015177995,
                -0.2567135004164067,
                0.8987539745369246,
                0.9402995886420709,
                0.5378064918413052,
            ],
            "color": "grey_8510",
        },
        {
            "id": 8,
            "vector": [
                0.39524717779832685,
                0.4000257286739164,
                -0.5890507376891594,
                -0.8650502298996872,
                -0.6140360785406336,
            ],
            "color": "white_9381",
        },
        {
            "id": 9,
            "vector": [
                0.5718280481994695,
                0.24070317428066512,
                -0.3737913482606834,
                -0.06726932177492717,
                -0.6980531615588608,
            ],
            "color": "purple_4976",
        },
    ]

    res = client.insert(collection_name="quick_setup", data=data)

    return res


def insert_generated_data(client: MilvusClient) -> dict:
    colors = [
        "green",
        "blue",
        "yellow",
        "red",
        "black",
        "white",
        "purple",
        "pink",
        "orange",
        "brown",
        "grey",
    ]
    data = [
        {
            "id": i,
            "vector": [random.uniform(-1, 1) for _ in range(5)],
            "color": f"{random.choice(colors)}_{str(random.randint(1000, 9999))}",
        }
        for i in range(1000)
    ]

    res = client.insert(collection_name="quick_setup", data=data[10:])

    return res


def similarity_search(client: MilvusClient) -> list[list[dict]]:
    query_vectors = [
        [0.041732933, 0.013779674, -0.027564144, -0.013061441, 0.009748648]
    ]

    res = client.search(
        collection_name="quick_setup",  # target collection
        data=query_vectors,  # query vectors
        limit=3,  # number of returned entities
    )

    print(res)
    return res

def drop_collection(client: MilvusClient) -> None:

    client.drop_collection(
        collection_name="quick_setup"
    )



if __name__ == "__main__":
    client = MilvusClient(
        uri="http://127.0.0.1:52070",
    )

    create_collection_and_schema(client=client)
    print(f"insert_data: {insert_data(client=client)}")
    print(f"generated data: {insert_generated_data(client=client)}")
    print(f"Similarity Search: {similarity_search(client=client)}")

    print(drop_collection(client=client))