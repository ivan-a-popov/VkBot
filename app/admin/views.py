from hashlib import sha256

from aiohttp.web_exceptions import HTTPBadRequest, HTTPForbidden, HTTPMethodNotAllowed
from aiohttp_apispec import request_schema, response_schema
from app.admin.schemas import AdminSchema
from app.web.app import View
from app.web.schemas import OkResponseSchema
from app.web.utils import json_response


# TODO: добавить проверку авторизации для этого View
class AdminLoginView(View):
    @request_schema(AdminSchema)
    @response_schema(OkResponseSchema, 200)
    async def post(self):
        email = self.data["email"]
        if not email:
            raise HTTPBadRequest
        password = self.data["password"]
        admin = await self.request.app.store.admins.get_by_email(email=email)
        if not admin or admin.password != sha256(password.encode()).hexdigest():
            raise HTTPForbidden
        return json_response(data={"id": admin.id, "email": admin.email})

    async def get(self):
        raise HTTPMethodNotAllowed("get", "post")


class AdminCurrentView(View):
    async def get(self):
        raise NotImplementedError
