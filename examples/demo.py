import asyncio

from tortoise import Tortoise, fields, models

from stoplight import init_anonymizations, Strategies

class Person(models.Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    age = fields.IntField()

    __anonymities__ = [
        ("name", Strategies.SUPPRESS, []),
        ("age", Strategies.VARY, [5])
    ]

    def __str__(self):
        return self.name


async def do_demo():
    # create (automatically commits)
    print("\n\n\nCreating new person with id=1, name=Elias and age=22...")
    p = await Person.create(id=1, name="Elias", age=22)

    print("Fetching record from database...\n")

    # fetch person from database
    me = await Person.filter(id=1).first()
    print("The record stored in the database:", me.name, me.age, "\n\n\n")


async def main():
    # register models
    await Tortoise.init(db_url="sqlite://:memory:", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

    await init_anonymizations()
    await do_demo()

    await Tortoise.close_connections()

if __name__ == "__main__":
    asyncio.run(main())