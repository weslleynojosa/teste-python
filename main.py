from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)


# Company Class/Model
class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    current_version = db.Column(db.String(10))
    should_update = db.Column(db.String(3))

    def __init__(self, name, current_version, should_update):
        self.name = name
        self.current_version = current_version
        self.should_update = should_update


class CompanySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'current_version', 'should_update')


# Version Class/Model
class Version(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    version_number = db.Column(db.String(10), unique=True)
    description = db.Column(db.String(200))
    date = db.Column(db.String(10))

    def __init__(self, version_number, description, date):
        self.version_number = version_number
        self.description = description
        self.date = date


# Version Schema
class VersionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'version_number', 'description', 'date')


# Init schema
company_schema = CompanySchema(strict=True)
companies_schema = CompanySchema(many=True, strict=True)
version_schema = VersionSchema(strict=True)
versions_schema = VersionSchema(many=True, strict=True)


@app.route('/company', methods=['POST'])
def add_company():
    name = request.json['name']
    current_version = request.json['current_version']
    should_update = request.json['should_update']

    new_company = Company(name, current_version, should_update)
    db.session.add(new_company)
    db.session.commit()

    return company_schema.jsonify(new_company)


@app.route('/company', methods=['GET'])
def get_companies():
    all_companies = Company.query.all()
    result = companies_schema.dump(all_companies)

    return jsonify(result.data)


@app.route('/company/<id>', methods=['GET'])
def get_company(id):
    company = Company.query.get(id)
    return company_schema.jsonify(company)


# Update a Company
@app.route('/company/<id>', methods=['PUT'])
def update_company(id):
    company = Company.query.get(id)

    name = request.json['name']
    current_version = request.json['current_version']
    should_update = request.json['should_update']

    company.name = name
    company.currentVersion = current_version
    company.shouldUpdate = should_update

    db.session.commit()

    return company_schema.jsonify(company)


# Delete Company
@app.route('/company/<id>', methods=['DELETE'])
def delete_company(id):
    product = Version.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return version_schema.jsonify(product)


# Create a Version
@app.route('/version', methods=['POST'])
def add_version():
    version_number = request.json['version_number']
    description = request.json['description']
    date = request.json['date']

    new_version = Version(version_number, description, date)

    db.session.add(new_version)
    db.session.commit()

    return version_schema.jsonify(new_version)


# Get All Versions
@app.route('/version', methods=['GET'])
def get_versions():
    all_versions = Version.query.all()
    result = versions_schema.dump(all_versions)
    return jsonify(result.data)


# Get Single Version
@app.route('/version/<id>', methods=['GET'])
def get_version(id):
    version = Version.query.get(id)
    return version_schema.jsonify(version)


# Update a Version
@app.route('/version/<id>', methods=['PUT'])
def update_version(id):
    version = Version.query.get(id)

    version_number = request.json['version_number']
    description = request.json['description']
    date = request.json['date']

    version.version_number = version_number
    version.description = description
    version.date = date

    db.session.commit()

    return version_schema.jsonify(version)


# Delete Version
@app.route('/version/<id>', methods=['DELETE'])
def delete_version(id):
    version = Version.query.get(id)
    db.session.delete(version)
    db.session.commit()
    return version_schema.jsonify(version)


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
