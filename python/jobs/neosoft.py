# -------- difference between shallow copy and deep copy

# import copy

# original_list = [[1, 2, 3], [4, 5, 6]]

# # normal copy
# normal_copied_list = original_list
# print("normal_copied_list Copied List 1 >>>>>:", normal_copied_list)

# # Shallow copy
# shallow_copied_list = copy.copy(original_list)

# # Deep copy
# deep_copied_list = copy.deepcopy(original_list)

# # Modify the original list
# original_list[0][0] = 99

# print("Original List:", original_list)
# print("normal_copied_list :", normal_copied_list)
# print("Shallow Copied List:", shallow_copied_list)
# print("Deep Copied List:", deep_copied_list)

# ---------- why we use cros
from flask import Flask, jsonify
from flask_cors  import CORS

app = Flask(__name__)
CORS(app)
# def create_app():
#     @app.route('/api')
#     def api():
#         return jsonify({'data' : 'Hello World !'})
#     return app

@app.route('/api')
def api():
    return jsonify({'data' : 'Hello World !'})

if __name__ == '__main__':
    app.run()
