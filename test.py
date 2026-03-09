from RPYC.remote_control import RemoteControlConnection

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 5000
    r = RemoteControlConnection(ip, port)
    f = r.modules.builtins.open("gal.txt", "w")
    print(f.write("gal"))
    f.close()
