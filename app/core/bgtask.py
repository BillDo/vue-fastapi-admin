from starlette.background import BackgroundTasks

from .ctx import CTX_BG_TASKS


class BgTasks:
    """Unified management of background tasks"""

    @classmethod
    async def init_bg_tasks_obj(cls):
        """Instantiate background tasks and set them in the context"""
        bg_tasks = BackgroundTasks()
        CTX_BG_TASKS.set(bg_tasks)

    @classmethod
    async def get_bg_tasks_obj(cls):
        """Get the background tasks instance from the context"""
        return CTX_BG_TASKS.get()

    @classmethod
    async def add_task(cls, func, *args, **kwargs):
        """Add a background task"""
        bg_tasks = await cls.get_bg_tasks_obj()
        bg_tasks.add_task(func, *args, **kwargs)

    @classmethod
    async def execute_tasks(cls):
        """Execute background tasks, usually after the request has been returned to the client"""
        bg_tasks = await cls.get_bg_tasks_obj()
        if bg_tasks.tasks:
            await bg_tasks()
