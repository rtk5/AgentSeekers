from flask import Flask, request

app = Flask(__name__)

# Define the flag
FLAG = "FLAG{you_found_the_secret_flag}"
#
@app.route('/')
def index():
    # Check the user-agent header from the request
    user_agent = request.headers.get('User-Agent')
    
    # If user-agent matches 'agent_program', reveal the flag
    if user_agent == "agent_program":
        return f"Congratulations! Here is your flag: {FLAG}"
    else:
        return "You are not worthy! You shall be allowed, only if you come from agent_program"

if __name__ == "__main__":
    app.run(debug=True)
