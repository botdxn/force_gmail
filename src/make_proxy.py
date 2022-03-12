from fp.fp import FreeProxy

def make_proxy():
    print("FUNC make_proxy STARTED")
    while True:
        try:
            print("Getting proxy...")
            proxy = FreeProxy(timeout=1, rand=True).get()
            print(f"Got proxy: {proxy}")
        except Exception as e:
            print(f"(make_proxy:FreeProxy): {e}")
            continue
        else:
            proxy = proxy.split(":")
            proxy_ip = str(proxy[0]) + ":" + str(proxy[1])
            proxy_port = int(proxy[2].replace(":", ""))
            print(f"{proxy_ip, proxy_port} prepared.")
            break

    return proxy_ip, proxy_port
