import subprocess
 
 
def diagnostico(host):
   comando = f"ping -c 1 {host}"
 
   resultado = subprocess.run(
       comando,
       shell=True,
       capture_output=True,
       text=True
   )
 
   return resultado.stdout
 
 
host_usuario = input("Ingrese un host: ")
print(diagnostico(host_usuario))
 