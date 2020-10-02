WELCOME_MESSAGE = '{"cards":[{"header":{"title":"Asistencia UD Iris","subtitle":"soporte@udistrital.edu.co","imageUrl":"https://metadata-chat.s3.us-east-2.amazonaws.com/ud-logo.png"},"sections":[{"widgets":[{"keyValue":{"topLabel":"Bienvenido:","content":"Por favor realiza la pregunta que deseas hacer acerca de la universidad y sus dependencias","contentMultiline":"true"}}]}]}]}'
NOT_FOUND_MESSAGE = '{"cards":[{"header":{"title":"Asistencia UD Iris","subtitle":"soporte@udistrital.edu.co","imageUrl":"https://metadata-chat.s3.us-east-2.amazonaws.com/ud-logo.png"},"sections":[{"widgets":[{"keyValue":{"topLabel":"Respuesta no encontrada:","content":"No se encontraron resultados. ¿Quieres buscar en enlaces en la pagina de la universidad?","contentMultiline":"true","button":{"textButton":{"text":"Ver Links Asociados","onClick":{"action":{"actionMethodName":"verLinks","parameters":[{"key":"question","value":"<<QUESTION>>"}]}}}}}}]}]}]}'
RESPONSE_MESSAGE = '{"cards":[{"header":{"title":"Asistencia UD Iris","subtitle":"soporte@udistrital.edu.co","imageUrl":"https://metadata-chat.s3.us-east-2.amazonaws.com/ud-logo.png"},"sections":[{"widgets":[{"keyValue":{"topLabel":"Pregunta:","content":"<<QUESTION>>","contentMultiline":"true"}},{"keyValue":{"topLabel":"Respuesta:","content":"<<RESPONSE>>","contentMultiline":"true"}}]}]}]}'
NOT_FOUND_LINK = 'No encontamos respuesta a tu pregunta, recuerda que puedes llamar al telefono: (+57 1) 3239300 o enviar correo a: soporte@udistrital.edu.co'

# SPACY_PROCESSOR_URL = "http://18.217.22.20:8089"
# SPACY_PROCESSOR_URL = "http://localhost:5000"

SPACY_PROCESSOR_URL = "http://3.236.56.229:8089"
SPACY_PROCESS_QUESTION_ENDPOINT = SPACY_PROCESSOR_URL + "/api/v1/question/similarity"
SPACY_PROCESS_LINK_ENDPOINT = SPACY_PROCESSOR_URL + "/api/v1/question/similarity_page"


ADMIN_URL = " http://54.84.40.204:8080"
ADMIN_LOGGER_ENDPOINT = ADMIN_URL + "/api/v1/logger/"
