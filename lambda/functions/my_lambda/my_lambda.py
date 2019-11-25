import os
import urllib
import uuid
import boto3
import json
import logging
from elasticsearch import Elasticsearch, RequestsHttpConnection, helpers
from requests_aws4auth import AWS4Auth

def lambda_handler(event, context):
    print('--> ALL IMPORTS PASS! <--')