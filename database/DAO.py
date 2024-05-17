from database.DB_connect import DBConnect
from model.contiguity import Contiguity
from model.country import Country


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllConfiniPerAnno(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = ("""select *
                    from countries.contiguity c 
                    where c.`year` <= %s and c.conttype = 1""")
        cursor.execute(query, (year,))
        for row in cursor:
            result.append(
                Contiguity(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllCountry():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from countries.country c"""
        cursor.execute(query)
        for row in cursor:
            result.append(
                Country(**row))
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getAllCountryExisting(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT c.StateAbb, c.CCode, c.StateNme
                    FROM countries.country c, countries.contiguity c2
                    WHERE (c2.state1no = c.CCode OR c.CCode = c2.state2no)
                    AND c2.year <= %s;
                    """
        cursor.execute(query, (year, ))
        for row in cursor:
            result.append(
                Country(**row))
        cursor.close()
        conn.close()
        return result
