#$P es igual a la particion donde se ubica la aplicacion de python
$P = (get-command python.exe).Path
#$A, con -Execute se especifica la aplicacion con la que se ejecutara el programa, -Argument es el programa que se va ejecutar, -workingDirectory es el directorio donde se encuentra el programa
$A = New-ScheduledTaskAction -Execute $P -Argument "actualizador.py" -workingDirectory "Ejemplo: C:\Usuario\..."
#$T Se aplican desencadenadores, el cual se ejecutara diariamente con -Daily y sera a las 8:00 pm con -At
$T = New-ScheduledTaskTrigger -Daily -At "8pm"
#$S Se aplican los ajustes que tendra la tarea, en donde por un intervalo de cada 10 minutos y 12 reinicios, la tarea se ejcutara, al mismo tiempo se crea un cronometro donde el limite son 5 horas
$S = New-ScheduledTaskSettingsSet -RestartInterval(New-TimeSpan -Minutes 10) -ExecutionTimeLimit(New-TimeSpan -Hours 5) -RestartCount 12
#Se ejecuta el registro de la tarea en el programador de tareas preservando los parametros configurados en las variables
Register-ScheduledTask Actualizador -RunLevel Highest -Trigger $T -Action $A -Settings $S