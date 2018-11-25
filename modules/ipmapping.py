import socket

results = []
def get_ip(name):
    res = socket.getaddrinfo(name[0], 80)
    for each in res:
        if(len(each)<6 and len(each)>4):
            results.append(each[4])

    return set(results)