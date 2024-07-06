import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def getAllPoints(self):
        query = "SELECT address FROM points"
        return await self.connector.fetch(query)

    async def getInformationFromVacancy(self, city,vacancy):
        query = (f"SELECT * FROM information "
                 f"WHERE vacancy = '{vacancy}' AND city = '{city}'")
        return await self.connector.fetch(query)

