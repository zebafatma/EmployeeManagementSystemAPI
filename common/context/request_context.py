from starlette_context import context


class RequestContext:

    @staticmethod
    def set_current_user(user):
        context["current_user"] = user

    @staticmethod
    def get_current_user():
        if context.exists():
            return context.get("current_user")
        return None
