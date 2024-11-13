import os

import app


class Config:
    SQLALCHEMY_DATABASE_URI = ('postgresql://neondb_owner:eJpC9dIcNb4h@ep-frosty-snow-a5z0mc27.us-east-2.aws.neon.tech'
                               '/neondb?sslmode=require')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
