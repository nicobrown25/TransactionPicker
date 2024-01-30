# Import Libraries
from flask import Flask, jsonify
from data import transactions_list



# Create Web App
app = Flask(__name__)


# returns list of transactions
@app.route('/get_transactions', methods=['GET'])
def get_transactions():
    response = {'Transactions': transactions_list}
    return jsonify(response), 200




# Returns list of 10 transactions with highest fees
@app.route('/get_ten_highest_fees', methods=['GET'])
def get_ten_highest_fees():
    
    # Input transactions_list as a dummy variable (find_ten_highest)
    ## Sorting algorithm here
    
    find_ten_highest = transactions_list
    
    id_transac_dict = {}
    
    for idx, transaction in enumerate(find_ten_highest):
        current_transaction = transaction['Data'].split()[1]
        id_transac_dict[transaction['ID']] = current_transaction
        
    sorted_id_list = sorted(id_transac_dict.items(), key=lambda x:x[1], reverse=True)[:10]
    
    # [(ID_NUM, TRANSAC), etc.]
    
    top_ten_highest = []
    for id_transac_pair in sorted_id_list:
        top_ten_highest.append(find_ten_highest[id_transac_pair[0] - 1])
    
    
    response = {'Ten Highest Transactions': top_ten_highest} # placeholder
    return jsonify(response), 200




# Returns list of 10 transactions with lowest fees
@app.route('/get_ten_lowest_fees', methods=['GET'])
def get_ten_lowest_fees():

    
    find_ten_lowest = transactions_list
    
    id_transac_dict = {}
    
    for idx, transaction in enumerate(find_ten_lowest):
        current_transaction = transaction['Data'].split()[1]
        id_transac_dict[transaction['ID']] = current_transaction
        
    sorted_id_list = sorted(id_transac_dict.items(), key=lambda x:x[1])[:10]
        
    top_ten_lowest = []
    for id_transac_pair in sorted_id_list:
        top_ten_lowest.append(find_ten_lowest[id_transac_pair[0] - 1])
        
    response = {'Ten Lowest Transactions': top_ten_lowest} # placeholder
    return jsonify(response), 200


    


# Returns second highest total fee sum after picking 10 transactions
@app.route('/get_next_highest_total', methods=['GET'])
def get_next_highest_total():
    find_ten_highest = transactions_list
    
    id_transac_dict = {}
    
    for idx, transaction in enumerate(find_ten_highest):
        current_transaction = transaction['Data'].split()[1]
        id_transac_dict[transaction['ID']] = current_transaction
        
    sorted_id_list = sorted(id_transac_dict.items(), key=lambda x: x[1], reverse=True)
    
    # Extract the IDs of the top 9 highest transactions and the 11th highest transaction
    selected_ids = [sorted_id_list[i][0] for i in range(9)] + [sorted_id_list[10][0]]

    # Retrieve the corresponding transactions based on IDs
    selected_transactions = [find_ten_highest[idx - 1] for idx in selected_ids]
    
    response = {'Selected Transactions': selected_transactions}
    return jsonify(response), 200


# Run app
app.run(host='0.0.0.0', port=5050)