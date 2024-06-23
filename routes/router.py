from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort, url_for

#import json

router = Blueprint('api', __name__)

@router.route('/')
def home():
    return render_template('index.html')

