
# flask api - pretam jayaswal

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):

		data = "hello from root"
		return jsonify({'data': data})


@app.route('/squre/<int:num>', methods = ['GET'])
def squre(num):

	return jsonify({'data': num**2})


# driver function
if __name__ == '__main__':

	app.run(debug = True)
