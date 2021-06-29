from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class EventSchema(BaseModel):
    date: str = Field(default="NA")
    duration: str = Field(default="NA")
    title: str = Field(default="NA")
    link: str = Field(default="NA")
    summary: str = Field(default="NA")
    attachment: str = Field(default="NA")

    class Config:
        schema_extra = {
            "example": {
                "date": "Friday, July 30, 2021",
                "duration": "7:00am - 8:00am PDT",
                "title": "WY Q2 2021 Earnings Webcast and Conference Call",
                "link": "https://investor.weyerhaeuser.com/events-and-presentations?item=124",
                "summary": "Join us on Friday, July 30 for our Q2 2021 earnings results webcast and conference call. Read the release",
                "attachment": "https://investor.weyerhaeuser.com/events-and-presentations?item=124",
            }
            
        }


# class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources and environmental engineering",
                "year": 4,
                "gpa": "4.0",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}