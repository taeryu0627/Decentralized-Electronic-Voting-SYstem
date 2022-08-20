from flask import Flask, jsonify, request

app = Flask(__name__)

chain = []
cnt = 0

@app.route('/List', methods=['GET'])
def vote_list():
    return jsonify(chain)


@app.route('/open', methods=['POST'])
def vote_open():
    global cnt
    data = request.get_json()
    block1 = {

        'type': 'open',
        'data': {
            'id': str(cnt),
            'question': data['question'],
            'options': data['options']
        }
    }
    chain.append(block1)
    cnt += 1
    return jsonify({'status': 'success'})

@app.route('/vote', methods=[])
def vote():
    data = request.get_json()
    block = {
        'type': 'vote',
        'data':{
            'vote':data['vote']
        }
    }
    chain.append(block)
    return jsonify({'status':'success'})