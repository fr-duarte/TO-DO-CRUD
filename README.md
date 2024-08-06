# Uso e instalaciones 
    
1. Instalas un entorno virtual y lo activas
   * En este caso te va a decir que tenes el usuarios restringido luego de ejecutar `Get-ExecutionPolicy`. 
   * Para eso tenes que abrir vs code como administrador y ejecutar en la terminal `Set-ExecutionPolicy RemoteSigned` en la terminal 
   * Ahora si creas el entorno virtual con `python -m venv venv` 
   * Por ultimo lo activas con `.\venv\Scripts\Activate`
2. Instalar dependencias
    * Instalas las dependencias ejecutando `pip install -r requirements.txt` en la terminal
3. Ejecutar projectp con el comando `python index.py`