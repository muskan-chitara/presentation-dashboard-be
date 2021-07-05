from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from enum import Enum

from ..database import (
    retrieve_event,
    retrieve_events,
    retrieve_category,
    retrieve_event_type,
    sort_asc,
    sort_dsc,
)
from ..models.event import (
    ErrorResponseModel,
    ResponseModel,
    EventSchema,
)

router = APIRouter()

class ModelName(str, Enum):
    conference = "conference"
    meeting = "meeting"
    upcoming = "upcoming"
    past = "past"
    sort_asc = "sort_asc"
    sort_dsc = "sort_dsc"

# @router.post("/", response_description="Student data added into the database")
# async def add_student_data(student: StudentSchema = Body(...)):
#    student = jsonable_encoder(student)
#    new_student = await add_student(student)
#    return ResponseModel(new_student, "Student added successfully.")

@router.get("/", response_description="Events retrieved")
def get_events():
    events = retrieve_events()
    if events:
        return ResponseModel(events, "Events data retrieved successfully")
    return ResponseModel(events, "Empty list returned")


@router.get("/models/{model_name}")
def get_model(model_name: ModelName):
    if model_name == ModelName.conference:
        events = retrieve_category(model_name.value)
        if events:
            return ResponseModel(events, "Events time data retrieved successfully")
        return ResponseModel(events, "Empty list returned")

    if model_name == ModelName.meeting:
        events = retrieve_category(model_name.value)
        if events:
            return ResponseModel(events, "Events time data retrieved successfully")
        return ResponseModel(events, "Empty list returned")

    if model_name == ModelName.past:
        events = retrieve_event_type(model_name.value)
        if events:
            return ResponseModel(events, "Events time data retrieved successfully")
        return ResponseModel(events, "Empty list returned")
    if model_name == ModelName.upcoming:
        events = retrieve_event_type(model_name.value)
        if events:
            return ResponseModel(events, "Events time data retrieved successfully")
        return ResponseModel(events, "Empty list returned")
    if model_name == ModelName.sort_dsc:
        events = sort_dsc()
        if events:
            return ResponseModel(events, "Events time data retrieved successfully")
        return ResponseModel(events, "Empty list returned")
    if model_name == ModelName.sort_asc:
        events = sort_asc()
        if events:
            return ResponseModel(events, "Events time data retrieved successfully")
        return ResponseModel(events, "Empty list returned")
    


# @router.put("/{id}")
# async def update_student_data(id: str, req: UpdateStudentModel = Body(...)):
#    req = {k: v for k, v in req.dict().items() if v is not None}
 #   updated_student = await update_student(id, req)
  #  if updated_student:
   #     return ResponseModel(
    #        "Student with ID: {} name update is successful".format(id),
     #       "Student name updated successfully",
    #  )
    #return ErrorResponseModel(
     #   "An error occurred",
      #  404,
       # "There was an error updating the student data.",
    #)

# @router.delete("/{id}", response_description="Student data deleted from the database")
# async def delete_student_data(id: str):
 #   deleted_student = await delete_student(id)
  #  if deleted_student:
   #     return ResponseModel(
    #        "Student with ID: {} removed".format(id), "Student deleted successfully"
     #   )
    #return ErrorResponseModel(
    #    "An error occurred", 404, "Student with id {0} doesn't exist".format(id)
    #)