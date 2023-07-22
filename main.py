import asyncio
from utils import database_funcs


async def main():
    e = await database_funcs.login_user(
        email="asfsfaasfasfsfaassf@gmail.com", password="something123"
    )
    a = await database_funcs.logout_user()
    print(a)

    return


if __name__ == "__main__":
    asyncio.run(main())
