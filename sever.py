import socket

ip_address = '192.168.1.85'
PORT = 5678


print('Creating Socket')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(ip_address, PORT)
    print('listening for connections...')
    s.listen(1)
    conn, addr = s.accept()
    print(f'Connection from {addr} established')
    with conn:
        while True:
            host_and_key = conn.recv(1024).decode
            with open('encrypted_hosts.txt', 'a') as f:
                f.write(host_and_key +'\n')
                break
            print('Connection completed and closed!!')
    