import os

from marshmallow import Schema

from flask import request
from flask.views import MethodView

from core.views.response import APIListResponse, APIDataResponse
from db.models.base import Base

DEFAULT_PAGINATE_BY = os.getenv("DEFAULT_PAGINATE_BY", 10)

class BaseView(MethodView):
    get_schema: Schema = None
    model: Base = None
    post_schema: Schema = None
    
    # Filters for the model
    get_filters = None
    
    # Pagination
    paginate_by = DEFAULT_PAGINATE_BY
    
    # Ordering
    order_by = None
    
    def get(self, *args, **kwargs):
        try:
            if "id" in kwargs:
                # Get single object 
                # Check for the existence of the object
                # And proper authorization
                return APIDataResponse({})
            else:
                limit = int(request.args.get("limit", self.paginate_by))
                offset = int(request.args.get("offset", 0))
                
                if self.get_filters:
                    objects = self.model.filter(self.get_filters)
                else:
                    objects = self.model.filter()
                
                # Apply pagination and ordering
                if self.order_by is not None:
                    objects = objects.order_by(self.order_by)
                
                objects = objects.limit(limit).offset(offset).all()
                
                objects_dump = self.get_schema.dump(obj=objects, many=True)
                return APIListResponse(
                    data=objects_dump, status_code=200, count=len(objects_dump)
                )
        except Exception as e:
            raise e
    