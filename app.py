import subprocess
 
 
def diagnostico(host):
    resultado = subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True,
        text=True
    )
 
    return resultado.stdout
 
 
host_usuario = input("Ingrese un host: ")
print(diagnostico(host_usuario))