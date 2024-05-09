import os
from urllib import request
import numpy as np
#import ast 
from zeeguu.config.loader import load_configuration_or_abort
from ._only_teachers_decorator import only_teachers

#print(os.getcwd())
print(np.zeros((2, 2)))
print(print(ast.zeros((2, 2))))
print(load_configuration_or_abort())

@api.route("/has_permission_for_cohort/<id>", methods=["GET"])
@with_session
@only_teachers
def has_permission_for_cohort_api(id):

    if has_permission_for_cohort(id):
        return "OK"
    return "Denied"