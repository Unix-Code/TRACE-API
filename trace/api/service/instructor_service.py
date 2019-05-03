from sqlalchemy_utils import sort_query

from api.model.course import Course
from api.model.instructor import Instructor


def get_all_instructors(page, page_size, sort, term_id=None, department_id=None):
    query = Instructor.query
    if term_id is not None or department_id is not None:
        filter_params = {**(term_id is not None and {'term_id': term_id} or {}),
                         **(department_id is not None and {'department_id': department_id} or {})}
        ids_subquery = Course.query.with_entities(Course.instructor_id).filter_by(**filter_params).distinct()
        query = query.filter(Instructor.id.in_(ids_subquery))
    sql_results = sort_query(query, sort).paginate(page, page_size, False).items
    return [inst.as_dict() for inst in sql_results]


def get_single_instructor(instructor_id):
    result = Instructor.query.get(instructor_id)
    return result.as_dict() if result is not None else result
