from abc import ABC


class AbstractRepository(ABC):
    async def exists(self, *args, **kwargs):
        raise NotImplementedError

    async def get_one(self, *args, **kwargs):
        raise NotImplementedError

    async def create_one(self, *args, **kwargs):
        raise NotImplementedError

    async def update_one(self, *args, **kwargs):
        raise NotImplementedError

    async def remove_one(self, *args, **kwargs):
        raise NotImplementedError

    async def get_list(self, *args, **kwargs):
        raise NotImplementedError
