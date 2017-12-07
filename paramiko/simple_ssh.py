import paramiko

with paramiko.SSHClient() as p:
    p.load_system_host_key()

    p.connect('192.168.0.3', port=22, username='root', password='root')

    stdin, stdout, stderr = p.exec_command('poweroff')

    print stdout.read()

