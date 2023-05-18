# import psycopg2
# from flask import Flask, redirect, request
# from multiprocessing import Process
# import logging

# class Server:
#     app = Flask(__name__)
#     server_process = None

#     @staticmethod
#     def run_server():
#         try:
#             Server.app.run(port=8080)
#         except Exception as e:
#             logging.error(e)

#     @staticmethod
#     def start():
#         server_process = Process(target=Server.run_server)
#         server_process.start()
#         Server.server_process = server_process

#     @staticmethod
#     def stop():
#         if Server.server_process:
#             Server.server_process.terminate()
#             Server.server_process.join()

#     @app.route('/')
#     def index():
#         return redirect('https://www.google.com')

#     @app.route('/oauth/callback')
#     def oauth_callback():
#         code = request.args.get('code')
#         return code