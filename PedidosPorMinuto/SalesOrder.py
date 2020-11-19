import pyodbc
import json
import flask

class SalesOrder:
    """"Class responsible to get amount of orders from database"""

    def set_api(self):
        app = flask.Flask(__name__)
        app.config["DEBUG"] = True

        @app.route('/', methods=['GET'])
        def home():
            json_object_return = self.get_order()
            return json_object_return

        app.run(host = '0.0.0.0')

    def get_order(self):

            amount_orders = {}
            # Some other example server values are
            # server = 'localhost\sqlexpress' # for a named instance
            # server = 'myserver,port' # to specify an alternate port

            server = 'xxxxx..dc.sbnet\xxxx,1433'
            database = 'database_name'
            username = 'user'
            password = 'password'

            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            cursor = cnxn.cursor()
            cmd = "SELECT distinct (COUNT(p.Id)/10) AS AVG_10_M,(SELECT distinct COUNT(p.Id) AS AVG_10_M FROM database_name.dbo.orders p (NOLOCK) WHERE p.CriadoEm >= DATEADD(minute,-1,GETDATE()) and p.CriadoEm < GETDATE()) AS last_minute FROM database_name.dbo.orders p (NOLOCK) WHERE p.CriadoEm >= DATEADD(minute,-11,GETDATE()) AND p.CriadoEm < DATEADD(minute,-2,GETDATE())"

            #Sample select query
            cursor.execute(cmd)
            row = cursor.fetchone()

            while row:
                amount_orders['last_10m'] = row[0]
                amount_orders['last_1m'] = row[1]
                row = cursor.fetchone()

            json_object = json.dumps(amount_orders, indent=4)
            return json_object
