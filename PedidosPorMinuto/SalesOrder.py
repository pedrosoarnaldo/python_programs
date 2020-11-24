import pyodbc
import flask

class SalesOrder:
    """"Class responsible to get amount of orders from database"""

    def set_api(self):
        app = flask.Flask(__name__)
        app.config["DEBUG"] = True

        @app.route('/', methods=['GET'])
        def homepage():
            return """<h1>OK</h1>"""

        @app.route('/pedidos', methods=['POST'])
        def home():
            cmd = ""
            minutes = flask.request.form.get('text')

            try:
                return_query = self.get_order(minutes)
            except:
                return_query = self.get_order('1')

            for key in return_query:
                cmd = cmd + key + " -> " + str(return_query[key]) + "\n"

            cmd = cmd + "\n Bom final de semana brother!\n"
            return cmd

        app.run(host = '0.0.0.0')

    def get_order(self, minutes):

        if int(minutes) >= 60:
            minutes = 60

        amount_orders = {}
        # Some other example server values are
        # server = 'localhost\sqlexpress' # for a named instance
        # server = 'myserver,port' # to specify an alternate port

        server   = 'server.dc.intra\INSTANCE_NAME,1433'
        database = 'Database_Name'
        username = 'user'
        password = 'password'


        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        cmd = "SELECT convert(varchar(5), p.CriadoEm, 108), count(p.Id) FROM database_name.dbo.Tabela p (NOLOCK) WHERE p.CriadoEm >= DATEADD(minute,-" + minutes + ",GETDATE()) and p.CriadoEm < GETDATE() group by convert(varchar(5), p.CriadoEm, 108) order by 1"
        print(cmd)
        #Sample select query
        cursor.execute(cmd)
        row = cursor.fetchone()

        while row:
            amount_orders[row[0]] = row[1]
            row = cursor.fetchone()

        return amount_orders
