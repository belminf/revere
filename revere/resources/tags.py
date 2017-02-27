from flask_restful import reqparse, abort, Resource, marshal, marshal_with
from revere import api
from revere.database import get_db
from revere.models.tags import Tag, TagFields

db_session, db_engine = get_db()


post_parser = reqparse.RequestParser()
post_parser.add_argument('name', type=str, required=True, help="tag name")
post_parser.add_argument('description', type=str, required=True, help="description")


@api.route('/tags/{tag_id}')
class TagResource(Resource):
    def __get_tag(self, tag_id):
        tag = Tag.query.get(tag_id)

        #  Will return None if it doesn't exist
        if not tag:
            abort(404, message="Tag with ID {} doesn't exist.".format(tag_id))

    def get(self, tag_id):
        return dict(self.__get_tag(tag_id))

    def delete(self, tag_id):
        tag = self.__get_tag(tag_id)
        tag.delete()

        return '', 204


@api.route('/tags')
class TagListResource(Resource):

    def get(self):
        return [marshal(t.__dict__, TagFields) for t in Tag.query.all()]

    def post(self):
        args = post_parser.parse_args()

        tag = Tag(**args)

        db_session.add(tag)
        db_session.commit()
        return dict(tag), 201
