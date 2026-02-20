from flask import Flask, request, jsonify
from flask_cors import CORS
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Inicializa o Flask (nosso servidor backend)
app = Flask(__name__)
# Permite que o index.html acesse o servidor sem bloqueios de segurança
CORS(app)

# --- CONFIGURAÇÕES DA IBM ---
CHAVE_API = '3SCCit8wW6s-wVcJbnvJeKA8449Kqb8xSL8vhmT_FTo9'
URL_SERVICO = 'https://api.us-south.assistant.watson.cloud.ibm.com/instances/71ca2c9d-0b98-4968-8be2-d40a742a7fdf'
ID_ASSISTENTE = '974d9a1f-2d24-4c6f-b582-b91a2968a510'

# Configura a autenticação com os servidores da IBM
authenticator = IAMAuthenticator(CHAVE_API)
assistant = AssistantV2(version='2021-11-27', authenticator=authenticator)
assistant.set_service_url(URL_SERVICO)

# Rota que recebe as mensagens vindas do site (index.html)
@app.route('/conversa', methods=['POST'])
def conversa():
    dados = request.json
    pergunta_usuario = dados.get('texto')
    
    try:
        # Comunicação Stateless: Envia a pergunta e o user_id para o Watson
        resposta = assistant.message_stateless(
            assistant_id=ID_ASSISTENTE,
            environment_id=ID_ASSISTENTE,
            input={
                'message_type': 'text',
                'text': pergunta_usuario
            },
            user_id='usuario_cardioia_001' 
        ).get_result()
        
        # Devolve a resposta do robô para o site em formato JSON
        return jsonify(resposta)
    
    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"erro": str(e)}), 500

# Inicia o servidor na porta 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)