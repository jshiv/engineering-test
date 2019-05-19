'''Config file db credentials'''
import os

DATABASE="zesty"
USER="postgres"
PASSWORD="engineTest888"
HOST=os.environ.get('POSTGRES_HOST',"localhost")
PORT=int(os.environ.get('POSTGRES_PORT', 5432))
