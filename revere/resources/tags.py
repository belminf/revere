from flask_restful import reqparse, abort, Resource
from ..models.tags import Tag
from ..database import get_db


db_session, db_engine = get_db()

post_parser = reqparse.RequestParser()
post_parser.add_argument('id', type=str, required=True, help="unique tag ID")
post_parser.add_argument('name', type=str, required=True, help="tag name")


class TagResource(Resource):
    def __get_tag(self, tag_id):
        tag = Tag.query.get(tag_id)

        #  Will return None if it doesn't exist
        if not tag:
            abort(404, message="Tag with ID {} doesn't exist.".format(tag_id))

    def get(self, tag_id):
        return self.__get_tag(tag_id)

    def delete(self, tag_id):
        tag = self.__get_tag(tag_id)
        tag.delete()

        return '', 204

    def post(self):
        args = post_parser.parse_args()

        tag = Tag(**args)

        db_session.add(tag)
        db_session.commit()
        return tag, 201
