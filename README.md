# introduction-quiz
	
#INSTRUCCIONES 

1. Instalar electisearch y levantar el servicio con `sudo systemctl start elasticsearch.service`

2. El programa es compatible con la versión de python 2.7. 

3. Instalar las librerias si es necesario de `requests` y `json`

4. En consola ejecutar el archivo `send_answers.py` con el siguiente comando `python send_answers.py`

5. Para imprimir la respuesta del request es necesario usar el siguiente comando: 
	* ` curl -XGET 'http://localhost:9200/quiz/post/1?pretty'`
 



